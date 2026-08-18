import numpy as np
def run(coupled=True, N=40, steps=60000, I=1.0, eps=0.05, delta=0.05, gmin=0.02, seed=0, reps=8,
        split='ohm', kick='add', ceiling=None):
    rng=np.random.default_rng(seed); shares=[]
    for r in range(reps):
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        for t in range(steps):
            if split=='ohm': i=I*g/g.sum()
            elif split=='sqrt': w=np.sqrt(g); i=I*w/w.sum()      # a different linear-in-w law
            elif split=='softmax': w=np.exp(g); i=I*w/w.sum()
            rate = eps*i*N if coupled else eps*np.full(N,I/N)*N
            fire=rng.random(N)<rate
            if kick=='add': g=g+np.where(fire, delta*rng.choice([-1,1],N), 0.0)
            else: g=g*np.where(fire, np.exp(delta*rng.choice([-1,1],N)), 1.0)   # multiplicative
            g=np.maximum(g,gmin)
            if ceiling: g=np.minimum(g,ceiling)
        i=I*(g/g.sum() if split=='ohm' else (np.sqrt(g)/np.sqrt(g).sum() if split=='sqrt' else np.exp(g)/np.exp(g).sum()))
        shares.append(np.sort(i)[::-1][:3].sum())
    return np.mean(shares),np.std(shares)
tests=[('baseline',{}),
       ('flat noise',dict(coupled=False)),
       ('floor 0.2 (10x)',dict(gmin=0.2)),
       ('floor 1e-4 (~0)',dict(gmin=1e-4)),
       ('ceiling 2',dict(ceiling=2.0)),
       ('kick 0.01 (small)',dict(delta=0.01,steps=200000)),
       ('kick 0.2 (big)',dict(delta=0.2)),
       ('rate x0.2',dict(eps=0.01,steps=200000)),
       ('multiplicative kicks',dict(kick='mult')),
       ('sqrt splitting',dict(split='sqrt')),
       ('multiplicative + flat',dict(kick='mult',coupled=False)),
]
for lab,kw in tests:
    m,s=run(**kw); print(f"{lab:24s} top-3 share = {m:.2f} ± {s:.2f}", flush=True)
