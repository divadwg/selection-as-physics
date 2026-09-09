# Thought-experiment reruns

These are default runs of three existing scripts, retained on 9 September 2026
to support the paper's discussion of the proposed route toward selection.
They are separate from the exact bounded stationary validation suite.
[Source hashes and environment](provenance.txt).

## Deterministic lattice

[Output](deterministic_lattice.txt),
[source](../../sims/core/08_mutation_from_unseen_layers_no_rng.py).

| Fine dynamics | Final top-three flow share | Variance versus mean-share slope | Sampled block-mean lag-one correlation |
|---|---:|---:|---:|
| Chaotic | 0.62 | 1.99 | 0.01 |
| Frozen | 0.08 | undefined | undefined |
| Periodic | 0.95 | 2.01 | -0.16 |

The random generator initializes the state. There are no random draws after
initialization. Repeating the same initial condition gives identical reported
statistics. The finite lattice and its coarse coupling thus demonstrate
concentration under deterministic evolution, without ongoing stochastic input.

The periodic control also concentrates. This corrects the earlier claim that
both nonchaotic controls eliminate concentration. The example does not establish
that chaos is necessary. A small sampled autocorrelation is not a proof of
unpredictability, white noise, a Markov property or a diffusion limit. The frozen
case has zero fluctuation variance, so its slope and correlation are undefined;
NumPy emits an invalid-division warning when the original code computes them.

Default parameters: 40 routes, 6×6 cells per route, 60,000 steps, coupling 3,
state floor 0.02, seed 0. The duplicate check uses seed 3. The source records
block means every ten steps, so the reported lag refers to that sampling interval.

## Equal coarse-route start

[Results](equal_route_start.csv), [provenance](equal_route_start.txt),
[runner](../../sims/core/19_equal_route_lattice_control.py).

This control starts all forty coarse states at exactly `g=1`, retaining the
heterogeneous microscopic initial lattice. It uses experiment 08's remaining
default parameters and takes 60,000 deterministic updates. Chaotic and frozen
cases use matched microscopic initial states for each seed.

| Fine-state seed | Initial top-three share | Chaotic final share | Frozen final share |
|---|---:|---:|---:|
| 0 | 0.075 | 0.614599 | 0.075 |
| 1 | 0.075 | 0.462626 | 0.075 |
| 2 | 0.075 | 0.529488 | 0.075 |

The fine-scale dynamics can therefore seed differentiated sharing without any
initial coarse-route size differences. The system has microscopic variation,
not an exactly uniform state at every scale. The model supplies possible routes
and their response law, rather than an initial pattern of dominant channels.
This tests seeding within the specified geometry. It neither models the spatial
formation of the geometry nor crosses both boundaries of the noise window.

Experiment 08 now exposes `initial_spread`, whose default `0.01` preserves the
original numerical instructions. This control sets it to zero. Frozen-route
shares are checked against `3/40` in the runner.

## Contact geometry

[Output](contact_geometry.txt),
[source](../../sims/core/09_footprint_extensive_vs_coherent_q_emerges.py).

| Coupling | Variance versus mean-share slope | Final top-three share |
|---|---:|---:|
| Sum over separate patches | 1.01 | 0.17 |
| One common coherent patch | 2.00 | 0.08 |
| Fixed patches, amplitude proportional to share | 1.99 | 0.63 |

The slopes agree with variance addition under the prescribed patch couplings.
They are fits across route-wise time-averaged shares and variances, not
conditional short-time estimates of the diffusion exponent in the theorem.
The coherent case also uses the same fluctuation for every route. It changes
cross-route correlations, so the comparison does not isolate the effect of the
exponent. Neither slope near two is an above-window test for `m=1`.

Default parameters: 40 routes, 1,500 patches of 4×4 cells, 25,000 steps, coupling
0.35, state floor 0.02, seed 0. Random initialization is followed by deterministic
updates. These routes use clipping at a lower floor and have no fixed upper
reflecting boundary; they are not the bounded model used for exact stationarity.

## Copying funded by throughput

[Output](copy_accumulator.txt),
[source](../../sims/core/18_copying_derived_accumulator.py).

| Copy cost | Final mean state ± standard deviation | Copy-rate slope | Ideal slope |
|---|---:|---:|---:|
| 200 | 8.67 ± 1.27 | 0.0045 | 0.0050 |
| 500 | 4.32 ± 1.17 | 0.0017 | 0.0020 |
| No copying | 1.05 ± 0.19 | undefined | not applicable |

Default parameters: 40 routes, 60,000 steps, three runs with seeds 0–2,
efficiency 1, perturbation size 0.05, base event rate 0.05, floor 0.02. The
spread is the population standard deviation over those three runs, not an
uncertainty interval for the mechanism.

The accumulator determines copying times from incoming resources and cost.
The copying machinery, inheritance, perturbation and replacement rules are
supplied. Random draws continue throughout this model; it is not connected to
the deterministic lattice. Replacement erases some accumulated resources,
and the code counts self-targeted attempts as births even though no replacement
occurs. The fitted rate is therefore an attempt-rate diagnostic, not an exact
measurement of successful offspring production.

## What these examples leave open

The proposed connection is:

1. Deterministic fine-scale dynamics supply effective coarse variation.
2. Variation and flow obey rules that place concentration inside a bounded window.
3. States persist and are copied, with reproduction funded by flow.

The scripts provide examples for parts of that connection, including a seed
mechanism for differentiating equivalent coarse routes. They have not yet
joined it in one model or represented the development of spatial flow paths
and connectivity in a material. Failure of one incomplete bridge is not a test of the
entire physical proposal. Conversely, agreement in separate examples does not
prove the complete proposal.

## Reproduce

From the repository root after installing `requirements-validation.txt`:

```sh
python sims/core/08_mutation_from_unseen_layers_no_rng.py
python sims/core/09_footprint_extensive_vs_coherent_q_emerges.py
python sims/core/18_copying_derived_accumulator.py
python sims/core/19_equal_route_lattice_control.py
```

The first three retained outputs are rounded by the original scripts. Those runs were made
from implementation `980fd41`; subsequent changes to script descriptions do
not change their numerical instructions. The provenance hashes identify the
source files used for the runs. The equal-start control has its own source hashes
and retains unrounded results in CSV. Its runner overwrites its two result files.
