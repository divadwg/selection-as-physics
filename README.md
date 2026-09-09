# Selection as physics

A research programme asking whether natural selection can be understood through
flows: deterministic fine-scale dynamics supply effective variation, a bounded
range of disturbance scaling permits concentrated sharing, and inherited states
can use flow to reproduce.

**Start with the [revised paper (PDF)](paper/finite_noise_window.pdf):
*A finite noise window for concentration of a shared flow*.**
[Editable source and build instructions](paper/README.md).

The paper combines an exact result for a specified stochastic model with
computational thought experiments exploring that proposed connection. The
repository supplies the implementations, independent stationary checks and
retained example runs, alongside further work on memory and inheritance.
The whole sequence has not yet been demonstrated in one physical system.

The models specify possible routes and their response to flow; they do not
prescribe which routes become dominant. An [equal-start lattice control](docs/research_examples/README.md#equal-coarse-route-start)
starts all forty routes identically: microscopic dynamics produce top-three
flow shares of 46–61%, compared with 7.5% initially and in frozen controls.
This demonstrates seeding of unequal sharing within the specified geometry.
The development of spatial paths and their connectivity in a material is not
yet modeled. Known power-law mathematics does not establish that broader
physical proposition, and this literature check has not shown that proposition
to be prior art.

## The proposed connection

1. A fine-grained deterministic lattice drives irregular disturbances in a coarse
   flow model, without fresh random input after initialization.
2. The stationary theory identifies a **bounded scaling window** for extreme
   flow concentration. Merely obtaining concentration is not enough to test it;
   the two failure regimes matter too.
3. Further models add persistent inherited states and copying funded by flow,
   asking how unequal sharing could become differential reproduction.

The contribution being investigated is this physical connection. The familiar
mathematics of one step does not establish that the complete connection is old,
nor do the separate examples prove it. The missing work is to join the steps
under consistent physical rules and test them together.

## The heredity sequence and its checks

The original programme already distinguishes three stages:

1. A pattern persists while flow replaces its material. Test whether a particular
   deviation survives renewal, as well as whether the general shape persists.
2. The pattern produces descendants. Test inherited differences and reproduction
   against disappearance, with individual identities and finite observation times.
3. A separate carrier recreates a property elsewhere. Test transmission using the
   same destination response and matched surroundings.

The [heredity audit](docs/heredity_audit.md) maps these stages to the existing
models, repairs the earlier claims and describes the new checks. Portable-token
simulations already existed; this revision strengthens their controls. A slowly
relaxing continuous carrier also succeeds in the new finite-time assay, so
universal claims that gates are necessary have been withdrawn.

The [new retained runs](docs/heredity_results/README.md) compare a lineage
extinction equation with independent event simulations, test both sides of a
copying threshold, and track transmitted state over repeated reproduction.
Copying and carrier laws remain explicit assumptions. Fine-lattice fluctuations
would count as mutation when they change a state that descendants inherit; that
coupling has not yet been joined to these new stochastic checks.

## A candidate prediction about establishment

With inherited states, the relevant reproduction threshold counts the kinds of
offspring a lineage produces, not just one founder's total births. Applying
established branching mathematics gives a predicted maximum copying cost from
flow, state transitions, disappearance and transmission fidelity.

In the tested extension, restoration toward a lower channel state **hinders
establishment over short transit but can help over long transit**, when greater
activity also damages portable information. The reversal survives grid refinement
and disappears in the state-independent damage control. This is a conditional,
testable prediction of the stated model; its originality is not established.
It is distinct from the stationary concentration window. See the
[threshold results and assumptions](docs/heredity_results/README.md#candidate-threshold-reversal).

## What the stationary calculation establishes

Suppose channels divide a fixed throughput. Each channel has a state `g`, and its
share grows with `g^m`. Disturbance changes that state without a systematic bias
in the chosen coordinate. The question is whether a small fraction of channels
accounts for a large fraction of flow in stationary observations.

For the particular reflected, independently driven model

```text
S = sum_i g_i^m
J_i = I g_i^m / S             (the actual shares sum to I)
D_i = N g_i^q / S             (the chosen variance-rate rule)
1 <= g_i <= R, m > 0
```

the exact joint stationary density is proportional to `S * product_i g_i^(-q)`.
Writing `p0` for normalized `g^(-q)` and `f` for normalized `g^(m-q)`, this gives

```text
Tagged-channel occupancy: pN = (1 - 1/N) p0 + f/N
Pooled flow density:       f
Pooled half-flow fraction: PN = (1 - 1/N) P0 + 1/(2N)
```

Here `P0` is the population tail under `p0` above the threshold carrying half the
pooled flow. For exact powers, `PN` tends to zero as both the state range `R` and
population `N` grow precisely when

**1 ≤ q ≤ m + 1.**

At fixed `N`, the fraction instead approaches `1/(2N)` inside that window. This
pooled statistic is different from counting whole channels carrying half the
flow in a single snapshot. Neither statistic establishes that particular
channels remain winners over time.

On `q=m`, disturbance variance rate is proportional to actual flow. Off that
line, the shared normalization is an assumption; a rule such as
`D_i proportional to J_i^(q/m)` is a different model. The inclusive endpoints
also need more than estimated limiting slopes: logarithmic factors can change
the result at an edge.

## Is the upper bound useful?

It puts a limit on this proposed concentration mechanism. Disturbance can become
so steeply dependent on size that large states are too rare to dominate pooled
flow as the state range expands. For `m=1`, the upper boundary is `q=2`.
Above it, a small but nonzero fraction can still carry half the flow; the result
does not predict equal sharing or a sharp transition in a finite apparatus.

This concerns the **slope of disturbance against state**, not its overall
strength. Multiplying all diffusivities by a constant changes the clock and
leaves the stationary distribution unchanged.

The threshold itself follows from familiar power-law moment mathematics; see
[Newman's review, Sections III.B and III.D](https://arxiv.org/abs/cond-mat/0412004),
which discusses both moment thresholds and weighted population tails. Its role here is a
conditional physical prediction, supported by an exact conserved-flow
calculation and a finite-population correction. The repository makes no priority
claim for the elementary inequality, and originality of the full model has not
been established. Its practical value depends on finding a
system where the stated assumptions and observables can be measured together.

## Thought experiments discussed in the paper

[Retained runs, assumptions and reproduction commands](docs/research_examples/README.md).

| Example | What the run shows | What it does not yet show |
|---|---|---|
| [Deterministic lattice](sims/core/08_mutation_from_unseen_layers_no_rng.py) | Concentration under deterministic updates after random initialization; reruns from the same state agree. | A diffusion limit, chaos being necessary, or self-formation of channels. The periodic control also concentrates. |
| [Contact patches](sims/core/09_footprint_extensive_vs_coherent_q_emerges.py) | Variance-versus-mean-share slopes of 1.01 and about 2 under different patch couplings. | Both window boundaries crossed in one controlled deterministic experiment; the coherent case also changes cross-route correlations. |
| [Copy accumulator](sims/core/18_copying_derived_accumulator.py) | Flow funds copy attempts; inherited states rise on average in the supplied copying model. | Copying machinery derived from the substrate, or reproduction driven by the same deterministic lattice. |

These examples make parts of the programme concrete. The exact theorem supplies
the conditional window; the lattice examples explore a source of disturbance;
the copying example explores reproduction. They use different dynamics and
must not be presented as one completed derivation.

## What the repository adds to the paper

| Resource | How it supports the paper |
|---|---|
| [Exact model implementation](sims/validation/conserved_flow.py) | Computes stationary marginals and quantiles, samples the full joint law, and simulates a reflecting event process. |
| [Automated tests](tests/test_conserved_flow.py) | Checks detailed balance by enumerating configurations, finite-population identities, an independent sampler, integral agreement, grid refinement and a relaxation control. |
| [Validation runner](sims/validation/run_validation.py) | Starts from low, high, log-uniform and stationary states; observes at physical times and retains transient as well as final errors. |
| [Retained results](docs/validation_results/README.md) | Records the default run, a [finer grid](docs/validation_results/finer_grid/README.md), and [forty channels](docs/validation_results/forty_channels/README.md), with seeds and parameters. |
| [Detailed model note](docs/conserved_flow_validation.md) | Derives the joint law and correction, explains the limits, and documents why the older walker check was insufficient. |
| [Heredity and establishment checks](docs/heredity_results/README.md) | Independently checks lineage probabilities, copying thresholds and transmission into fresh sites. |
| [Paper source and figure data](paper/README.md) | Makes the manuscript editable and the figure reproducible from the tested formula. |

The eight conserved-flow tests pass; six additional tests check the lineage and
carrier models against analytic controls and conservation requirements. Across the retained ensemble runs on `[1,3]`,
the largest final occupancy and flow CDF errors are approximately `0.0203` and
`0.0245`; the largest mean snapshot half-flow fraction error is `0.0114`.
All are below the declared `0.05` tolerance. This checks bounded implementations;
it does not establish equilibration at arbitrary ranges or physical validity.
Large-range tables and the paper figure are exact-law evaluations, not dynamic
simulations at those ranges.

## Further work beyond the paper

These older models have their own assumptions; the current
[heredity audit](docs/heredity_audit.md) distinguishes retained evidence from
superseded interpretations. They suggest further
questions; they are not consequences of the stationary theorem, and they have
not all received the same validation as `sims/validation/`.

| Extension | What it explores | Where to look |
|---|---|---|
| Memory and inheritance | How restoring drift erases deviations, and when repeated copying preserves them. | [Drift](sims/core/11_drift_kills_sorting.py), [copying and memory](sims/core/12_copying_rescues_heredity.py) |
| Lineage establishment | Whether a rare family survives when descendants inherit a changing state. | [Lineage instrument](sims/core/16_r0_instrument.py), [null models](sims/core/17_stricter_null_r0v2_necessity.py) |
| Transport of stored state | How barriers and travel time affect a detached state's ability to influence another site. | [Gated parcels](sims/core/13_portability_gated_parcels.py), [transit](sims/core/15_transit_gated_vs_ungated.py) |
| Structural boundaries | Toy models of loops, memory and channel formation under specified driving rules. | [Boundary simulations](sims/boundaries/) |

These extensions develop the programme discussed in the paper, including what
is needed for inherited differences to last and spread. Their results are
model-specific. The current work does not derive life, persistent winners, or
Darwinian evolution from diffusion alone.

## Entropy and the original motivation

The programme began with a proposed entropy-production explanation, then moved
to competition for input flow. The [corrected entropy ledger](docs/entropy_ledger.md)
explains what fixed boundary entropy flows do constrain, why nonlinearity differs
from discrete memory storage, and where copying costs and fidelity could provide
a thermodynamic connection. The stationary channel-state process has detailed
balance; its concentration window is not an entropy-production maximum.

## Evidence still needed

A physical test needs simultaneous individual channel states and flows under a
fixed total, adequate state range, and observations long enough to assess
stationarity. Drift, measurement noise, inter-channel correlations and the
shared factor `S` must be accounted for when estimating disturbance scaling.
An incomplete test cannot fairly reject the model.

The exploratory aggregate-nanowire dataset route was discontinued because it
could not test the channel-resolved fixed-total model. No exponent fit or
empirical verdict from that route is claimed. Existing notes placing published
exponents on the window are hypotheses, not validation.

## Run the validated model

From the repository root, with Python 3.10 or later:

```sh
python -m pip install -r requirements-validation.txt
python -m unittest discover -s tests -v
python -m sims.validation.run_validation
```

NumPy is the only dependency for these checks. The runner writes into
`docs/validation_results` by default; choose another `--output` directory to
keep the retained results. [More runs and build commands](paper/README.md).
Older exploratory scripts may require additional packages and run substantial
simulations when executed.

## Earlier material

The [experiment notebook](docs/experiments.md), [derivations](docs/derivations.md),
[research directions](docs/papers.md) and [references](docs/references.md) retain
the development of the wider programme. The
[previous README](docs/README_before_paper_revision_2026-09-09.md) preserves the
broader argument. Some historical prose makes stronger claims than the current
paper supports; this README, the revised paper and the conserved-flow validation
note define the current scope.

The old [independent-walker script](sims/core/04_selection_window_exact_law.py)
retains correct power-law integration, but its SDE experiment is an opt-in legacy
diagnostic. Starting at the desired stationary distribution did not establish
convergence. Historical figures based on that interpretation should not be used
as evidence for the revised theorem.
