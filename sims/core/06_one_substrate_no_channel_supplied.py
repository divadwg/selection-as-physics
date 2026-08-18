"""
Rule and flow as one substrate, two speeds. No separate 'rule' variable.
Each route holds material s (slow). Flux through a route is what physics says: less where more material, i ∝ 1/(1+s).
Material responds to flux according to a property of the material itself, a: ds = a * flux.
   a<0: flow removes this material (erodible).  a>0: flow deposits more of it (armouring).  a starts random, mean 0.
Material moves: where activity is, material (with its property a) spreads into neighbouring routes.
Where activity is, a mutates without bias.  Nothing says which a is good.
"""
import numpy as np
def run(seed=0,N=40,steps=40000,I=1.0,eps=0.05,k=0.02,mut=0.05,copy_p=0.3,smin=0.0,smax=50.0):
    rng=np.random.default_rng(seed)
    s=np.full(N,5.0)+0.05*rng.standard_normal(N)
    a=rng.uniform(-1,1,N)
    hist=[]
    for t in range(steps):
        w=1/(1+s); i=I*w/w.sum(); rate=eps*i*N
        s=s+k*a*i*N                                  # material responds to the flow through it, per its own nature
        fire=rng.random(N)<rate
        a=a+np.where(fire,mut*rng.choice([-1,1],N),0.0)
        cp=rng.random(N)<copy_p*rate                 # material spreads where activity is, carrying its property
        if cp.any():
            src=np.where(cp)[0]; dst=(src+rng.choice([-1,1],src.size))%N; a[dst]=a[src]; s[dst]=0.5*(s[dst]+s[src])
        s=np.clip(s,smin,smax); a=np.clip(a,-2,2)
        if t%5000==0 or t==steps-1:
            w=1/(1+s); i=I*w/w.sum()
            hist.append((t,float((i*a).sum()),float((a<0).mean()),float(s.mean()),float(np.sort(i)[::-1][:3].sum())))
    return hist
if __name__=="__main__":
    for lab,kw in [('full',{}),('no spreading',dict(copy_p=0.0)),('material inert (k=0)',dict(k=0.0))]:
        H=[run(seed=s,**kw) for s in range(5)]
        print(lab); print("   t    flux-weighted a   frac erodible(a<0)   mean material   top-3 flux share")
        for j in range(len(H[0])):
            r=np.mean([h[j] for h in H],axis=0); print(f"{int(r[0]):6d}   {r[1]:+.2f}             {r[2]:.2f}               {r[3]:.2f}           {r[4]:.2f}")
