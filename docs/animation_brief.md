# Brief: one-world animation (educational/marketing, not evidence)

Goal: a single looping animation (60-90 s, no narration needed, captions only) showing selection emerging from physics in one continuous world. This is an illustration of results already established separately in sims/; it proves nothing and must not be presented as evidence.

## The world
A 2D basin seen from above. Rain falls uniformly (gentle particle drizzle). Water routes downhill to one outlet edge. The bed is erodible; cutting rises with the water passing (this is the one nonlinearity, and the on-screen caption when channels first appear should say so: "where cutting rises with flow, channels carve themselves").

## Sequence (wide shot -> close-up -> wide shot)
1. 0-15 s, noise: flat noisy plateau, sheet flow, nothing but shimmer. Caption: "rain on a plateau; every cell equal."
2. 15-35 s, concentration: channels self-carve, dendritic network forms, a few grow dark (carrying most water), most fade. Overlay two counters: "channels above median width" (falls) and "share of water in top 3 channels" (rises past 50%). Caption: "count channels: most are trickles; count water: a few rivers."
3. 35-50 s, the zoom: camera dives into one reach of the biggest channel, transition to the flow-past-obstacle view (streamlines past a boulder, recirculation loop shaded behind it, growing with drive). Caption: "zoom into any channel and this is what it is made of: flow past obstruction; push hard enough and the flow makes a loop, the smallest thing with an inside." Then a beat where the same view runs with 'momentum off': loop vanishes, fore-aft symmetric. Caption: "linear flow never loops."
4. 50-70 s, memory and takeover: zoom back out. Show a capture event (one channel eroding into a neighbour's catchment, taking its water). Tint the bed by material type: self-clearing material (flow scours it wider) in green vs self-silting in grey; green spreads along the busy channels and takes over. Caption: "material the flow can rewrite is a rule; the self-reinforcing rule wins."
5. 70-85 s, the punchline: freeze, draw the two-census split as two small inset histograms (channels piled low, water spread high). Caption: "population piles where it is disturbed least; the flow sits with the few disturbed most. That gap is natural selection, from physics."
6. 85-90 s: title card: "Selection is what a flow does to the material it passes through." + repo URL.

## Technical guidance
- Do NOT couple lattice-Boltzmann to erosion (fragile). Two separate engines, cut between them: plateau engine = D8 routing + stream-power erosion on ~200x120 grid (port of sims/boundaries/03, add material-type layer from sims/core/06 and capture from hyb seed-capture logic); close-up engine = D2Q9 lattice Boltzmann past a disc (port of sims/boundaries/01), precomputed at 3 drives + linear control.
- Determinism: seed everything once; the animation should be exactly reproducible.
- Render: matplotlib/manim or canvas; 1080p, dark background, water in blues, bed in earth tones, self-clearing material green.
- Counters must be computed from the running sim, not scripted.
- Honesty rule: captions state only what the separate experiments established; no claims about biology beyond the final title card's "from physics".

## Assets to reuse
- sims/boundaries/03 (plateau), sims/core/06 (material types), sims/boundaries/01 (LB flow + linear control), sims/boundaries/05 (bump memory, optional beat if time allows: kill flow, bed remembers).
