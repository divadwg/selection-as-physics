"""
Copying as memory refresh: does replication rescue heredity from re-templating?
Setup: forty routes, kicks at rate ∝ share (as ever), re-templating pull toward g*=1 at rate ktemp,
PLUS copying: at rate ∝ share, a channel overwrites a random neighbour's g with its own.
Prediction (registered in README condition 1): the population climb survives re-templating levels
that kill sorting alone, and the survivable ktemp scales with copy rate c0.
Readout: mean g at end (climb) and top-3 share (concentration), vs ktemp, at three copy rates.
"""
import numpy as np
def run(ktemp, c0, N=40, steps=60000, eps=0.05, delta=0.05, gmin=0.02, seed=0, reps=3):
    mg=[]; t3=[]
    for r in range(reps):
        rng=np.random.default_rng(seed+r)
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        for t in range(steps):
            share=g/g.sum()
            fire=rng.random(N)<np.minimum(eps*N*share,1.0)
            g=g+np.where(fire,delta*rng.choice([-1,1],N),0.0)
            cop=rng.random(N)<np.minimum(c0*N*share,1.0)      # copier fires ∝ share
            for i in np.where(cop)[0]:
                j=rng.integers(N)
                g[j]=g[i]                                     # overwrite neighbour with own state
            g=g-ktemp*(g-1.0)                                 # re-templating pull
            g=np.maximum(g,gmin)
        share=g/g.sum(); mg.append(g.mean()); t3.append(np.sort(share)[::-1][:3].sum())
    return np.mean(mg),np.std(mg),np.mean(t3)
print("ktemp (dent-life) vs mean-g and top3, at copy rates 0, 0.005, 0.02:")
for ktemp in [0.0,1e-4,1e-3,1e-2]:
    row=f"ktemp={ktemp:g} (dl={'inf' if ktemp==0 else int(1/ktemp)}):"
    for c0 in [0.0,0.005,0.02]:
        m,sd,t3=run(ktemp,c0)
        row+=f"   c0={c0}: mean-g={m:.2f}±{sd:.2f} top3={t3:.2f}"
    print(row,flush=True)
