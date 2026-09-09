"""
Historical exploratory model. Current controls and qualifications are in
docs/heredity_audit.md. These assumptions do not establish universal gating
necessity or indefinite transmission; matched replacements are in
sims/validation/heredity.py.

Prediction (D4): transit survival vs distance is near-flat for GATED parcels, exponential-decaying for UNGATED.
Clean redesign of the confounded control: NO types anywhere; inheritance only via the carried value.
Parcel = a value v carried for d steps through churn before landing.
Gated: v is which-side-of-barrier (binary); flips only if accumulated churn crosses ΔE (Kramers-like).
Ungated: v is continuous; relaxes toward ambient (1.0) at rate λ and diffuses with churn each transit step.
Measure: correlation between emitted value and landed value, vs distance d.
"""
import numpy as np
rng=np.random.default_rng(0)
def transit_gated(v,d,dE=1.0,sigma=0.35):
    x=0.0
    for _ in range(d):
        x+=sigma*rng.standard_normal()
        if abs(x)>dE: v=1-v; x=0.0
    return v
def transit_ungated(v,d,lam=0.08,sigma=0.12):
    for _ in range(d):
        v=v-lam*(v-1.0)+sigma*rng.standard_normal()
    return v
print("distance: gated fidelity (P[value preserved]) | ungated corr(emitted, landed)")
for d in [2,5,10,20,40,80]:
    # gated: binary values
    keep=0; n=2000
    for _ in range(n):
        v0=rng.integers(2); v1=transit_gated(v0,d)
        keep+= (v1==v0)
    # ungated: continuous values drawn around 1 with spread
    v0s=1.0+0.8*rng.standard_normal(800)
    v1s=np.array([transit_ungated(v,d) for v in v0s])
    c=np.corrcoef(v0s,v1s)[0,1]
    print(f"d={d:3d}: gated {keep/n:.2f} | ungated {c:+.2f}",flush=True)
