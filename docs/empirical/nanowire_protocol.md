# Nanowire data: scope and analysis plan

Written before fitting noise exponents to the downloaded measurements. This is a
versioned analysis plan, not an externally registered study.

## Question this dataset can address

Do increments of the measured whole-network conductance show state-dependent
variance within one fixed-voltage recording, after accounting for its conditional
mean change? Is a local diffusion description adequate at the available sampling
interval? These are exploratory tests of an aggregate electrical observable.

Source: Milano et al., Nature Communications 16, 3509 (2025),
https://doi.org/10.1038/s41467-025-58741-2 . Data:
https://doi.org/10.5281/zenodo.15050217 .

## Questions this dataset cannot settle

The paper measures effective conductance between two electrodes, not the separate
conductances and currents of competing paths. Voltage is controlled; total current
is not fixed. Consequently the data cannot validate or invalidate the conserved-
flow concentration window, its upper boundary, or the finite-N correction. Making
currents sum to one numerically would not repair these missing experimental
conditions. A result outside the window for the aggregate coordinate is not a
counterexample to a claim about individual channels.

## Data audit before estimation

- Identify experimental and simulated files using figure captions. Never treat
  model-generated curves as independent experimental evidence.
- Preserve source files, checksums, units and original column order. Verify time
  order, missing values, repeated samples, sampling intervals and state range.
- Use unfiltered conductance measurements for the primary analysis. Authors'
  threshold-selected noise and jump files are diagnostics, not an unbiased sample
  of the original process.
- The main fixed-voltage candidate is the experimental 3.6 V recording in Figure
  5a. Use 18,500 through 33,500 seconds: the Methods specify a 15,000-second
  observation period after 18,500 seconds. The file extends into a later low-bias
  relaxation, which must not be included in the fixed-voltage analysis. Preserve
  the earlier 0-18,500-second transient as a separate analysis. Audit Figure 2b inset
  for additional within-voltage stationary segments.
- Do not concatenate different voltage conditions to estimate a state exponent.
  Changes in voltage alter the dynamics as well as the mean conductance.

## Exploratory analysis

1. Report the time and conductance range actually covered, particularly within
   each stationary segment. A narrow range limits identification of an exponent.
2. Calculate non-overlapping increments at several sampling lags. Use conditional
   mean changes to account for drift, and central second moments for a finite-lag
   variance diagnostic. Do not assume its small-lag diffusion limit exists.
3. Compare a constant-variance conditional-mean model with variance proportional
   to conductance raised to a fitted power. Split records chronologically into
   training and held-out portions; a predictive improvement is evidence only for
   the local statistical model, not for the concentration theorem.
4. Retain all increments as the primary result. Report sensitivity to extreme
   increments separately; excluding large changes changes the question and cannot
   establish the diffusion coefficient of the full process.
5. Check lag dependence, residual correlations and changes between time blocks.
   Use block resampling where estimating uncertainty; do not treat overlapping
   increments as independent measurements.
6. Test the estimator on synthetic constant-noise and state-dependent-noise
   processes, including a narrow-range example. Inadequate recovery prevents a
   claim about the corresponding observed exponent.

The conductance is used in its physical units without subtracting a fitted floor.
Multiplying the units does not change a power-law exponent; shifting the origin
can. The paper's affine normalized memory coordinate is a different variable.
An exponent over the observed finite range is not an asymptotic tail exponent.

## Interpretation rules

- Inapplicable: the measurement does not correspond to the quantity in the claim.
- Inconclusive: the quantity is relevant but range, sampling, uncertainty, drift,
  jumps or instability prevent discrimination.
- Local support or local tension: a reproducible result supports or challenges a
  stated statistical assumption for this observable and regime only.
- A full physical test requires simultaneous path-level state and flow records,
  measured total input, independent estimation of drift and noise, and a regime
  where the model assumptions can be checked. Testing both window boundaries also
  requires observations spanning those regimes.

These rules apply symmetrically. Missing information must not become a rejection,
while an attractive-looking exponent must not become confirmation.
