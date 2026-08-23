"""
Copying DERIVED, not imposed (reviewer rec 2). Each channel accumulates copy-resource at rate eta*J_i
(throughput supplies work); when A_i >= E_copy it reproduces: a random channel is overwritten by
daughter with g = parent g + eps (eps from kicks' own scale: hidden-layer variation), A resets by cost.
No P(copy) ∝ J anywhere. Measure: (a) emergent per-channel copy rate b vs mean J: predict linear,
slope eta/E_copy; (b) population mean g climbs (Darwinian selection with derived copying);
(c) control E_copy = inf: no copying, no climb.
"""
import numpy as np
def run(E_copy, eta=1.0, N=40, steps=60000, eps0=0.05, delta=0.05, gmin=0.02, seed=0, reps=3):
    MG=[]; SLOPE=[]
    for r in range(reps):
        rng=np.random.default_rng(seed+r)
        g=np.full(N,1.0)+0.01*rng.standard_normal(N)
        A=np.zeros(N); births=np.zeros(N); Jsum=np.zeros(N)
        for t in range(steps):
            share=g/g.sum()
            fire=rng.random(N)<np.minimum(eps0*N*share,1.0)
            g=g+np.where(fire,delta*rng.choice([-1,1],N),0.0)
            g=np.maximum(g,gmin)
            A+=eta*share            # throughput funds the accumulator
            Jsum+=share
            if np.isfinite(E_copy):
                ready=np.where(A>=E_copy)[0]
                for i in ready:
                    j=rng.integers(N)
                    if j!=i:
                        g[j]=g[i]+delta*rng.choice([-1,1])   # inherited state + hidden-layer variation
                        A[j]=0.0
                    A[i]-=E_copy; births[i]+=1
        MG.append(g.mean())
        b=births/steps; Jm=Jsum/steps
        ok=(b>0)
        if ok.sum()>5: SLOPE.append(np.polyfit(Jm[ok],b[ok],1)[0]*1.0)
    return np.mean(MG),np.std(MG),(np.mean(SLOPE) if SLOPE else float('nan'))
for E in [200.0, 500.0, float('inf')]:
    m,sd,sl=run(E)
    pred='' if not np.isfinite(E) else f"  (predicted slope eta/E = {1.0/E:.4f})"
    print(f"E_copy={E}: mean-g={m:.2f}±{sd:.2f}  emergent b(J) slope={sl:.4f}{pred}",flush=True)
