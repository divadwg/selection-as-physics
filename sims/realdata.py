"""
Occupancy law p(S) ∝ 1/D(S) applied to published fluctuation-scaling measurements.
For each system: state S (share of flow linear in S), event rate r(S), kick size sigma(S) => D = 0.5 r sigma^2 => q, predicted density exponent, compare observed.
Then: for firms, what steady drift/entry-exit closes the gap between predicted S^-1.5 and observed ~S^-2 ?
"""
import numpy as np
systems=[
 # name, beta (relative sigma ∝ S^-beta), r scaling exponent in S, observed density exponent, source
 ("Cities (Gibrat, Zipf)",      0.00, 0.0, 2.0, "Gabaix 1999; Ioannides & Overman 2003"),
 ("US firms 1974-1993",         0.20, 0.0, 2.0, "Stanley 1996 (beta 0.20±0.03); Axtell 2001 (Zipf)"),
 ("US firms 1993-2015",         0.26, 0.0, 2.0, "Sci Rep 2019 (beta 0.26±0.01)"),
 ("Country GDP",                0.15, 0.0, None, "Lee et al 1998"),
 ("Growing networks (degree)",  None, 1.0, 3.0, "Jeong-Neda-Barabasi 2003 attach exp≈1; BA density k^-3"),
]
print(f"{'system':28s} {'q':>5s} {'pred p exp':>10s} {'obs':>6s}  regime")
for name,beta,rexp,obs,src in systems:
    if beta is not None:
        # relative kick sigma/S ∝ S^-beta -> absolute sigma^2 ∝ S^(2-2beta); D ∝ S^(rexp + 2 - 2beta)
        q=rexp+2-2*beta
    else:
        # additive unit kicks (+1 link), rate ∝ degree^1 -> D ∝ S^1
        q=rexp
    regime='no concentration' if q<1 else ('marginal (log)' if abs(q-1)<1e-9 else 'concentration')
    print(f"{name:28s} {q:5.2f} {('S^-%.2f'%q):>10s} {(('S^-%.1f'%obs) if obs else '  n/a'):>6s}  {regime}   [{src}]")

print("\nFirms: zero-drift Itô with D ∝ S^1.5 predicts p ∝ S^-1.5; observed ~S^-2.")
print("Add steady net proportional drift mu (growth minus exit) : stationary p ∝ S^-q * exp(-(mu/const)...) -- for D∝S^2 (Gibrat) a reflecting floor + any negative net drift gives Zipf exponent 1+ (Gabaix).")
print("General: with D ∝ S^q and drift v(S)=a*S^(q-1) (same scaling), stationary p ∝ S^-(q - a/c) style: exponent shifts by a constant. Needed shift here: -0.5.")
# quick numeric check: simulate additive-in-S kicks with sigma ∝ S^(1-beta), reflecting floor, no drift; measure density exponent
def sim(beta, N=4000, T=4000, seed=0):
    rng=np.random.default_rng(seed); S=np.ones(N)
    for t in range(T):
        S=S+0.05*S**(1-beta)*rng.standard_normal(N)   # multiplicative-ish kick with variance ∝ S^(2-2beta)
        S=np.maximum(S,1.0)
    return S
for beta in [0.0,0.25]:
    S=sim(beta); h,edges=np.histogram(np.log(S),bins=25); c=0.5*(edges[1:]+edges[:-1]); m=h>5
    slope=np.polyfit(c[m],np.log(h[m]),1)[0]   # density in log S: p(logS) ∝ S^(1-qexp) => slope = 1-qexp
    print(f"sim beta={beta}: predicted q={2-2*beta:.2f}, fitted density exponent from sim = {1-slope:.2f}")
