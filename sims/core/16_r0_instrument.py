"""
R0 instrument. Forty channels; one is seeded with a heritable MARKER at t=0.
Copying ∝ share spreads the marker (birth). Re-templating erases it: a marked channel whose g
falls back within eps of g*=1 loses the marker (death by erasure). Measure per-progenitor copies
before death (R0 empirically), survival probability of the seed lineage, and compare with
branching theory P_surv ≈ 2(R0-1)/(R0 var-ish) near threshold. Sweep copy rate c0 and re-templating ktemp.
"""
import numpy as np
def trial(c0,ktemp,N=40,steps=20000,eps=0.05,delta=0.05,gmin=0.02,seed=0):
    rng=np.random.default_rng(seed)
    g=np.full(N,1.0)+0.01*rng.standard_normal(N)
    marked=np.zeros(N,bool); marked[0]=True; g[0]=1.4       # seed: one marked, slightly wide channel
    births=[]; alive0=True; copies0=0
    for t in range(steps):
        share=g/g.sum()
        fire=rng.random(N)<np.minimum(eps*N*share,1.0)
        g=g+np.where(fire,delta*rng.choice([-1,1],N),0.0)
        cop=rng.random(N)<np.minimum(c0*N*share,1.0)
        for i in np.where(cop)[0]:
            j=rng.integers(N)
            if j!=i:
                g[j]=g[i]
                if marked[i] and not marked[j]:
                    marked[j]=True
                    if i==0 and alive0: copies0+=1
                elif not marked[i]: marked[j]=False
        g=g-ktemp*(g-1.0); g=np.maximum(g,gmin)
        died=marked&(np.abs(g-1.0)<0.03)&(rng.random(N)<0.5)  # erasure death when re-templated home
        if died[0] and alive0: alive0=False
        marked&=~died
        if not marked.any(): return copies0, False, t
    return copies0, marked.any(), steps
print("c0, ktemp -> mean copies-per-progenitor (R0 est), lineage survival frac, theory 2(R0-1) clip[0,1]")
for c0,ktemp in [(0.002,2e-3),(0.005,2e-3),(0.01,2e-3),(0.005,5e-3),(0.005,1e-3)]:
    R=[]; S=[]
    for s in range(30):
        c,surv,t=trial(c0,ktemp,seed=s); R.append(c); S.append(surv)
    R0=np.mean(R); Ps=np.mean(S); th=max(0.0,min(1.0,2*(R0-1)))
    print(f"c0={c0} ktemp={ktemp}: R0≈{R0:.2f}  P_survive={Ps:.2f}  theory≈{th:.2f}",flush=True)
