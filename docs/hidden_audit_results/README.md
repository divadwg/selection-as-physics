# Calibrating the hidden layer before predicting sharing

The deterministic pilot now has a separate calibration and prediction check.
Its measured second-moment scaling closely recovers the supplied coupling, and
predicts independent finite-range runs reasonably well. Residual drift remains
unresolved. These checks strengthen the numerical connection; they do not derive
the coupling from contact counts or validate a physical system.

## What is measured

The unchanged torus map and reflected update are defined in the
[original pilot](../hidden_map_results/README.md). Here N=8 and m=1. Calibration
uses 256 independently initialised ensembles, seed 310, g initially 2, a burn-in
of 4 and another 4 time units of observations. Every 32nd update contributes an
increment, provided its **pre-update** state is far enough from both boundaries
that no possible kick could touch either. Thus inclusion does not select by the
sign or size of the realised kick. The excluded boundary neighbourhood shrinks
with the step; these are interior diagnostics, not a test of boundary dynamics.

Fit the raw second moment to

```text
E[(delta g_i)^2 | g_i,S] / (2 dt) = c N g_i^q / S^gamma.
```

Both q and gamma are estimated; gamma is not fixed to its supplied value 1.
Multiplicative moment equations estimate the coefficients. Sandwich standard
errors cluster by independent ensemble, retaining dependence among its routes
and sampled times. Raw second moments approximate diffusion variance only when
drift and memory corrections are negligible. Power-law adequacy beyond these
moment equations is not established by coefficient recovery alone.

At dt=1/2048:

| Supplied q | Measured q ± SE | Measured gamma ± SE |
|---:|---:|---:|
| .5 | .5023 ± .0036 | 1.0052 ± .0100 |
| 1 | 1.0010 ± .0035 | 1.0025 ± .0098 |
| 1.5 | 1.5026 ± .0036 | 1.0067 ± .0095 |
| 2.5 | 2.5034 ± .0038 | 1.0103 ± .0100 |

`fits.csv` also retains dt=1/512 and the fitted amplitude. These standard errors
are asymptotic, individual uncertainties, not simultaneous confidence bounds.
Recovering a supplied coupling checks the coarse approximation; it is not a
new discovery that the physical coupling must have this form.

## Independent predictions

Under the candidate **zero-drift** diffusion, the fitted law has zero-current
stationary density proportional to `S^gamma product_i g_i^(-q)`: multiplying this
by any D_i removes its dependence on g_i. Reference samples from the exact gamma=1
mixture are reweighted by `S^(gamma-1)`. No concentration observations enter the fit.
The amplitude c changes the clock, not this density.

Calibration covers [1,3]. Independent runs use seeds 910–912, with all channels
starting at 1, 2 or 3; 256 ensembles per start. The table gives the largest final
CDF discrepancy across those starts, on 101 thresholds at time 32.

| Supplied q | Channel-count CDF error | Pooled-flow CDF error |
|---:|---:|---:|
| .5 | .02073 | .02033 |
| 1 | .02055 | .02058 |
| 1.5 | .01973 | .01491 |
| 2.5 | .02333 | .01911 |

The reference has 100,000 samples. A second reference seed checks integration
variability; discrepancies are retained in `heldout.csv`. Resampling whole
held-out ensembles 2,000 times gives approximate 95% radii for the maximum
centred CDF sampling error: .0273–.0308 for channel counts and .0294–.0328 for
pooled flow across the retained times and starts. These are **sampling-only**
radii. They omit fitted-parameter uncertainty, reference integration error and
systematic approximation errors, and are not a formal model-acceptance test.

A further prediction keeps the [1,3] calibration and widens the range to [1,6],
using q=.5 and 2.5, new seeds 1010–1011 and starts at either endpoint. At time 64,
the largest errors are .02534 for channel counts and .03145 for pooled flow.
The corresponding sampling radii are .0264–.0288 and .0314–.0344. Times 32 and 64
are retained. These runs show no clear discrepancy beyond this sampling scale;
they do not prove relaxation or the large-range limiting window. In particular,
unequal sharing at q=2.5 in a finite range does not contradict the upper bound.

## Drift and correlation caution

At dt=1/512 the highest-state drift bin leans negative for every exponent.
Refinement reduces this concern but does not remove it conclusively. For q=2.5
and pre-states in [2.5,3], the estimates are:

| dt | Ensembles | Drift ± cluster SE |
|---:|---:|---:|
| 1/512 | 256 | −2.865 ± 1.067 |
| 1/2048 | 256 | −2.160 ± .949 |
| 1/8192 | 512 across two seeds | −1.367 ± .582 |

The finest check was chosen after inspecting the earlier results. It combines
seeds 310 and 311; seed 310 is reused across step sizes, so rows are not independent.
The remaining pooled estimate is about 2.35 standard errors below zero. With
several bins examined and a changing boundary exclusion, this is a reason to
retain the drift question, not to assert a nonzero limiting drift or dismiss it.
The diagnostics average within state bins, not within the full configuration.

Driver products at lags 1, 2, 4 and 8, and between adjacent routes, are small
relative to their ensemble sampling errors. They are unconditional products of
the normalised hidden driver, not a complete check of conditional coarse
cross-covariances or higher-order memory. Identical values across q reflect the
same hidden trajectories, not independent replications of this check.

A unit control verifies exact equality of updates when activity is multiplied
by four and dt divided by four. This checks the specified clock-rescaling
identity. It is not evidence that varying activity in a physical device leaves
its other properties unchanged.

## Consequence for Paper 1 and the physical assay

The prediction has survived a more informative numerical check than fitting a
stationary histogram. The next mathematical gap is to bound the effect of the
remaining drift and memory, or establish their limiting disappearance. Wider
ranges and population sizes are still needed for the asymptotic concentration
classification. None of these finite checks invalidates that conditional theorem.

The [memristor protocol](../memristor_q_analysis.md) should use the same separation:
calibrate state-changing increments first, predict separate observations second.
A mismatch in calibration tests applicability; a well-resolved failure of the
conditional prediction tests the model. Insufficient relaxation or measurement
resolution leaves the comparison undecided. No physical measurements were added.
The paper's theoretical claim is unchanged; these details belong in the repository.

## Reproduce and inspect

From the repository root:

```sh
python -m sims.validation.run_hidden_audit
python -m sims.validation.run_hidden_followup
python -m sims.validation.run_hidden_drift_refinement
python -m unittest discover -s tests
```

The runners overwrite retained results. Calibration NPZ files contain ensemble
identifier, pre-state, total state and increment, fitted coefficients, covariance
and per-ensemble driver products. Prediction files retain the reference CDFs;
held-out files retain full coarse snapshots. Drift refinement retains per-ensemble
counts and sums in each bin, sufficient to reconstruct its estimates and standard
errors without keeping millions of additional increments. CSV files contain the
reported summaries. Manifests record settings and source hashes. The full suite
has 32 passing tests, including coefficient recovery, a one-route analytic
stationary reference and the activity-clock identity.
