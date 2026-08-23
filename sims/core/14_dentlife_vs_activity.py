"""
Prediction (D1 tension): busy sites erase their own marks faster.
Carved-bed world: plateau with channels; plant identical test dents (small deepenings) at
channel sites spanning a range of local discharge Q; measure each dent's decay time.
Mechanism expected: erosion/deposition churn scales with Q (activity), so T_eff rises with Q,
so dent-life falls with Q. Measure: dent half-life vs Q, log-log slope.
"""
import numpy as np
def route(z):
    nx,ny=z.shape; best=np.full((nx,ny),-1); bs=np.full((nx,ny),-np.inf)
    idx=np.arange(nx*ny).reshape(nx,ny)
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if dx==0 and dy==0: continue
            zn=np.roll(np.roll(z,-dx,0),-dy,1); s=(z-zn)/np.hypot(dx,dy)
            if dx==1: s[-1,:]=-np.inf
            if dx==-1: s[0,:]=-np.inf
            if dy==1: s[:,-1]=-np.inf
            if dy==-1: s[:,0]=-np.inf
            m=s>bs; bs[m]=s[m]; best[m]=np.roll(np.roll(idx,-dx,0),-dy,1)[m]
    return best,bs
def step(z,k=0.02,m_exp=0.5,noise=0.004,lam=0.01,rng=None):
    nx,ny=z.shape
    best,slope=route(z)
    Q=np.full(nx*ny,1.0); order=np.argsort(-z.ravel()); b=best.ravel()
    for i in order:
        if b[i]>=0: Q[b[i]]+=Q[i]
    Q=Q.reshape(nx,ny)
    E=k*(Q**m_exp)*(np.clip(slope,0,None))
    # activity-scaled churn: random erosion/deposition with sd ∝ sqrt(Q) (extensive contact)
    churn=noise*np.sqrt(Q)*rng.standard_normal((nx,ny))
    z=z-np.minimum(E,0.5)+churn
    z=z+lam*(np.roll(z,1,0)+np.roll(z,-1,0)+np.roll(z,1,1)+np.roll(z,-1,1)-4*z)*0.25
    z[0,:]=0.0
    return z,Q
def run(seed=0,nx=70,ny=70,burn=400,depth=0.6,track=250):
    rng=np.random.default_rng(seed)
    X=np.arange(nx)[:,None]; z=10.0+0.002*X+0.05*rng.standard_normal((nx,ny)); z[0,:]=0.0
    for t in range(burn): z,Q=step(z,rng=rng)
    # choose dent sites across Q deciles (channel cells only, away from outlet)
    cells=[(i,j) for i in range(5,nx-5) for j in range(3,ny-3)]
    qs=np.array([Q[i,j] for i,j in cells]); order=np.argsort(qs)
    picks=[cells[order[int(f*(len(order)-1))]] for f in np.linspace(0.55,0.999,10)]
    z0=z.copy()
    for (i,j) in picks: z[i,j]-=depth          # plant identical dents
    ref=z0
    Qs=[]; halflives=[]
    dent0={p:depth for p in picks}
    alive=dict(dent0); tdead={}
    for t in range(track):
        z,Q=step(z,rng=rng)
        ref,_=step(ref,rng=np.random.default_rng(seed+999+t))  # control surface evolves too
        for p in list(alive):
            i,j=p; d=(ref[i,j]-z[i,j])          # remaining dent vs control
            if d<depth/2 and p not in tdead: tdead[p]=t+1; del alive[p]
    for p in picks:
        i,j=p; Qs.append(Q[i,j]); halflives.append(tdead.get(p,track))
    return np.array(Qs),np.array(halflives)
allQ=[]; allH=[]
for s in range(4):
    q,h=run(seed=s); allQ+=list(q); allH+=list(h)
allQ=np.array(allQ); allH=np.array(allH)
ok=(allQ>0)&(allH>0)
slope=np.polyfit(np.log(allQ[ok]),np.log(allH[ok]),1)[0]
print(f"dent half-life vs local discharge: log-log slope = {slope:+.2f}  (prediction: negative)")
for lo,hi,lab in [(0,np.median(allQ),'low-Q half'),(np.median(allQ),1e9,'high-Q half')]:
    m=(allQ>=lo)&(allQ<hi)
    print(f"  {lab}: median Q={np.median(allQ[m]):.0f}, median half-life={np.median(allH[m]):.0f} steps")
