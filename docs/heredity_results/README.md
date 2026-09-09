# Retained heredity and threshold checks

These results support the [heredity audit](../heredity_audit.md). They describe
specified toy models, not empirical observations or a complete origin-of-life
construction. All random seeds and model parameters are in the manifests.

| File | Contents |
|---|---|
| `branching.csv`, `branching_trials.csv` | Backward-equation predictions and 18,000 exact-event trial outcomes at three observation times. |
| `thresholds.csv` | Critical copying coefficients and costs at 8, 16 and 32 grid intervals. |
| `threshold_checks.csv`, `threshold_trials.csv` | 12,000 outcomes at 0.8 and 1.2 times the predicted critical copying coefficient. |
| `restoration_reversal.csv` | Activity-dependent and constant-damage controls at 16, 32 and 64 intervals. |
| `transport.csv` | 120 transfer assays, each with 10,000 packets; same destination response for all stores. |
| `generations.csv` | Every generation of 180 population runs; parent–child correlation, population response and work accounting. |
| `founder_identity_check.txt` | Corrected historical script 16's five 30-seed summaries; finite-time survival only. |
| `manifest.json`, `threshold_manifest.json` | Settings, seeds and source hashes. |

All 18 lineage and 12 threshold predictions lie within marginal 99% Wilson
intervals formed from the simulation counts. Censored trials widen the bounds:
they count as dead for the lower endpoint and alive for the upper endpoint.
These are individual intervals, not a simultaneous confidence statement across
all runs. The largest distance between a predicted probability and the raw
censoring bracket is .0226 for the lineage checks and .0274 for the threshold
checks. The analytic one-state controls and timestep refinement provide separate
numerical checks. These comparisons do not certify continuum convergence.

## Candidate threshold reversal

Critical copying coefficient c in b=c*g; a lower value makes establishment
easier. The 64-interval calculation gives:

| Transit time | No restoration | Restoration 0.7 | Consequence of restoration |
|---|---:|---:|---|
| 0 | .1747 | .3517 | Raises the required copying coefficient |
| 20 | .4639 | .5571 | Raises it |
| 30 | .6855 | .6999 | Slightly raises it |
| 40 | .9329 | .8785 | Lowers it |
| 60 | 1.5880 | 1.3803 | Lowers it |

The sign change is present on all three refinement grids. Numbers still vary
with grid spacing; no precise continuum crossover location is claimed. With
state-independent transit damage, restoration raises the critical coefficient
at every tested transit time. This isolates the assumed activity–damage coupling
in this model; it does not establish that coupling in nature or claim novelty
for branching mathematics.

## Reproduce

From the repository root, using the validation NumPy environment:

```sh
python -m unittest discover -s tests -v
python -m sims.validation.run_heredity --output work/heredity-results
python -m sims.validation.run_thresholds --output work/heredity-results
python sims/core/16_r0_instrument.py
```

The output option keeps committed results intact. The threshold checks use a
fixed background for rare lineages, positive death rate .4, and explicit stochastic
births. A cap hit is censored, not established survival. No claim about long-run
finite-population takeover is made. The transport and reproduction assays assume
a carrier and a copying mechanism. Their shuffled-pair comparison is a statistical
null; it does not physically remove inherited information from the population.
