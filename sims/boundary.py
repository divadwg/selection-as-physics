import numpy as np
def run(m, N=40, steps=200000, I=1.0, eps=0.05, delta=0.05, gmin=0.02, seed=0, reps=6, checkpoints=(2000,20000,200000)):
    rng=np.random.default_rng(seed); out={c:[] for c in checkpoints}
    for r in range(reps):
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        for t in range(1,steps+1):
            w=g**m; i=I*w/w.sum(); rate=eps*i*N
            fire=rng.random(N)<rate
            g=np.maximum(g+np.where(fire,delta*rng.choice([-1,1],N),0.0),gmin)
            if t in out:
                w=g**m; i=I*w/w.sum(); out[t].append(np.sort(i)[::-1][:3].sum())
    return {c:(np.mean(v),np.std(v)) for c,v in out.items()}
print("share law i ∝ g^m ; top-3 share of flux at 2k / 20k / 200k steps (uniform = 0.075)")
for m in [0.5,0.75,1.0,1.5,2.0]:
    r=run(m); print(f"m={m:4.2f}: "+"  ".join(f"{r[c][0]:.2f}±{r[c][1]:.2f}" for c in (2000,20000,200000)))
