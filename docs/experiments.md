# Experiments (record)


1. Driven lattice flow past a disc (D2Q9): closed loop above Re ≈ 10, grows with drive; linear rule: no loop at any drive, fore-aft symmetric. No shedding seen in run time (T7 in flow not reproduced).
2. River-bed hybrid: seed a bump, loop forms in lee. Wipe flow, keep bump: loop regrows. Keep flow, remove bump: loop dies. Memory lives in the slow layer (T11).
3. Seeds capture bed material in proportion to size (rich get richer); weak competition in periodic channel; sub-cell roughness erased (lattice threshold, not physics).
4. Memory dial: linear memory only slows forgetting; gated memory holds indefinitely (T8a).
5. Held-back plateau: flow-proportional cutting builds a dendritic channel network from noise, channels compete and capture; slope-only cutting builds a smooth sheet.
6. Rhythm on a linear medium: storage pays ~10% more throughput but no pattern forms. Making memory pay is not making it concentrate.
7. Forty routes, undirected additive kicks at rate ∝ share: concentration (Theorem iii); flat noise: no. Survives floor, ceiling, rate, kick-size tests. Dies at sublinear share law.
8. Add undirected copying ∝ share: population mean climbs 1 → 13; controls flat (Theorem iv).
9. Add free-sign write-back: positive couplings take over 95–99% within 5000 steps; no copying: win flux, don't spread; no write-back: nothing; no gate: still works (Theorem v, T12a).
10. One-substrate version (material obstructs flow, flow moves material per the material's own property, spreads where activity is): erodible sign takes over 96%; controls as predicted (R6).
11. Boundary sweep m = 0.5 … 2: matches Theorem (iii).


## Which sim is which

### Conserved-flow validation update

`sims/validation/` derives and checks the coupled finite-population stationary law.
It tests multiple initial conditions at fixed physical times, compares against an
independent exact joint-law sampler, and separates pooled from snapshot half-flow
fractions. See [the derivation](conserved_flow_validation.md) and
[retained results](validation_results/README.md). This replaces the interpretation
of script 04 as a validation of conserved-flow dynamics.

### Core (paper 1: the theorem and its checks)
| Script | What it shows | Figure |
|---|---|---|
| `sims/core/01_concentration_forty_routes.py` | forty routes, undirected kicks at rate ∝ share: flux concentrates; flat noise: no | `figures/core/concentration_only_when_noise_scales_with_share.png` |
| `sims/core/02_heredity_copying_climb.py` | add undirected copying ∝ share: population mean trait climbs; controls flat | `figures/core/heredity_copying_population_climbs.png` |
| `sims/core/03_exponent_sweep_toy_line.py` | on the line q = m: no concentration below m = 1, marginal at 1 | `figures/core/exponent_sweep_toy_line_selection_iff_m_ge_1.png` |
| `sims/core/04_selection_window_exact_law.py` | exact power-law integrals; historical independent-SDE run retained only as an optional diagnostic, not a convergence check | `figures/core/selection_window_phase_diagram_m_q.png` |
| `sims/core/05_writeback_free_sign_selection.py` | free-sign flow-to-rule coupling: positive sign takes over; controls | `figures/core/writeback_self_reinforcing_sign_takes_over.png` |
| `sims/core/06_one_substrate_no_channel_supplied.py` | material obstructs flow, flow moves material by its own property: erodible sign wins; no channel drawn | `figures/core/one_substrate_self_clearing_material_takes_over.png` |
| `sims/core/18_copying_derived_accumulator.py` | copying derived, not imposed: accumulator A += ηJ, copy at cost E; emergent b(J) linear, slope ≈ 0.9·η/E (200: 0.0045 vs 0.0050; 500: 0.0017 vs 0.0020); mean-g climbs 8.7 / 4.3 scaling inversely with cost; flat without copying. Closes the J→b bridge | (numbers in record) |
| `sims/core/17_stricter_null_r0v2_necessity.py` | (a) stricter null: junction pairs +0.40 vs straight-segment +0.66: h2 signal is carved-line continuity, not branching-specific transmission; rung-2 claim reframed (inheritance = connectivity at bifurcation). (b) R0 v2: trajectory-integrated R0_eff up to 30 with zero survival; establishment is a first-passage escape race, not an R0 phenomenon; P_surv ≈ 1-(1-p_esc)^M; two-stage law (escape, then compounding). (c) ungated-necessity: gated effect flat with distance (+1.5/+1.2), continuous parcels transmit nothing (+0.04/+0.01): gating necessary and sufficient for portability | (numbers in file and record) |
| `sims/core/14_dentlife_vs_activity.py` | D1-tension prediction: dent half-life vs local discharge. Healing-dominated regime: flat (+0.03), NOT confirmed; churn-dominated regime (healing off, churn up): −0.16, confirmed. Scope condition added to D1: the tension bites only where activity-churn dominates erasure | (numbers in record) |
| `sims/core/15_transit_gated_vs_ungated.py` | D4 prediction, clean redesign of the confounded control (no types; value-only transit). Direction confirmed; sharpened: toy gate (diffusive accumulator) gives quadratic-in-barrier persistence, true Kramers-exponential needs a metastable well; dial fidelity saturates at a noise floor as λ→0 while gate fidelity keeps rising with ΔE: gates are tunable to arbitrary persistence, dials are not | (numbers in record) |
| `sims/core/16_r0_instrument.py` | R0 instrument, first run: lineages die (P_surv = 0) despite per-progenitor R0 up to 1.5; branching theory fails because offspring inherit the parent's decaying g and the family sinks together (correlated fates). Finding: establishment requires trait escape from re-templating, not just multiplication; R0 must be computed along the decaying trajectory (D2's τ_dev factor doing the work). Instrument to be upgraded accordingly | (numbers in record) |
| `sims/core/13_portability_gated_parcels.py` | rung 3 first pass: gated type tokens shed downstream shape child-site flow at 10-60 sites beyond parent's reach (+0.94 vs shuffled-token null -0.14); transported self-reinforcing type sweeps 0.50 → 0.95; ungated control confounded (types frozen but write-back active), redesign owed before 'gating necessary' is claimed; first measurement recorded parent type at end not emission, corrected in-file | `figures/core/portability_gated_parcels_rung3.png` |
| `sims/core/12_copying_rescues_heredity.py` | with copying ∝ share, the population climb survives re-templating that kills sorting alone (mean g 3.3-4.3 vs 1.08 at dent-life 10k), rescue scales with copy rate, fails where copy-interval ≈ dent-life; copying homogenises shares while raising them | `figures/core/copying_rescues_heredity_from_retemplating.png` |
| `sims/core/11_drift_kills_sorting.py` | restoring drift toward environment-set g*: concentration 0.48 → 0.09 as dent-life falls ∞ → 100 steps; consistency check, near-tautological, of the weak-re-templating condition the zero-drift theorem assumed; successor experiment (copying as memory refresh) is the one with falsifiable content | `figures/core/drift_kills_sorting_dent_life.png` |
| `sims/core/10_h2_heredity_from_flow.py` | plateau with healing dial: v1 raw parent-daughter regression confounded by spatial smoothness (rose with healing); v2 distance-matched null: heredity excess +0.21 at zero healing, ≈0 by λ=0.05; heredity lives in the slow layer and one dial kills it (D2b in numbers) | `figures/core/heredity_from_flow_excess_vs_healing.png` |
| `sims/core/09_footprint_extensive_vs_coherent_q_emerges.py` | footprint ∝ share at fixed per-patch coupling on chaotic substrate: variance exponent 1.01 emerges (D ∝ J derived, not injected); coherent control: 2.00, at/above upper edge; common-mode noise fails to select even in-window: variation must be idiosyncratic | `figures/core/footprint_q_emerges_and_common_mode_fails.png` |
| `sims/core/08_mutation_from_unseen_layers_no_rng.py` | deterministic chaotic substrate, no RNG after t=0: kicks emerge as coarse-level dice, variance ~ share² from contact alone, concentration follows; frozen substrate: nothing; periodic substrate: concentration without unpredictability, so selection needs scaled variance, not randomness | `figures/core/mutation_from_unseen_layers_no_rng.png` |
| `sims/core/07_q_from_published_exponents.py` | q from cities, firms, GDP, networks; firm stationary-vs-transient exponent check | `figures/core/real_systems_on_the_window.png` |

