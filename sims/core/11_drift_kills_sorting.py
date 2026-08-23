"""
Does drift kill sorting? The unification's untested prediction.
Forty routes, share = g/sum(g), kicks at rate ∝ share (the classic setup),
PLUS restoring drift: g -> g - kdrift*(g - 1) each step (environment re-templates toward g*=1).
Dent-life ≈ 1/kdrift steps. Predict: concentration dies as kdrift rises past ~1/T_obs.
"""
import numpy as np
def run(kdrift, N=40, steps=60000, eps=0.05, delta=0.05, gmin=0.02, seed=0, reps=3):
    out=[]
    for r in range(reps):
        rng=np.random.default_rng(seed+r)
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        for t in range(steps):
            share=g/g.sum()
            fire=rng.random(N)<np.minimum(eps*N*share,1.0)
            g=g+np.where(fire,delta*rng.choice([-1,1],N),0.0)
            g=g-kdrift*(g-1.0)                      # environment re-templates
            g=np.maximum(g,gmin)
        share=g/g.sum(); out.append(np.sort(share)[::-1][:3].sum())
    return np.mean(out),np.std(out)
print("kdrift, dent-life(steps), top-3 share (uniform 0.075):")
for kd in [0.0, 1e-5, 1e-4, 1e-3, 1e-2]:
    mu,sd=run(kd); dl='inf' if kd==0 else f"{1/kd:.0f}"
    print(f"kdrift={kd:g}: dent-life={dl:>6s}  top3={mu:.2f}±{sd:.2f}",flush=True)
