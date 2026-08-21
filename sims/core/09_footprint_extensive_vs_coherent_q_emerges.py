"""
P6a from geometry + independence, tested. No RNG after t=0.
Substrate: B independent KxK chaotic coupled-map blocks (mixing patches).
Channels: N=40 sharing fixed flux; footprint n_i = number of blocks touched, proportional to share; per-block coupling FIXED.
Extensive case: kick_i = kappa * sum over its n_i blocks of that block's fluctuation  -> predict var ∝ share^1.
Coherent control: kick_i = kappa * n_i * (one shared block's fluctuation)            -> predict var ∝ share^2.
Fixed-footprint control (original design): kick_i = kappa * share*N * (own single block) -> var ∝ share^2.
"""
import numpy as np
def run(mode='extensive', N=40, B=1500, K=4, steps=25000, kappa=0.35, gmin=0.02, seed=0):
    rng=np.random.default_rng(seed)                 # initial condition only
    X=rng.random((B,K,K))
    g=np.full(N,1.0)+0.01*rng.standard_normal(N)
    mu=X.mean(axis=(1,2))
    kicks=[]; shares=[]
    for t in range(steps):
        Y=4*X*(1-X)
        X=0.9*Y+0.1*0.25*(np.roll(Y,1,1)+np.roll(Y,-1,1)+np.roll(Y,1,2)+np.roll(Y,-1,2))
        gray=X.mean(axis=(1,2)); mu=0.999*mu+0.001*gray; fluc=gray-mu
        share=g/g.sum()
        n=np.maximum(1,np.round(share*(B-N)).astype(int))       # footprint ∝ share
        off=np.concatenate([[0],np.cumsum(n)[:-1]])
        if mode=='extensive':
            kick=np.array([kappa*fluc[off[i]:off[i]+n[i]].sum() for i in range(N)])
        elif mode=='coherent':
            kick=kappa*n*fluc[0]
        else:  # fixed footprint, amplitude ∝ share (the original noise_from_layers design)
            kick=kappa*share*N*fluc[:N]
        g=np.maximum(g+kick,gmin)
        if t>steps//2 and t%25==0: kicks.append(kick.copy()); shares.append(share.copy())
    kicks=np.array(kicks); shares=np.array(shares); v=kicks.var(0); m=shares.mean(0)
    ok=(v>1e-30)&(m>0); slope=float(np.polyfit(np.log(m[ok]),np.log(v[ok]),1)[0])
    top3=float(np.sort(g/g.sum())[::-1][:3].sum())
    return slope, top3
for mode,pred in [('extensive',1.0),('coherent',2.0),('fixed_amp',2.0)]:
    s,t3=run(mode=mode)
    print(f"{mode:10s}: measured variance ~ share^{s:.2f}  (predicted {pred:.0f})   top-3 share {t3:.2f}")