### Boundaries (what linear systems cannot do)

None of these is new physics. Recirculation above a threshold and the fore-aft symmetry of Stokes flow, bistable memory, stream-power channelisation, and the failure of a linear medium to pattern under periodic forcing are all textbook. They are here as checked, pictured preconditions of the theory's domain, not as results; they belong in a paper only as illustrations of the boundaries the core theorem assumes.
| Script | What it shows | Figure |
|---|---|---|
| `sims/boundaries/01_lattice_flow_loops_above_threshold.py` | D2Q9 flow past a disc: closed loop above Re ≈ 10, grows with drive; linear rule never loops | `figures/boundaries/lattice_flow_loops_vs_drive_linear_never_loops.png` |
| `sims/boundaries/02_memory_gate_vs_dial.py` | continuously rewritten memory only slows forgetting; gated memory holds | `figures/boundaries/memory_gate_holds_dial_only_slows.png` |
| `sims/boundaries/03_plateau_channel_network.py` | flow-proportional cutting builds channels from noise; slope-only cutting builds a sheet | `figures/boundaries/plateau_channels_form_only_with_flow_proportional_cutting.png` |
| `sims/boundaries/04_blinking_gradient_negative.py` | storage pays under rhythm but no pattern forms in a linear medium | `figures/boundaries/blinking_gradient_builds_no_pattern.png` |
| `sims/boundaries/05_riverbed_hybrid_memory_in_slow_layer.py` | seed a bump: loop forms; kill flow keep bump, loop regrows; keep flow kill bump, loop dies; seeds capture bed material ∝ size | `figures/boundaries/riverbed_memory_lives_in_bump_not_flow.png` |

Dropped from the repo (numbers retained in the record above): stress-test script for concentration (floor/ceiling/rate/kick/splitting), the superseded first lattice script, and four river-bed figures (bump erosion, rough bed, seed capture) whose content is three sentences.
