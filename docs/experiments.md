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

- `sims/lg.py`, `sims/lg2.py`: D2Q9 lattice flow past a disc; loops above threshold; linear control. Figures: loops_vs_drive, threshold.
- `sims/hyb.py`: river-bed hybrid; memory test; seed capture. Figures: memory_test, bump_test2, rough_bed_test, seed_capture.
- `sims/memdial.py`: memory as dial vs gate. Figure: memory_dial.
- `sims/heldback.py`: plateau channel network. Figure: heldback_plateau.
- `sims/rhythm.py`: blinking gradient over a linear medium (negative). Figure: rhythm_test.
- `sims/kink.py`, `kink2.py`, `kink3.py`: forty-route concentration, stress tests, heredity. Figure: heredity_test.
- `sims/memloop.py`: free-sign write-back. `sims/substrate.py`: one-substrate version.
- `sims/boundary.py`: m sweep on the toy line q = m.
- `sims/realdata.py`: q from published fluctuation exponents; firm transient-vs-stationary check.
- `sims/window2.py`: exact-law integration of the (m,q) window; large-N Itô SDE check.
