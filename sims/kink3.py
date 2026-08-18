import numpy as np
def run(copy_p, coupled=True, N=40, steps=60000, I=1.0, eps=0.05, delta=0.05, gmin=0.02, seed=0, reps=8):
    rng=np.random.default_rng(seed); out=[]
    for r in range(reps):
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        for t in range(steps):
            i=I*g/g.sum()
            rate = eps*i*N if coupled else eps*np.full(N,I/N)*N
            fire=rng.random(N)<rate
            g=g+np.where(fire, delta*rng.choice([-1,1],N), 0.0)
            # heredity: an active route copies its rule into a neighbour, at a rate scaled like everything else
            cp=rng.random(N)<copy_p*rate
            if cp.any():
                src=np.where(cp)[0]; dst=(src+rng.choice([-1,1],src.size))%N
                g[dst]=g[src]
            g=np.maximum(g,gmin)
        i=I*g/g.sum(); top=np.argmax(g)
        share3=np.sort(i)[::-1][:3].sum()
        kin=(np.abs(g-g[top])<0.05).mean()          # fraction of routes carrying (near) the winning rule
        ntypes=len(np.unique(np.round(g,2)))
        out.append((share3,kin,ntypes))
    o=np.array(out); return o.mean(0),o.std(0)
for lab,kw in [('no copying',dict(copy_p=0.0)),('copying, coupled noise',dict(copy_p=0.3)),('copying, flat noise',dict(copy_p=0.3,coupled=False))]:
    m,s=run(**kw); print(f"{lab:26s} top-3 flux share={m[0]:.2f}  routes carrying winner's rule={m[1]:.2f}  distinct rule types={m[2]:.0f}")
