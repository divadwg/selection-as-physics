# Natural selection as physics

*Logic summary. This README is the argument. Records, references and history are in `docs/`; code in `sims/`; figures in `figures/`.*

---

## 0. Plain English summary

We started with one thermodynamic fact. Order has to be paid for: any pattern that persists in a flow is rebuilt continuously, and rebuilding it exports entropy (second law); for patterns maintained against noise by continual error correction, that correction is erasure and carries a Landauer floor. So a finite energy flux can sustain only a bounded amount of *maintained* order. Turned round: for a given flux there is a maximum negentropy of this kind. (Well supported, not a general theorem: no minimum cost per unit order for merely existing is established.) Complexity has an energy budget; organisms are not fragile because they are complex, they are complex because they run on huge throughput.

From there: pushed hard enough, a flow cannot stay smooth and must make structure, and the minimal structure is a loop, the smallest thing with an inside. Everything is flow; a whirlpool and a strand of DNA both replace their substance continuously. Most flow patterns forget (nudge them and the gradient rebuilds the old shape); a few remember (they rebuild by copying their own last state). That single difference in the rebuild rule is the gap between persisting and evolving.

Then the result. Each channel's state wanders with a jitter (diffusivity) that may grow with the flux it carries; that growth is a hypothesis to measure, not a law. When it does grow, the population piles into quiet low states while the flux is carried by the rare high ones. That is concentration and differential persistence; when copying is also proportional to share, it becomes Darwinian selection with fitness equal to share. It holds only inside a window: jitter must grow at least linearly with state, and not faster than one power above how flux grows with state. Copying makes it cumulative; feedback makes it reflexive.

**How far from "natural selection is physics":** three levels. (A) Solid: throughput-scaled state noise gives population/flux inversion and concentration iff m ≥ 1; a small sharp stochastic result, related to Landauer's blowtorch and to nonlinear preferential attachment. (B) One bridge away: when throughput also controls copying, ordinary Darwinian selection follows; the bridge (reproduction ∝ throughput) and the constitutive hypothesis (D ∝ g^m) are what must be defended or measured. (C) The synthesis (loops, rebuild rules, everything is flow) is a research programme, not a theorem, and must not ride on (A). Not done: one real system measured end to end, and the identification with biological reproduction-selection is argued, not measured. Honest status: proved in the smallest systems that can carry it, located where it stops, not yet shown to be what biology runs on.

---

## 1. The theorem in one non-living example, and where life enters

Take a rainy basin. A fixed amount of water falls each year and must leave by some set of channels: that is the conserved total. Each channel has a state, its width. Wider channels carry more water roughly in proportion: that is the share, Ohm's law for water. Every year each channel's banks are knocked about at random, silting or scouring, and a channel carrying more water has its banks disturbed more often. Those disturbances are kicks, undirected. How often a channel is kicked, times how hard squared, is its jitter (the diffusivity D).

Two counts. Count channels: over time most are narrow, because a channel that silts up carries little, is rarely disturbed, and stays as it is; the population drifts to where jitter is least. That is Landauer's blowtorch, and all he claimed. Count water: it is carried by the few wide channels, because share follows width and the wide ones, however few, are still wide. Population says trickles; water says a handful of rivers. The counts disagree, and disagree more over time as long as jitter grows at least in proportion to width. Braided rivers and drainage networks are this, measured, with nothing alive in them. The disagreement is the shape Darwin described: many are born, a few carry the future, and the few are not a random sample.

So far no lineage. A wide channel is wide; when it silts it is gone. For the picture to climb rather than spread, width must pass between channels. Rivers do it two ways: a channel wider than its stable size splits, each branch inheriting the parent's cross-section (splitting); a wide channel erodes into a neighbour's catchment and takes its water (capture). Both are copying at a rate rising with share, both are physics, and both make the basin's channels widen on average over time: Price's equation with nothing alive.

What rivers cannot do is carry width as a number. A channel's state travels only with the channel, by splitting or conquest. It cannot be handed to a different channel, stored, varied, and handed on again. That missing row is where the theory says life begins. Grass does it: a tuft drops seed, and the seed carries the root plan without carrying the root. The state has become portable, and once portable it accumulates. The theorem does not need that row; concentration, the disagreement between counts, and the climb by splitting and capture all follow without it. The row is what selection produces when something can carry a state away from its carrier. That is why the same theorem covers rivers and grass, and why it puts the boundary between them at one place: not metabolism, not reproduction, but the point where a channel's state can travel without the channel.

### Term map

