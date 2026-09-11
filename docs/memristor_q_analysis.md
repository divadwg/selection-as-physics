# Memristors as a candidate test of the sorting mechanism

Revised 11 September 2026. The [earlier interpretation](memristor_q_analysis_before_assay_audit.md)
was useful for identifying a candidate platform, but overstated what measured
read-noise slopes established. It is not empirical confirmation of the window.

## What the published work supplies

[Balogh et al., 1/f noise spectroscopy and noise tailoring of nanoelectronic devices](https://arxiv.org/abs/2106.02683)
reviews resistance-dependent fluctuations and their microscopic interpretation.
[Manning et al., winner-takes-all paths](https://doi.org/10.1038/s41467-018-05517-6)
demonstrates and models concentrated conduction in nanowire networks.
These motivate a candidate system; neither establishes our conditional diffusion
law or a two-sided stationary window. Existing physical explanations of pathway
selection must be compared with ours, rather than treating all concentration as
support for the same mechanism.

The earlier conversion from relative conductance noise to exponents near -1,
1.5 and 2 was a hypothesis about the relevant state dynamics. A band-limited
read-noise variance is not automatically a diffusion coefficient for conductance
rewriting. A 1/f spectrum especially requires care about temporal memory, bandwidth
and which state is actually changing. The exponent 2 is a boundary for m=1,
not a measurement beyond the upper edge. Claims that existing regimes already
confirm or falsify the sorting prediction are withdrawn; the platform is not rejected.

## Proposed apparatus: parallel, separately measured branches

A practical candidate is a fixed set of separately sensed memristive branches in
parallel, supplied by one regulated total current. Start with individual devices
as the observable channels; resolving multiple filaments inside one device would
require additional instrumentation. Feasibility and non-invasive readout still
need assessment. A device-level test would establish a result at that level,
not automatically at the level of internal filaments.

In an approximately ohmic operating range, let G_i be branch conductance and
G_tot=sum G_i. Then I_i=I_total G_i/G_tot, giving m=1 if the model state is scaled
conductance. All branches share voltage V=I_total/G_tot. Sense each I_i and the
common V simultaneously to reconstruct conductances and actual shares. Correct
for sensing impedances; appreciably nonlinear branches require a different response
law. Current compliance on a voltage sweep is not equivalent to a regulated fixed
current throughout the measurement.

## Calibrate before testing concentration

1. Measure branch state changes at several time resolutions under drive. Separate
   instrumental read noise from persistent conductance changes. Estimate conditional
   drift and increment variance in the chosen state coordinate.
2. Account for the entire configuration: the theorem requires D_i proportional to
   G_i^q/G_tot, not just a power of G_i in isolation. Vary the other branches while
   keeping a target G_i comparable to test the G_tot dependence. Under current
   control this also changes voltage; that effect must be included, not ignored.
3. Check cross-branch correlations, bias-driven drift, jumps, bounds, ageing and
   whether a diffusion approximation is supported over any resolved time range.
   Correlated common-voltage effects are a potential mismatch with independent
   noise. A failed calibration leaves applicability open; it does not test the
   stationary prediction.
4. Only then predict finite-range pooled concentration on separate observations,
   using measured channel count and state range. Retain physical-time weighting,
   starts from different states and evidence of adequate relaxation. Do not fit
   the concentration curve to the same data used to declare success.

A useful amplitude control changes the common variance prefactor without changing
the calibrated drift, exponent or normalization. The model predicts unchanged
stationary sharing. A window test must instead change the *state dependence* of
variance while maintaining those other assumptions. We do not yet have a verified
experimental control that does this across both edges. Changing drive, temperature
or filament regime may change several quantities simultaneously; such comparisons
need full recalibration rather than interpretation as a pure noise sweep.

## Current, power and any optimisation claim

Holding current fixed does not hold input power fixed:

```text
V = I_total/G_tot
P = I_total V = I_total^2/G_tot.
```

At fixed voltage instead, I_total=V G_tot and P=V^2 G_tot. Those are different
boundary conditions. Record voltage and power as well as the shares. A larger
G_tot would lower dissipation under fixed current, but the sorting theorem does
not say G_tot increases monotonically or is maximised. Two configurations with
the same G_tot can have very different share concentration and identical power.
No maximum-power or minimum-dissipation claim follows merely from uneven shares.

## What we still need

A viable branch-resolved measurement protocol; identification of state-rewriting
noise; calibration of the joint law and its time range; and a control capable
of changing its scaling without silently changing the mechanism. Aggregate network
traces alone do not supply these. The older aggregate-data detour remains closed;
this is a more specific prospective test, not a relabelling of that dataset as
validation. No apparatus has been built or physical outcome measured in this audit.
