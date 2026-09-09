"""
Historical implementation: its routing can send water uphill from a pit.
Use sims/validation/construction.py and run_construction for the corrected
downhill and outlet accounting. These old results are not current validation.

Held-back gradient test. A raised, nearly flat, noisy plateau of erodible material.
Rain falls uniformly. Water can only leave at the bottom edge (base level).
Rules: water flows to the lowest of 8 neighbours; a cell's discharge = its rain + everything routed into it;
erosion rate = k * discharge^m * slope^n   (stream power; m>0 means flow concentrates its own cutting)
Control: m=0, erosion depends on slope only (linear-in-flow: no concentration feedback).
Nothing tells the plateau to make channels. Watch whether it does.
"""
import numpy as np
def route(z):
    nx,ny=z.shape; best=np.full((nx,ny),-1); bs=np.full((nx,ny),-np.inf)
    idx=np.arange(nx*ny).reshape(nx,ny)
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if dx==0 and dy==0: continue
            zn=np.roll(np.roll(z,-dx,0),-dy,1); s=(z-zn)/np.hypot(dx,dy)
            # no wrap in x; y wraps? no: treat both edges as walls except bottom outlet
            if dx==1: s[-1,:]=-np.inf
            if dx==-1: s[0,:]=-np.inf
            if dy==1: s[:,-1]=-np.inf
            if dy==-1: s[:,0]=-np.inf
            m=s>bs; bs[m]=s[m]; best[m]=np.roll(np.roll(idx,-dx,0),-dy,1)[m]
    return best,bs
def step(z,k,m_exp,n_exp=1.0,rain=1.0,outlet_row=0):
    nx,ny=z.shape
    best,slope=route(z)
    Q=np.full(nx*ny,rain)
    order=np.argsort(-z.ravel())         # high to low
    b=best.ravel()
    for i in order:
        if b[i]>=0: Q[b[i]]+=Q[i]
    Q=Q.reshape(nx,ny)
    E=k*(Q**m_exp)*(np.clip(slope,0,None)**n_exp)
    E[outlet_row,:]=0
    z=z-np.minimum(E, 0.5)   # cap per-step cut
    z[outlet_row,:]=0.0
    return z,Q
def run(m_exp, nx=80, ny=80, steps=1200, k=None, seed=0):
    rng=np.random.default_rng(seed)
    X=np.arange(nx)[:,None]
    z=10.0+0.002*X+0.05*rng.standard_normal((nx,ny))  # plateau, tiny tilt toward row 0, noise
    z[0,:]=0.0                                        # base level
    if k is None: k={0.0:0.3,0.5:0.02,1.0:0.002}[m_exp]
    hist=[]
    for t in range(steps):
        z,Q=step(z,k,m_exp)
        if t%50==0 or t==steps-1:
            row=Q[1,:]                                # discharge just above outlet
            tot=row.sum(); top=np.sort(row)[::-1]
            nch=int((row>0.02*tot).sum())             # channels carrying >2% of flow
            hist.append((t,nch,float(top[0]/tot),float(top[:3].sum()/tot)))
    return z,Q,hist
if __name__=="__main__":
    import json, time
    t0=time.time(); out={}
    for lab,m in [('full_m0.5',0.5),('full_m1',1.0),('linear_m0',0.0)]:
        z,Q,h=run(m); out[lab]=dict(hist=h,z=z.tolist(),Q=Q.tolist())
        print(lab,'(t, n_channels, share of biggest, share of top3):',[(a,b,round(c,2),round(d,2)) for a,b,c,d in h[::4]],flush=True)
    json.dump(out,open('/home/claude/heldback.json','w')); print(time.time()-t0)
