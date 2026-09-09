"""
Historical exploratory model. Current controls and qualifications are in
docs/heredity_audit.md. These assumptions do not establish universal gating
necessity or indefinite transmission; matched replacements are in
sims/validation/heredity.py.

Rung 3: portability. Does a detached, gated parcel of state shape flow where its parent never touched?
World: 1D chain of sites along a flow direction. Each site has a gated material type: 0 = self-silting, 1 = self-clearing
(type is the configuration-addressed rule: local erodibility response; read by whatever flow touches it, catalysis-style).
Flow: fixed total enters upstream, each site passes flow ∝ its conductance g; g dynamics: kicks ∝ local flow, plus
write-back with sign set by TYPE (self-clearing: flow widens; self-silting: flow narrows). Re-templating pull on g.
Transport: with prob ∝ local flow, a site sheds a PARCEL carrying its type token downstream a random distance
(gated: token is discrete, unchanged in transit), which overwrites the landing site's type.
Controls: (a) ungated transport: parcel carries a CONTINUOUS copy of parent g that blurs (decays toward 1) in transit
and adds to landing g, no type; (b) shuffled tokens (type randomised at landing): breaks parent-offspring link.
Measurement: correlation between a landing site's post-development flow structure and its PARENT's type,
at distances the parent's own flow never reached, vs the shuffled null.
"""
import numpy as np
def run(mode='gated', L=200, steps=40000, eps=0.08, delta=0.06, ktemp=2e-4, wb=0.004,
        shed=0.02, gmin=0.05, seed=0):
    rng=np.random.default_rng(seed)
    g=np.ones(L)+0.01*rng.standard_normal(L)
    typ=(rng.random(L)<0.5).astype(int)          # half self-clearing, half self-silting
    parent=np.full(L,-1)                          # who seeded this site's type (site index), -1 = original
    events=[]                                     # (parent_site, child_site, t)
    for t in range(steps):
        flow=g/g.sum()
        fire=rng.random(L)<np.minimum(eps*L*flow,1.0)
        g=g+np.where(fire,delta*rng.choice([-1,1],L),0.0)
        sgn=np.where(typ==1,+1.0,-1.0)
        g=g+wb*sgn*flow*L                         # type-addressed write-back: the READ
        g=g-ktemp*(g-1.0)
        g=np.maximum(g,gmin)
        # shedding: busy sites emit a parcel downstream
        emit=rng.random(L)<np.minimum(shed*L*flow,1.0)
        for i in np.where(emit)[0]:
            d=rng.integers(10,60)                 # lands well beyond parent's neighbourhood
            j=i+d
            if j>=L: continue
            if mode=='gated':
                events.append((typ[i],j,t)); typ[j]=typ[i]; parent[j]=i
            elif mode=='ungated':
                val=1.0+(min(g[i],3.0)-1.0)*np.exp(-d/15.0)   # blurred, capped continuous copy
                g[j]=np.clip(g[j]+0.3*(val-1.0),gmin,5.0); events.append((1.0 if g[i]>1.0 else 0.0,j,t))
            elif mode=='shuffled':
                events.append((typ[i],j,t)); typ[j]=rng.integers(2); parent[j]=i
    # measurement: for events in first half (time to develop), does child's final g reflect parent's type at emission?
    pairs=[]
    for (ptype,j,t) in events:
        if t<steps//2:
            pairs.append((float(ptype), g[j]))                # parent's type AT EMISSION
    if len(pairs)<20: return float('nan'),len(pairs)
    P=np.array(pairs)
    hi=P[P[:,0]==1][:,1]; lo=P[P[:,0]==0][:,1]
    if len(hi)<5 or len(lo)<5: return float('nan'),len(pairs)
    # effect size: mean child g under self-clearing parent minus under self-silting parent
    return float(hi.mean()-lo.mean()), len(pairs)
for mode in ['gated','ungated','shuffled']:
    effs=[]
    for seed in range(4):
        e,n=run(mode=mode,seed=seed)
        if e==e: effs.append(e)
    print(f"{mode:9s}: child-site final g, (self-clearing parent) - (self-silting parent) = {np.mean(effs):+.3f} ± {np.std(effs):.3f}",flush=True)
# takeover check in gated mode: does one type spread?
import numpy as np
fr=[]
for seed in range(4):
    rng=np.random.default_rng(seed)
    # rerun gated capturing final type fraction
    L=200; steps=40000
    g=np.ones(L)+0.01*rng.standard_normal(L); typ=(rng.random(L)<0.5).astype(int)
    for t in range(steps):
        flow=g/g.sum()
        fire=rng.random(L)<np.minimum(0.08*L*flow,1.0)
        g=g+np.where(fire,0.06*rng.choice([-1,1],L),0.0)
        g=g+0.004*np.where(typ==1,1.0,-1.0)*flow*L
        g=g-2e-4*(g-1.0); g=np.maximum(g,0.05)
        emit=rng.random(L)<np.minimum(0.02*L*flow,1.0)
        for i in np.where(emit)[0]:
            j=i+rng.integers(10,60)
            if j<L: typ[j]=typ[i]
    fr.append(typ.mean())
print(f"gated takeover: final fraction self-clearing = {np.mean(fr):.2f} ± {np.std(fr):.2f} (started 0.50)")
