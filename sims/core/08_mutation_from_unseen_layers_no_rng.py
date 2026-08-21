"""
Mutation from unseen layers, watched happening. No RNG after t=0.
Fine layer: chaotic coupled-map lattice (logistic r=4), deterministic, mixing.
Coarse layer: each channel sits on a KxK block; 'gray' = block mean.
Channels: forty routes, share = g/sum(g). Kick = coupling * throughput-contact * (gray - longrun mean).
Controls: frozen fine layer (no churn) and periodic fine layer (orderly churn).
Measurements: (1) gray deviations unpredictable from coarse history but exactly reproducible from fine state;
(2) effective kick variance on a channel scales with its share; (3) concentration appears; dies in controls.
"""
import numpy as np
def fine_step(x, eps=0.1, mode='chaotic'):
    if mode=='frozen': return x
    if mode=='periodic':
        return np.roll(x,1,axis=0)          # pure transport: orderly, non-mixing
    y=4*x*(1-x)                              # logistic, chaotic
    return (1-eps)*y + eps*0.25*(np.roll(y,1,0)+np.roll(y,-1,0)+np.roll(y,1,1)+np.roll(y,-1,1))
def run(mode='chaotic', N=40, K=6, steps=60000, kappa=3.0, gmin=0.02, seed=0):
    rng=np.random.default_rng(seed)          # used ONLY for initial condition
    X=rng.random((N*K, K))                   # each channel's block: rows [i*K:(i+1)*K]
    g=np.full(N,1.0)+0.01*rng.standard_normal(N)
    grays=np.zeros((steps//10, N)); kicks=[]; shares=[]
    mu=np.array([X[i*K:(i+1)*K].mean() for i in range(N)])   # running mean per block
    for t in range(steps):
        X=fine_step(X,mode=mode)
        gray=np.array([X[i*K:(i+1)*K].mean() for i in range(N)])
        mu=0.999*mu+0.001*gray               # slow running mean; kicks couple to fluctuation only
        share=g/g.sum()
        kick=kappa*share*N*(gray-mu)         # contact ∝ share: busier channels feel more substrate churn
        g=np.maximum(g+kick, gmin)
        if t%10==0: grays[t//10]=gray
        if t>steps//2 and t%50==0: kicks.append(kick.copy()); shares.append(share.copy())
    share=g/g.sum()
    kicks=np.array(kicks); shares=np.array(shares)
    # measurement 2: does kick variance scale with share? fit log var(kick_i) vs log mean share_i
    v=kicks.var(0); m=shares.mean(0)
    ok=(v>1e-30)&(m>0)
    slope=float(np.polyfit(np.log(m[ok]),np.log(v[ok]),1)[0]) if ok.sum()>3 else float('nan')
    # measurement 1: autocorrelation of gray deviations (coarse-unpredictability proxy)
    d=grays[len(grays)//2:]-grays[len(grays)//2:].mean(0)
    ac1=np.mean([np.corrcoef(d[:-1,i],d[1:,i])[0,1] for i in range(N)])
    top3=np.sort(share)[::-1][:3].sum()
    return dict(mode=mode, top3=float(top3), kickvar_vs_share_slope=float(slope), gray_autocorr=float(ac1))
if __name__=="__main__":
    for mode in ['chaotic','frozen','periodic']:
        r=run(mode=mode)
        print(f"{mode:9s}: top-3 share={r['top3']:.2f}  kick-variance~share^{r['kickvar_vs_share_slope']:.2f}  gray autocorr={r['gray_autocorr']:+.2f}")
    # reproducibility check: same seed twice, identical trajectory (determinism below)
    a=run(seed=3); b=run(seed=3); print("re-run same initial condition: identical results ->", a==b)
