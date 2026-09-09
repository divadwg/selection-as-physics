"""Historical finite-population lineage instrument, with founder identity repaired.

Reports survival to a finite horizon, not eventual establishment. Counts actual
births by the original individual; replacement ends that individual's life.
No scalar survival formula is fitted. The independently checked branching model
is in sims/validation/heredity.py; its fixed background differs from this model.
"""
import numpy as np
def trial(c0,ktemp,N=40,steps=20000,eps=0.05,delta=0.05,gmin=0.02,seed=0):
    rng=np.random.default_rng(seed)
    g=np.full(N,1.0)+0.01*rng.standard_normal(N)
    marked=np.zeros(N,bool); marked[0]=True; g[0]=1.4       # seed: one marked, slightly wide channel
    identity=np.arange(N); next_identity=N; copies0=0
    for t in range(steps):
        share=g/g.sum()
        fire=rng.random(N)<np.minimum(eps*N*share,1.0)
        g=g+np.where(fire,delta*rng.choice([-1,1],N),0.0)
        cop=rng.random(N)<np.minimum(c0*N*share,1.0)
        for i in np.where(cop)[0]:
            j=rng.integers(N)
            if j!=i:
                founder_birth = identity[i]==0
                identity[j]=next_identity; next_identity+=1
                g[j]=g[i]
                if founder_birth and marked[i]: copies0+=1
                if marked[i] and not marked[j]:
                    marked[j]=True
                elif not marked[i]: marked[j]=False
        g=g-ktemp*(g-1.0); g=np.maximum(g,gmin)
        died=marked&(np.abs(g-1.0)<0.03)&(rng.random(N)<0.5)  # erasure death when re-templated home
        identity[died]=-1
        marked&=~died
        if not marked.any(): return copies0, False, t
    return copies0, marked.any(), steps
if __name__ == "__main__":
    print("copy rate, restoration: original-founder births and fraction alive at 20,000 steps")
    for c0,ktemp in [(0.002,2e-3),(0.005,2e-3),(0.01,2e-3),(0.005,5e-3),(0.005,1e-3)]:
        results=[trial(c0,ktemp,seed=s) for s in range(30)]
        print(f"c0={c0} ktemp={ktemp}: founder births={np.mean([r[0] for r in results]):.2f} "
              f"alive at horizon={np.mean([r[1] for r in results]):.2f}",flush=True)
