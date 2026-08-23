"""
h2: does heredity self-emerge from flow, and what kills it?
Plateau world (stream-power incision). Trait = incision depth (local relief).
Junctions = one downstream trunk, two upstream branches (splitting seen along flow).
Confound control: regress log(incision) on log(Q), log(slope) across all channel cells; use residuals.
h2 = OLS slope of daughter residual on parent residual across junctions.
Dial: bed healing rate lam (diffusive relaxation erasing carved memory).
Predict: h2 > 0 at lam=0, -> 0 as lam grows; channels die at high lam.
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
def lap(z):
    return (np.roll(z,1,0)+np.roll(z,-1,0)+np.roll(z,1,1)+np.roll(z,-1,1)-4*z)
def run(lam, nx=80, ny=80, steps=600, m_exp=0.5, k=0.02, seed=0):
    rng=np.random.default_rng(seed)
    X=np.arange(nx)[:,None]
    z=10.0+0.002*X+0.05*rng.standard_normal((nx,ny)); z[0,:]=0.0
    for t in range(steps):
        best,slope=route(z)
        Q=np.full(nx*ny,1.0); order=np.argsort(-z.ravel()); b=best.ravel()
        for i in order:
            if b[i]>=0: Q[b[i]]+=Q[i]
        Q=Q.reshape(nx,ny)
        E=k*(Q**m_exp)*(np.clip(slope,0,None)**1.0); E[0,:]=0
        z=z-np.minimum(E,0.5)
        z=z+lam*lap(z)                      # healing: erases carved memory
        z[0,:]=0.0
    return z,Q,best
def h2_measure(z,Q,best,qthresh=8.0):
    nx,ny=z.shape; N=nx*ny
    chan=(Q.ravel()>=qthresh)
    # incision = local median relief
    from scipy.ndimage import median_filter
    rel=(median_filter(z,size=7)-z).ravel()
    # residual: log rel ~ log Q + log slope proxy (use downstream drop)
    b=best.ravel(); drop=np.zeros(N)
    valid=b>=0; drop[valid]=z.ravel()[valid]-z.ravel()[b[valid]]
    sel=chan&(rel>1e-3)&(drop>1e-4)
    import numpy.linalg as la
    Xd=np.column_stack([np.log(Q.ravel()[sel]),np.log(drop[sel]),np.ones(sel.sum())])
    y=np.log(rel[sel]); coef,_,_,_=la.lstsq(Xd,y,rcond=None)
    res=np.full(N,np.nan); res[sel]=y-Xd@coef
    # junctions: channel cell receiving >=2 channel inflows
    inflows={}
    for i in range(N):
        if chan[i] and b[i]>=0 and chan[b[i]]:
            inflows.setdefault(b[i],[]).append(i)
    pairs=[]
    for j,ups in inflows.items():
        if len(ups)>=2 and not np.isnan(res[j]):
            for u in ups:
                # daughter trait: mean residual over 3 cells walking upstream from u
                seg=[]; c=u
                for _ in range(3):
                    if np.isnan(res[c]): break
                    seg.append(res[c])
                    prev=[p for p,dn in [(p,b[p]) for p in inflows.get(c,[])] if chan[p]]
                    ups2=[p for p in range(N) if b[p]==c and chan[p]]
                    if len(ups2)!=1: break
                    c=ups2[0]
                if seg: pairs.append((res[j],np.mean(seg)))
    if len(pairs)<8: return float('nan'),len(pairs)
    P=np.array(pairs); slope=np.polyfit(P[:,0],P[:,1],1)[0]
    return float(slope),len(pairs)
if __name__=="__main__":
    for lam in [0.0,0.02,0.05,0.12]:
        agg=[]; npairs=0
        for seed in range(3):
            z,Q,best=run(lam,seed=seed)
            h,n=h2_measure(z,Q,best); npairs+=n
            if h==h: agg.append(h)
        print(f"lam={lam}: h2 = {np.mean(agg):+.2f} ± {np.std(agg):.2f}  (junction-daughter pairs: {npairs})",flush=True)

def h2_v2(z,Q,best,qthresh=8.0,nnull=2000,seed=0):
    """Distance-matched null: related-pair corr minus unrelated same-distance corr."""
    import numpy as np
    from scipy.ndimage import median_filter
    rng=np.random.default_rng(seed)
    nx,ny=z.shape; N=nx*ny
    chan=(Q.ravel()>=qthresh)
    rel=(median_filter(z,size=7)-z).ravel()
    b=best.ravel(); drop=np.zeros(N); valid=b>=0
    drop[valid]=z.ravel()[valid]-z.ravel()[b[valid]]
    sel=chan&(rel>1e-3)&(drop>1e-4)
    Xd=np.column_stack([np.log(Q.ravel()[sel]),np.log(drop[sel]),np.ones(sel.sum())])
    y=np.log(rel[sel]); coef,_,_,_=np.linalg.lstsq(Xd,y,rcond=None)
    res=np.full(N,np.nan); res[sel]=y-Xd@coef
    ij=lambda i:(i//ny,i%ny)
    # related pairs: junction j, daughter start u (adjacent channel cells)
    inflows={}
    for i in range(N):
        if chan[i] and b[i]>=0 and chan[b[i]]: inflows.setdefault(b[i],[]).append(i)
    rel_pairs=[]; dists=[]
    for j,ups in inflows.items():
        if len(ups)>=2 and not np.isnan(res[j]):
            for u in ups:
                if not np.isnan(res[u]):
                    rel_pairs.append((res[j],res[u]))
                    (x1,y1),(x2,y2)=ij(j),ij(u); dists.append(np.hypot(x1-x2,y1-y2))
    if len(rel_pairs)<8: return np.nan,np.nan,len(rel_pairs)
    R=np.array(rel_pairs); dmean=np.mean(dists)
    # null pairs: random channel-cell pairs at the same distance (±0.5), NOT in parent-daughter relation
    cand=np.where(sel)[0]; null_pairs=[]
    tries=0
    while len(null_pairs)<nnull and tries<50*nnull:
        tries+=1
        a,c=rng.choice(cand,2,replace=False)
        (x1,y1),(x2,y2)=ij(a),ij(c)
        if abs(np.hypot(x1-x2,y1-y2)-dmean)<=0.6 and b[a]!=c and b[c]!=a:
            null_pairs.append((res[a],res[c]))
    Nl=np.array(null_pairs)
    corr_rel=np.corrcoef(R[:,0],R[:,1])[0,1]
    corr_null=np.corrcoef(Nl[:,0],Nl[:,1])[0,1] if len(Nl)>8 else np.nan
    return corr_rel, corr_null, len(rel_pairs)
if True:
    import numpy as np
    print("\nv2: related-pair correlation vs distance-matched unrelated null (excess = heredity)")
    for lam in [0.0,0.05,0.12]:
        ex=[]
        for seed in range(3):
            z,Q,best=run(lam,seed=seed)
            cr,cn,n=h2_v2(z,Q,best,seed=seed)
            if cr==cr and cn==cn: ex.append((cr,cn))
        if ex:
            cr=np.mean([a for a,_ in ex]); cn=np.mean([b for _,b in ex])
            print(f"lam={lam}: related {cr:+.2f}  null {cn:+.2f}  excess {cr-cn:+.2f}",flush=True)
