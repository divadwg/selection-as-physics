# Spatial construction checks

These checks distinguish channel geometry, sorting, a persistent flow pattern,
and pattern multiplication. They do not claim that all occur under one model,
or that dividing patterns necessarily inherit selectable variations.

## Existing lattice flow past a pole

The starting point is the repository's original boundary experiment 01. Its
missing `lg.py` helper has been restored using standard D2Q9 equilibrium moments.
The undocumented vorticity-patch counter has been removed. The runner now writes
portable output paths, uses deterministic inlet conditions, and overwrites open
boundaries after streaming to remove unintended periodic x wraparound. This is
a repaired implementation, not a reproduction of the unavailable helper's counts.
The transverse boundary remains periodic.

Each site has nine directional populations, with streaming to neighbouring sites
and relaxation toward a local equilibrium. Density and momentum are the moments
of those populations. This is a simple lattice-Boltzmann fluid model with the
usual hydrodynamic connection to Navier–Stokes, not a direct molecular gas or an
arbitrary lattice of real-valued neighbours. See
[the asymptotic analysis](https://doi.org/10.1016/j.jcp.2005.05.003).
The circular obstacle represents persistent environmental heterogeneity. Its
existence and persistence are imposed; the circulating wake is not drawn into
the initial condition. A fixed obstacle is not time-varying stochastic noise.

| Nominal Reynolds number | Rule / geometry | Returning tracers, coarse / finer grid |
|---|---|---:|
| 2 | Full rule, pole | 0 / not run |
| 20 | Full rule, pole | 10 / 6 |
| 20 | Linear rule, pole | 0 / not run |
| 20 | Full rule, no pole | 0 / not run |
| 40 | Full rule, pole | 60 / 50 |
| 40 | Linear rule, pole | 0 / not run |

These are 120 trial trajectories in the final frozen velocity field, not 120
independent simulations or a count of whirlpools. Return requires a full turn
in velocity direction, path length above two obstacle radii, and return within
one lattice unit of the starting point. Low-speed closed paths required a longer
tracer observation than the first trial; the initial failure to see a return was
not used to reject circulation. A solid-rotation field and a uniform straight
field independently test the detector. This gives numerical evidence of wake
circulation; it does not establish indefinite trapping in a time-dependent flow.

Full-rule field changes over the final observation extension are below 0.4% of
the nominal inlet velocity. Density and probe diagnostics are retained. The two
grids change obstacle resolution with domain proportions held fixed. They support
the qualitative result but do not determine a precise Reynolds-number threshold.
The linear rule removes the quadratic equilibrium terms: it is a comparison in
this geometry, not a universal theorem that linear flow can never circulate.
No vortex reproduction or inheritance is claimed here.

`pole_flow.csv` contains the measurements; `pole_manifest.json` records settings
and source hashes. NPZ files retain velocity, vorticity, the obstacle and tracer
paths. A larger returning count is not a larger physical population.

## Channel geometry, separate from concentration

The earlier plateau model could route from a depression to a higher neighbour.
The new drainage routine permits only strictly downhill transfer, terminates flow
at the outlet, and accounts for any flow retained at pits. Descending elevation
then gives an acyclic accumulation order and outlet-plus-pit flow equals rainfall.
Unit total rainfall and a rough slope initialize the landscape. No incised paths
are supplied. D8 routing does choose one downhill neighbour per cell, so this is
a landscape model, not a resolved water-sheet instability.

Across five initial roughness seeds, flow-dependent erosion develops transverse
relief in four runs; one remains smooth at the tested time. Final top-three outlet
fractions range from .0625 to .6033. The slope-only control ends at .0625 in all
five runs. The geometric relief measure, rather than the flow fraction alone,
identifies bed structure. Initial erosion totals are matched between controls;
subsequent erosion histories need not match. This small fixed-grid study is an
existence example in the supplied erosion law, not a universal threshold or
spatial-convergence claim.

`landscape.csv` retains every recorded state metric for both models and all five
seeds. Initial/final fields for seed zero are saved. All recorded terminal flow
balances equal one to floating-point precision. Do not infer a negative physical
verdict from the one smooth finite-time run.

## Pattern multiplication through local reactions

The separate constructive example is the established Gray–Scott system:

```
du/dt = .16 Laplacian(u) - u*v² + F*(1-u)
dv/dt = .08 Laplacian(v) + u*v² - (F+k)*v
F=.03, k=.062
```

The local reaction U+2V -> 3V is autocatalytic; diffusion moves material and the
reservoir feeds/removes it. These reaction laws are supplied. There is no operation
that detects a spot and creates another spot. The model therefore demonstrates
macroscopic pattern multiplication from microscopic kinetic rules, not the origin
of autocatalytic chemistry itself. Feed is a distributed reservoir exchange, not
the fixed-total flow of the concentration theorem. No energy ledger is inferred
from these irreversible kinetic equations.

One finite circular perturbation, with small initial irregularities, develops
multiple separated spots during deterministic evolution. Three seeds give 51,
49 and 53 connected regions above concentration .2 at time 4000. Halving the
timestep gives 51; refining space and time together gives 45; expanding the domain
gives 56. Exact counts depend on resolution and threshold; multiplication is the
qualitative result. Time zero can contain disconnected islands at threshold .25
because that threshold cuts through the perturbed initial concentration, so it
must not be used to claim multiple initial parent spots. At .15 and .2 the initial
region is connected.

The unseeded state, small distributed noise, and controls removing the nonlinear
reaction or the feed produce no surviving spots in these runs. This shows why
origin amplitude and subsequent amplification are different questions. A finite
prepared disturbance establishes possibility in this model; small-noise failure
does not measure a spontaneous waiting time or exclude larger rare disturbances.

The stored time series and snapshots show growth and subdivision, not individual
parentage or transmission of a selectable variant. Those remain open. These are
reproductions of known mechanisms, not new discoveries:
[Pearson (1993)](https://arxiv.org/abs/patt-sol/9304003),
[Reynolds, Ponce-Dawson and Pearson (1997)](https://doi.org/10.1103/PhysRevE.56.185).
Related spot replication was observed in a different chemical reaction system:
[Lee and colleagues (1994)](https://doi.org/10.1038/369215a0).

## Reproduce

From the repository root with NumPy installed:

```sh
python -m unittest discover -s tests -v
python -m sims.validation.run_construction --output work/construction-results
python -m sims.validation.run_pole_flow --output work/construction-results
```

The output arguments preserve committed data. `manifest.json` records the spatial
construction settings and hashes; `pole_manifest.json` covers the restored flow
model. Six new tests check fluid moments, tracer controls, downhill drainage,
periodic components and reaction/diffusion balances. These supplement the earlier
stationary and heredity checks. The paper presents the argument briefly; methods,
controls and limitations live here.
