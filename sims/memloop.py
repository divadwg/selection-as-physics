"""
Memory loop test. Parallel routes, fixed total flux, Ohm splitting.
Each route has: g (conductance = its rule) and c (a coupling: how its own throughput writes back into g).
Write-back: if throughput i crosses a gate theta, g += c * (i - theta).   c can be +, - or 0.
c is itself heritable and mutable (undirected), like g. Nothing says which c is good.
Question: do positive-c routes (memory loops: flow writes rule that raises flow) take over?
"""
import numpy as np
def run(seed=0, N=40, steps=60000, I=1.0, eps=0.05, delta=0.05, gmin=0.02, theta=None, copy_p=0.3, kc=0.5, cmut=0.05):
    rng=np.random.default_rng(seed)
    g=np.full(N,1.0)+0.01*rng.standard_normal(N)
    c=rng.uniform(-1,1,N)                    # random couplings, mean zero
    if theta is None: theta=I/N              # gate at the fair share
    hist=[]
    for t in range(steps):
        i=I*g/g.sum(); rate=eps*i*N
        # write-back through the gate: the flow writes the rule
        over=np.clip(i-theta,0,None)
        g=g+kc*c*over*N                       # scaled so a route at 2x fair share moves ~kc*c per step
        # undirected mutation of both g and c, where activity is
        fire=rng.random(N)<rate
        g=g+np.where(fire,delta*rng.choice([-1,1],N),0.0)
        c=c+np.where(fire,cmut*rng.choice([-1,1],N),0.0)
        # undirected copying of the whole rule (g and c) into a neighbour, where activity is
        cp=rng.random(N)<copy_p*rate
        if cp.any():
            src=np.where(cp)[0]; dst=(src+rng.choice([-1,1],src.size))%N; g[dst]=g[src]; c[dst]=c[src]
        g=np.maximum(g,gmin); c=np.clip(c,-2,2)
        if t%5000==0 or t==steps-1:
            i=I*g/g.sum()
            hist.append((t, float((i*c).sum()), float(c.mean()), float((c>0).mean()), float(g.mean())))
    return hist
if __name__=="__main__":
    H=[run(seed=s) for s in range(6)]
    print("t     flux-weighted c   mean c   frac c>0   mean g   (avg over 6 seeds)")
    for k in range(len(H[0])):
        row=np.mean([h[k] for h in H],axis=0)
        print(f"{int(row[0]):6d}   {row[1]:+.2f}          {row[2]:+.2f}    {row[3]:.2f}      {row[4]:.2f}")
