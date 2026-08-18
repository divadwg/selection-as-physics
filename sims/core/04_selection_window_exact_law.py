import numpy as np
# (1) Exact stationary law: p ∝ g^-q on [1,R]; flux density ∝ g^(m-q). Fraction of channels carrying the top half of flux.
def P_half(m,q,R):
    g=np.logspace(0,np.log10(R),200000); p=g**-q; J=g**m*p
    F=np.cumsum(J*np.gradient(g)); F/=F[-1]
    k=np.searchsorted(F,0.5)               # state above which half the flux sits
    P=np.cumsum(p*np.gradient(g)); P/=P[-1]
    return 1-P[k]
print("Exact stationary law: fraction of channels carrying the top half of flux, as range R grows")
print("      R:     1e2     1e4     1e6     1e8   -> limit")
for m,q in [(1,0.5),(1,1),(1,1.5),(1,2),(1,2.5),(1,3.5),(0.5,2),(2,3),(2,4)]:
    vals=[P_half(m,q,R) for R in (1e2,1e4,1e6,1e8)]
    inw='in ' if 1<=q<=m+1 else 'out'
    trend='→0' if vals[-1]<0.5*vals[0] else '→const'
    print(f"m={m} q={q} [{inw}]: "+"  ".join(f"{v:.4f}" for v in vals)+f"   {trend}")

# (2) Large-N Itô diffusion, no cap: dg = sqrt(2 D(g)) dW, D=g^q, reflect at [1,R]. Check occupancy ∝ 1/D and P_half.
rng=np.random.default_rng(0)
def sde(m,q,R=1e3,N=200000,T=20000):
    g=np.exp(rng.uniform(0,np.log(R),N)); dt=1e-3
    for t in range(T):
        g=g+np.sqrt(2*g**q*dt)*rng.standard_normal(N)
        g=np.where(g<1,2-g,g); g=np.where(g>R,2*R-g,g)   # reflect
        g=np.clip(g,1,R)
    return g
print("\nLarge-N Itô SDE (no cap), R=1e3: fitted occupancy exponent vs -q, and P_half vs exact")
for m,q in [(1,0.5),(1,1),(1,2),(1,3.5),(2,4)]:
    g=sde(m,q); h,e=np.histogram(np.log(g),bins=30,range=(0,np.log(1e3))); c=0.5*(e[1:]+e[:-1]); mask=h>50
    slope=np.polyfit(c[mask],np.log(h[mask]),1)[0]; qfit=1-slope        # p(g)∝g^-q  => p(log g)∝g^(1-q)
    J=g**m; order=np.argsort(-J); Jc=np.cumsum(J[order])/J.sum(); nhalf=np.searchsorted(Jc,0.5)+1
    print(f"m={m} q={q}: fitted q={qfit:.2f}   P_half sim={nhalf/len(g):.4f}   exact={P_half(m,q,1e3):.4f}")