| Term | Maths | River basin | Darwin |
|---|---|---|---|
| Conserved total I | fixed sum shared by N channels | the year's rain | carrying capacity, the finite resource |
| Channel i | one of N parts | one channel | one individual or lineage |
| State g | variable setting a channel's share | width | the heritable trait |
| Share g^m/Σg^m | fraction of the total | fraction of water | fitness (once copying is tied to it) |
| Exponent m | how steeply share rises with state | does doubling width double water (yes, m≈1) | how strongly the trait matters |
| Kick | random ± change to g | banks silt or scour | mutation, undirected |
| Kick rate r(g) | how often | more for busier channels | mutation rate, rising with activity (hypothesis) |
| Kick size σ(g) | how big | how much one disturbance changes width | mutation effect size |
| Jitter D = ½rσ² | diffusivity | how much width wanders per year | rate the trait drifts |
| Occupancy p ∝ 1/D | fraction of channels at each state | most channels narrow | the ordinary many (this row is the blowtorch, nothing more) |
| Flux density share·p | fraction of total at each state; flat when q=m | water spread evenly across widths | resource sits in the rare large few |
| Concentration 1 ≤ q ≤ m+1 | vanishing fraction carries finite share | a few channels carry most water | differential success; fails if jitter grows too slowly, or too fast relative to flux |
| Copying ∝ share | a state overwrites a neighbour's | splitting; capture | reproduction; here share becomes fitness by definition |
| Mean trait rises | Δḡ = Cov(g, w)/w̄ (Price) | channels widen on average | descent with modification |
| Write-back c | own flux rewrites own state, sign free | a channel whose flow scours it wider | adaptation; positive sign wins |
| Floor, range | reflecting g_min; spread so far | can't be narrower than zero | extinction; time for diversity |
| Portable state | state carried without its carrier | rivers cannot; seed can | heredity as such; where life starts |

*Free premises, not in the theorem:* kick rate (more precisely D) rises at least linearly with state; share is linear in state; copying goes with share. Each is a claim about the world to be measured.

*The equation.* p(g) ∝ 1/D(g). With share ∝ g^m and D ∝ g^q: flux density ∝ g^(m−q); concentration iff 1 ≤ q ≤ m+1, both edges marginal; the toy is q = m, inside the window for all m ≥ 1.

## 2. Definitions

- D1. *Pattern*: a configuration distinguishable from background at some resolution.
- D2. *Gradient-rebuilt* vs *self-rebuilt* pattern: re-formed each instant from ambient physics, versus re-formed by reference to its own prior state. Both are flow; both replace their substance. The rebuild rule is the difference. Whirlpool: nudge it, the gradient restores the old shape. DNA: nudge a base, the next copy carries the nudge.
- D3. Domain: gradient-rebuilt patterns and the self-rebuilt patterns they couple to. Kinetically trapped order (crystal, table) is outside: its entropy bill was paid once at creation; ours is paid continuously because existence and rebuilding are the same event.
- D4. *Loop in flow*: closed circulation distinct from through-flux. Needs two spatial dimensions (a 1D world has no interior), a conserved current (Life has none, so its gliders are travelling wobbles), and a nonlinearity (linear flow cannot tell upstream from down). A spiral is a circle plus a through-flux: closed in one direction (boundary, identity), open in the other (metabolism). A wobble repeats in time but encloses nothing: it leaks; a loop traps.
- D5. A pattern is *real* at a resolution if its shorthand predicts as well as tracking the parts (predictive closure); its *boundary* is the contour where the shorthand stops leaking. Not yet operational on a lattice.
- D6. *Self-routing ratio*: fraction of a pattern's sustaining flux that would not exist without it. Shaping loops (near 0: whirlpool, the water came anyway) vs causing loops (near 1: fire, no fire no oxidation). Independent of intensity. No agency implied; causal topology only.
- D7. *Hybrid*: a gradient-rebuilt loop coupled to a self-rebuilt pattern it reads and writes. Rule and flow are one substrate at two speeds; the channel between them is what a timescale separation is.
- D8. *Rule*: a local input-to-output mapping; misapplication under noise is a kink.
- D9. *Loop in memory*: rule shapes flow, flow writes rule, written rule shapes next flow. Same object as D4, one level up.

## 3. Rules (the objects selection acts on)

