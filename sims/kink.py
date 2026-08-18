import numpy as np
def run(coupled, N=40, steps=20000, I=1.0, eps=0.05, delta=0.05, gmin=0.02, seed=0, reps=20):
    rng=np.random.default_rng(seed); shares=[]; ginis=[]
    for r in range(reps):
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        for t in range(steps):
            i=I*g/g.sum()                          # Ohm: flux splits in proportion to conductance
            rate = eps*i*N if coupled else eps*np.full(N,I/N)*N   # events per path per step
            fire=rng.random(N)<rate                # misapplication events
            g=g+np.where(fire, delta*rng.choice([-1,1],N), 0.0)   # undirected kick
            g=np.maximum(g,gmin)
        i=I*g/g.sum(); s=np.sort(i)[::-1]
        shares.append(s[:3].sum()); 
        ginis.append(np.abs(np.subtract.outer(i,i)).mean()/(2*i.mean()))
    return np.mean(shares),np.std(shares),np.mean(ginis)
for label,c in [('noise rate ∝ flux',True),('noise rate flat',False)]:
    for steps in [2000,20000,100000]:
        m,s,gi=run(c,steps=steps,reps=10)
        print(f"{label:22s} steps={steps:6d}  top-3 paths' share of flux = {m:.2f}±{s:.2f}   gini={gi:.2f}")
