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

### Core (paper 1: the theorem and its checks)
| Script | What it shows | Figure |
|---|---|---|
| `sims/core/01_concentration_forty_routes.py` | forty routes, undirected kicks at rate ∝ share: flux concentrates; flat noise: no | `figures/core/concentration_only_when_noise_scales_with_share.png` |
| `sims/core/02_heredity_copying_climb.py` | add undirected copying ∝ share: population mean trait climbs; controls flat | `figures/core/heredity_copying_population_climbs.png` |
| `sims/core/03_exponent_sweep_toy_line.py` | on the line q = m: no concentration below m = 1, marginal at 1 | `figures/core/exponent_sweep_toy_line_selection_iff_m_ge_1.png` |
| `sims/core/04_selection_window_exact_law.py` | exact stationary law integrated over (m, q); large-N Itô SDE check | `figures/core/selection_window_phase_diagram_m_q.png` |
| `sims/core/05_writeback_free_sign_selection.py` | free-sign flow-to-rule coupling: positive sign takes over; controls | `figures/core/writeback_self_reinforcing_sign_takes_over.png` |
| `sims/core/06_one_substrate_no_channel_supplied.py` | material obstructs flow, flow moves material by its own property: erodible sign wins; no channel drawn | (numbers in record above) |
| `sims/core/07_q_from_published_exponents.py` | q from cities, firms, GDP, networks; firm stationary-vs-transient exponent check | (table in record above) |

### Boundaries (paper 2: what linear systems cannot do)
| Script | What it shows | Figure |
|---|---|---|
| `sims/boundaries/01_lattice_flow_loops_above_threshold.py` | D2Q9 flow past a disc: closed loop above Re ≈ 10, grows with drive; linear rule never loops | `figures/boundaries/lattice_flow_loops_vs_drive_linear_never_loops.png` |
| `sims/boundaries/02_memory_gate_vs_dial.py` | continuously rewritten memory only slows forgetting; gated memory holds | `figures/boundaries/memory_gate_holds_dial_only_slows.png` |
| `sims/boundaries/03_plateau_channel_network.py` | flow-proportional cutting builds channels from noise; slope-only cutting builds a sheet | `figures/boundaries/plateau_channels_form_only_with_flow_proportional_cutting.png` |
| `sims/boundaries/04_blinking_gradient_negative.py` | storage pays under rhythm but no pattern forms in a linear medium | `figures/boundaries/blinking_gradient_builds_no_pattern.png` |
| `sims/boundaries/05_riverbed_hybrid_memory_in_slow_layer.py` | seed a bump: loop forms; kill flow keep bump, loop regrows; keep flow kill bump, loop dies; seeds capture bed material ∝ size | `figures/boundaries/riverbed_memory_lives_in_bump_not_flow.png` |

Dropped from the repo (numbers retained in the record above): stress-test script for concentration (floor/ceiling/rate/kick/splitting), the superseded first lattice script, and four river-bed figures (bump erosion, rough bed, seed capture) whose content is three sentences.