- R1. A rule is a standing local property that shapes how flow passes a point, is not consumed by that flow, and can differ from point to point. In the toy, g. In chemistry, a catalyst. In a CA, the update law if allowed to be local.
- R2. A catalyst is a rule. Which catalyst is present determines how the flow runs, without symbols. DNA is a catalyst set stored one level up. The gap is capacity, not kind.
- R3. A rule becomes heritable when it is local, stored in state, and carried and re-instantiated by the patterns it steers. Rule 110 fails all three: global, external, uncarried. That is why it computes and never evolves.
- R4. Misapplication under noise is a kink, the minimal nonlinearity. Where flux is, misapplication is more frequent (P6a).
- R5. Two rules in the toy: g (how much flux the channel passes; the phenotype the flow sees) and c (how the channel's throughput rewrites g; a rule about the rule; the genotype of the memory loop). Both kicked, both copied.
- R6. Rule and flow are one substrate on two timescales. Sand is the rule, erosion is the write; nobody supplies a channel. The "reading problem" was an artefact of drawing rule and flux as separate variables.
- R7. The evolving rule is not the physics rule. Ohm splitting, kick ∝ share, copy ∝ share, fixed total: universal and unvaried. Selection happens by them, not on them.

## 4. Premises

- P1 (First law): energy conserved.
- P2 (Second law): local order paid for with disorder elsewhere, at the time of the transaction.
- P3 (Minimum price, restricted): stated as a lemma, L1 below. No general floor for order merely existing.
- P4 (Instability): above critical throughput smooth relaxation is impossible; structure forced. Proven for convection; reproduced in our lattice; nonlinearity shown necessary.
- P5 (Preferred scale): flow structures have a stable size; surplus makes more, not bigger. Empirical; not reproduced by us.
- P6 (Noise): whatever an observer cannot resolve appears as irreducible noise in what they can (Mori-Zwanzig). Hidden below, dice above. Nothing here depends on what the hidden layer is made of.
- P6a (Constitutive hypothesis, not FDT): the diffusivity of a channel's state in the privileged variable g scales as g^m, i.e. with its throughput. Equilibrium FDT does not give this; far from equilibrium FDT is generically violated (Harada-Sasa). Status: hypothesis to be derived or tested per system class. Evidence in the direction: transcription-associated mutagenesis; metabolic-rate scaling of molecular evolution. Also assumed: kicks additive and symmetric in g (the stochastic metric); reparameterization changes the apparent exponent.
- P6b (Transport): what a flow can move, it moves in proportion to itself.
- P7 (Finitude): every gradient is finite.
- P8 (Storage): configurations stable between copies can hold information (Schrödinger's aperiodic crystal); their role is stability between copies, not permanence.
- P9 (Description/constructor): cumulative replication needs a stored description plus a reader (von Neumann).
- P10 (Linear response): share of flux rises at least linearly with the state that carries it, m ≥ 1. Ohm, stream power, catalysis satisfy; diffusion alone does not.

## 4a. Lemma L1 (irreversible maintenance)

In the domain of D3 a pattern persists only by being rebuilt. Rebuilding against noise means the noised state is discarded and the pattern's state re-imposed; discarding a state is logically irreversible, hence carries the Landauer erasure cost per erased degree of freedom per rebuild. Therefore maintained order in this domain has a minimum dissipation rate proportional to (order held) × (rebuild rate). Landauer supplies the cost of erasure; the lemma supplies the claim that maintenance contains erasure. The second half is what must be checked per system, not assumed. Outside D3 (kinetically trapped order) the lemma does not apply and no floor is claimed.

## 5. Theorem (the core)

General form. For a zero-drift Itô process in a coordinate g with reflecting boundaries, stationary density p(g) ∝ 1/D(g), where D(g) = ½·r(g)·σ(g)² is the local diffusivity (event rate × squared kick size). Special case (the toy): σ constant, r ∝ share, share ∝ g^m, so D ∝ g^m. Then:
- (i) Occupancy p(g) ∝ g^(−m): population piles where kicks are fewest (Landauer's blowtorch).
- (ii) Flux-weighted density g^m·p(g) is flat: flux spread over the whole explored range while population sits at the bottom. The inversion.
- (iii) General: with share J(g) ∝ g^m and diffusivity D(g) ∝ g^q, occupancy p ∝ g^(−q) and flux-weighted density J·p ∝ g^(m−q). Over explored range [1, R]: for q < m+1 the top carries the flux and the population fraction there → constant (q < 1), 1/ln R (q = 1), R^(1−q) (q > 1); at q = m+1 the flux integral is logarithmic and the fraction → R^(−m/2) → 0; for q > m+1 the flux integral converges, the half-flux state is a finite constant, and a finite fraction of channels carries it. **Selection window: 1 ≤ q ≤ m+1, both edges marginal.** Too little state-dependent jitter (q < 1): no concentration. Too much relative to throughput (q > m+1): high states so depleted that even flux sits low; no separation. The toy is the line q = m, inside the window for m ≥ 1, so the original 'selection iff m ≥ 1' stands. Verified on that line: top-3 share at 200k steps 0.18 / 0.35 / 0.61 / 0.96 / 0.98 for m = q = 0.5 / 0.75 / 1 / 1.5 / 2. Lower edge seen off the line (m = 1: q = 0.5 → 0.23, q = 1 → 0.39). Window verified by direct integration of the exact stationary law over range R = 10² to 10⁸ (fraction of channels carrying the top half of flux): m=1, q=0.5 → 0.21 constant; q=1 → 0.15, 0.075, 0.050, 0.038 (1/ln R); q=1.5 and 2 → 0.09, 0.01, 0.001, 0.0001 (power to zero); q=2.5 → 0.125 constant; q=3.5 → 0.315 constant; m=2, q=3 → 0; q=4 → 0.125 constant. Large-N Itô SDE (2×10⁵ walkers, no event cap) at m=q=1: fitted occupancy exponent 1.00, simulated fraction 0.1002 vs exact 0.1002. Forty-channel toy cannot resolve the upper edge (finite fraction vs 3/40; event cap saturates D); the exact law does.

*Empirical target (three separate measurements).* Measure independently J(g), r(g), σ²(g); construct D = ½·r·σ²; read off m and q. Selection by this mechanism iff 1 ≤ q ≤ m+1. 'Noise scales with flux' (D ∝ J) is one hypothesis placing a system on q = m; it is not part of the theorem.
- (iii′) Falsifiers, two-sided. Below the window: D flat or falling in g even when throughput rises (disturbances more frequent but smaller: a well-damped high-throughput channel); p flat or rising; no concentration or reversed. Above the window: D growing faster than g^(m+1); high states so rare that flux itself sits low; no separation. Prediction: neither regime shows selection by this mechanism. If either nonetheless concentrates, the stochastic coordinate is wrong, the Itô model is incomplete, or another mechanism is responsible.
- (iv) Copying into random neighbours at rate ∝ share is Moran with reproductive rate ∝ share. Mean share is fixed at 1/N; the mean trait g rises by Price, Δḡ = Cov(g, w)/w̄; kicks supply variance; population climbs in g. (Corrected: earlier 'mean share rises by its variance' was wrong.)
- (v) Write-back g ← g + c·share with c free, heritable, mean zero: growth rate ∝ c, largest positive c wins; relaxes once saturated. A replicator/feedback-selection result, not Eigen: no sequence space, no error threshold.
- Boundary (iii) is the γ = 1 threshold of nonlinear preferential attachment (Krapivsky-Redner-Leyvraz 2000) and η = 1 of dielectric breakdown. Cite; do not claim. What is ours: the exponent is fixed by physics not chosen, and the inversion.
- Caveats: multiplicative kicks concentrate by themselves (Gibrat), a different mechanism; the clean demonstration is additive. Convention (Itô) is fixed by events-then-kicks and must be stated. General statement in diffusivity: p ∝ 1/D(g); the theorem is about D(g) ∝ g^m plus share ∝ g^m in a privileged additive coordinate; 'exponent fixed by physics' requires physics to fix both the variable and the metric.

### Where entropy enters, and where it does not

- The theorem (p ∝ 1/D, the window) contains no entropy. Occupancy is set by kinetics along the path, not by entropy or its derivatives; that was Landauer's point in 1975.
- The flux I is fixed by the gradient and boundary conditions. Entropy production is not fixed by the flux: the same flux can pass through smooth channels producing little entropy or through structured, dissipative ones producing more.
- Maintaining a channel's structure is paid for out of its own share of the flux (T1, Lemma L1), bounded by that share (T2, per channel). So what is competed for is flux; each channel converts part of its share into the entropy that keeps it what it is, up to the limit of its share.
- The theorem is silent on how much a channel dissipates to hold its structure. Two channels with equal share can differ in dissipation and it does not decide between them. Selection here favours neither maximum nor minimum entropy production; it favours what carries flux. Dissipation is the price, not the score.
- A mill is a structured flow. Structured flows change flux (inputs and routes), not entropy production (outputs). Total entropy production is set by where the flow ends up (the sea, 255 K space) and is the same for every arrangement of channels on a given gradient; structure can raise it only by raising the inflow. Local order is paid for out of the channel's own share of a degradation that was already total: the bare gradient thermalised is the maximum that flux can produce, and structure can match it (steady maintenance) or fall below it (net storage), never exceed it: a heat engine between two reservoirs at fixed heat flow cannot increase the total entropy production, only match or reduce it. This is why entropy production cannot separate channels and share of flux can.
- What is selected is share of free-energy flux, subject to persistence: Lotka's 1922 principle, here with a mechanism and a window. Not maximisation: a bias that holds inside 1 ≤ q ≤ m+1 and while flux still separates channels.
- Entropy enters the *hypothesis* D ∝ J: channels that dissipate more jitter more. Where that holds, the second law's cost and the theorem's driver are the same quantity and the system sits on q = m inside the window. Where it fails, the theorem predicts no selection.

## 6. Derivation

- T1 (existing is paying). From D2 + P2 + P3: a flow pattern exists only while paying; existing and being rebuilt are one event.
- T2 (the ceiling). From T1 + P7: for a given flux, a maximum maintained negentropy. Well supported for erasure-maintained patterns; not a general theorem.
- T3 (the corridor). From P4 + T2: below threshold no pattern holds; above it, patternlessness cannot hold.
- T4 (loops are things). From D4 + D5: identity in the pattern, boundary non-arbitrary. Ship of Theseus resolved: identity lives in the loop.
- T5 (loops self-route to varying degrees, and capture). From D6.
- T6 (competition). From T2 + P5 (or copying) + P7: multiplication of fixed-intake loops alone exhausts a finite gradient. Growth (causing loops expanding at their edge) and capture add to this but are not required.
- T7 (multiplication). From P5, or from copying (iv).
- T8 (variation): rebuilding under noise guarantees it; erased in gradient-rebuilt patterns, carried in self-rebuilt.
- T8a (memory alone needs a gate): a plain relaxation-to-self only slows forgetting; persistence needs a threshold. When the write goes through the flow, the loop is its own nonlinearity and no gate is needed.
- T9 (selection): concentration and differential persistence from Theorem (i)–(iii), inside the window 1 ≤ q ≤ m+1; Darwinian selection only once copying ∝ share is added (iv), which is the bridge; reflexivity from (v).
- T10 (robust win, prediction): persisting types are noise-robust, multiply realizable.
- T10a (stasis without memory): flow alone yields a stable zoo of types, not lineages. Bénard rolls forever is this theorem.
- T11 (memory migrates to self-rebuilt patterns): only there does variation outlive one rebuild. DNA is not durable stuff; it is a flow whose maintenance step is a copy.
- T12 (the hybrid is the unit of evolution): a loop that lives, carrying a self-rebuilt pattern that is read and copied at partition under noise.
- T12a (reading is selected, not installed): any flow-to-rule channel with free sign is closed into a loop by selection.
- T13 (selection does not stop, but not by one trait): on a single scalar trait selection is self-extinguishing (at the ceiling every survivor carries a near-equal share and the flux stops distinguishing). It continues because: at the ceiling P5 forces splitting, turning competition zero-sum; causing loops that unlock held-back gradient raise the total flux and with it the ceiling (complexity ratchets by capture, bounded at each moment by T2); and the environment is the other channels, so the share landscape co-evolves and never flattens.

## 10. Darwin map

See the term map in §1. Additions not in the table: death = freezing at the floor or being overwritten; drift = the flat-noise control; genotype/phenotype = c/g in the write-back toy, self-rebuilt pattern / flow loop in the hybrid, reading is the map between them; environment = the other channels plus the fixed total. Missing from the toy: recombination; an error threshold (a single number cannot be corrupted).

## 11. Open joints and status

Open: one real system measured end to end (noise ∝ flux, m ≥ 1, concentration observed); identification of persistence-selection with reproduction-selection (argued via iv, not measured); D5 not operational; P5 not reproduced.
Proved (toy): Theorem (i)–(v). Reproduced: P4, T3, T8a, T11, T12a, boundary. Physics near equilibrium, evidenced beyond: P6a. Known math to cite: boundary ≡ nonlinear preferential attachment.

Prior art and literature check: see `docs/references.md`.

---

## Repository

- `docs/experiments.md`: what was run, what it showed, which sim.
- `docs/references.md`: prior art to cite and the literature check.
- `docs/papers.md`: the paper plan.
- `docs/entropy_ledger.md`: the full sun–Earth–space entropy ledger; three Earths (dirt, diamond, whirlpool).
- `docs/history.md`: ΛB post-mortem and distinctions kept from the working conversation.
- `sims/`: simulation code (Python, numpy; scipy for one helper).
- `figures/`: outputs referenced in docs/experiments.md.
