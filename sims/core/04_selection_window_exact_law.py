"""Exact power-law quantiles; optional historical SDE diagnostic.

For the coupled conserved-flow check, run:
    python -m sims.validation.run_validation
"""
import argparse
import numpy as np


def P_half(m, q, R):
    """Integrate p proportional to g^-q; find the top half of weighted flow."""
    g = np.logspace(0, np.log10(R), 200000)
    p = g**-q
    flux = g**m * p
    cumulative_flow = np.cumsum(flux * np.gradient(g))
    cumulative_flow /= cumulative_flow[-1]
    k = np.searchsorted(cumulative_flow, 0.5)
    population = np.cumsum(p * np.gradient(g))
    population /= population[-1]
    return 1 - population[k]


def sde(m, q, R=1e3, N=200000, T=20000, rng=None):
    """Historical independent-walker experiment; not a validated integrator.

    The log-uniform start is already stationary for q=1. The run length is
    insufficient for some other exponents, and large jumps are clipped after
    a single reflection. Retained for reproducing the original diagnostic.
    Parameter m affects the observable, not these independent dynamics.
    """
    if rng is None:
        rng = np.random.default_rng(0)
    g = np.exp(rng.uniform(0, np.log(R), N))
    dt = 1e-3
    for _ in range(T):
        g = g + np.sqrt(2*g**q*dt) * rng.standard_normal(N)
        g = np.where(g < 1, 2-g, g)
        g = np.where(g > R, 2*R-g, g)
        g = np.clip(g, 1, R)
    return g


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--legacy-sde", action="store_true",
                        help="Run the slow, unvalidated historical independent-walker diagnostic")
    args = parser.parse_args()
    print("Exact stationary law: fraction carrying the top half of flux as range R grows")
    print("      R:     1e2     1e4     1e6     1e8   -> limit")
    for m, q in [(1,.5), (1,1), (1,1.5), (1,2), (1,2.5), (1,3.5), (.5,2), (2,3), (2,4)]:
        values = [P_half(m, q, R) for R in (1e2, 1e4, 1e6, 1e8)]
        window = 'in ' if 1 <= q <= m+1 else 'out'
        trend = '→0' if values[-1] < .5*values[0] else '→const'
        print(f"m={m} q={q} [{window}]: " + "  ".join(f"{v:.4f}" for v in values) + f"   {trend}")
    if not args.legacy_sde:
        return
    print("\nLEGACY DIAGNOSTIC: starts at the q=1 stationary density; no burn-in or")
    print("step-size convergence established. Other exponents may not equilibrate.")
    print("This does not validate the coupled conserved-flow model.")
    rng = np.random.default_rng(0)
    for m, q in [(1,.5), (1,1), (1,2), (1,3.5), (2,4)]:
        g = sde(m, q, rng=rng)
        h, edges = np.histogram(np.log(g), bins=30, range=(0,np.log(1e3)))
        centres = (edges[1:] + edges[:-1])/2
        mask = h > 50
        fitted_q = 1 - np.polyfit(centres[mask], np.log(h[mask]), 1)[0]
        flow = np.sort(g**m)[::-1]
        count = np.searchsorted(np.cumsum(flow)/flow.sum(), .5) + 1
        print(f"m={m} q={q}: fitted q={fitted_q:.2f}   P_half sim={count/len(g):.4f}   exact={P_half(m,q,1e3):.4f}")


if __name__ == "__main__":
    main()
