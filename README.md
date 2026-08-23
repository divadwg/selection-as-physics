# Natural selection as physics

*Logic summary. This README is the argument; records, references, ledger and history are in `docs/`; code in `sims/`; figures in `figures/`.*

---

## 0. The claim, plainly

Everything that persists in a flow is a pattern the flow keeps re-making. For a fixed energy input, total entropy production is set by the input, not the route: structure changes flux (inputs and routes), never entropy per joule (outputs). Order is paid for out of a degradation that was already total; entropy is produced when order degrades, not when it is created. So the currency anything can compete over is share of the flow, and the question "is natural selection physics?" becomes: under what conditions does sharing a flow, plus noise, produce Darwin's phenomenon?

The answer is one stationary law with four conditions read off it. Where all four hold, a minimal Darwinian regime follows within this model class, and both bridges are now physically derived rather than assumed: D ∝ J from extensive recruitment of independently perturbed degrees of freedom (geometry gives throughput and substrate contact from the same cause; sims/core/08-09), and b ∝ J from a copy-resource accumulator (throughput supplies work, a copy has finite cost, so b = ηJ/E_copy; derived and measured emergent, slope ≈ 90% of η/E, sims/core/18). Each bridge is a testable physical condition: growth by recruiting independent units, and work-funded copying; each condition is separately checkable, each has a failure regime, and real systems can be placed on the resulting diagram from measured exponents.

**Status in one line:** condition 2 (sorting) is a verified theorem with real-system placements; condition 1 (heredity) is demonstrated and its law owed; condition 3 (establishment) is imported physics being wired in; condition 4 (portability) has a mechanism chain and no experiment yet. Pre-copying, everything here is *sorting* (Vrba-Gould), not selection, and the write-ups say so.

## 1. The unified law and the four conditions

For a state g with re-templating v(g) and diffusivity D(g) = ½·r·σ² (event rate × kick size², both moments delivered by the same unresolved fast layers, Mori-Zwanzig): stationary occupancy

**p(g) ∝ (1/D(g)) · exp(∫v/D)**

and with share of a conserved flux ∝ g^m, flux-weighted density ∝ g^(m−q) where D ∝ g^q.

**Condition 1, heredity = weak re-templating.** Deviations must outlive the timescale on which they matter (dent-life > generation, or with copying, > waiting-time-to-copy). Fast fields fail this (whirlpool: memory of type, not of deviation; perturbations contract); slow gated stores pass it. Weismann's split falls out: soma = fast field, germline = gated store. Measured: healing kills parent-daughter excess correlation in the carved-bed world (sims/core/10); re-templating erases the inversion (sims/core/11, consistency check, near-tautological and labelled so). Owed: dent-life derived from medium physics. Non-obvious registered predictions: marginal-window systems (q ≈ 1) are most re-templating-vulnerable; copying is memory refresh, so high share extends effective heredity (fitness feeds back on heritability): CONFIRMED (sims/core/12): the climb survives re-templating that kills sorting alone, rescue scales with copy rate, and fails exactly where copy-interval approaches dent-life; with copying, concentration collapses while the mean climbs (the herd, not the hierarchy: correct Moran behaviour).
Mechanism note (gating as the v-killer): a barrier converts hidden-layer influence from (mean pull, continuous jitter) to (mean ≈ 0, rare discrete kicks). Heredity-capable media are exactly the gated ones; digital storage is the generic solution, not a biological accident.

**Condition 2, sorting = the window on D** (equivalently: a moment-divergence window for a physically generated heavy-tailed stationary distribution). Occupancy piles where jitter is least; flux sits with the few disturbed most; the two censuses separate iff **1 ≤ q ≤ m+1**, both edges marginal, and only for idiosyncratic noise (common-mode kicks select nothing: variation must differ between competitors). q is set by growth geometry: extensive growth (independent units add) gives q = m, inside the window; coherent amplification gives q = 2m, at or beyond the upper edge; demonstrated in-substrate, 1.01 and 2.00 (sims/core/09). Epistemic status upgraded on review: the hidden-layer lattice is a physical derivation of state-dependent diffusivity, not merely a consistency check. Width gives throughput and substrate contact from the same geometry (n ∝ w/ℓ, J ∝ w, so n ∝ J with no independent noise assumption); independent patches give D ∝ J (q = m, the window's lower boundary), coherent forcing gives D ∝ J² (q = 2m, the upper boundary at m = 1): the two correlation classes of the hidden layer land exactly on the window's two edges, and the exponent emerges from geometry plus correlation structure. The remaining fully-spatial measurement (width, contacted cells, throughput, disturbance all measured directly in one sim) is an additional demonstration, not a fundamental gap. A further requirement flagged for the derivation: identify the physically natural variable in which perturbations are additive and unbiased, since a nonlinear change of variables introduces noise-induced drift (the variable choice is the first thing a statistical physicist will attack). Verified by exact integration and large-N SDE (sims/core/04); demonstrated with emergent deterministic noise, no RNG (sims/core/08). Real placements from published exponents: cities q ≈ 2, GDP ≈ 1.7, firms ≈ 1.5–1.6, networks ≈ 1, all inside; suggestive rather than validating (observed Var(Δg|g) ∝ g^q can also reflect drift, births/deaths, ageing, nonstationarity, finite windows, measurement noise, and does not by itself establish the stationary diffusion model). The memristor case is stronger because g is genuinely a conductance and throughput is precise, but the relevant quantity is the state-rewriting rate, not readout noise; the parallel-filament experiment remains the decisive one (docs/memristor_q_analysis.md). Fitness here = throughput share, and becomes reproductive fitness only via the copying bridge (assumed ∝ share; flagged).

**Condition 3, establishment = R₀ > 1 while rare.** A replicator lineage survives only if each maker completes, before dying, more than one surviving copy: R₀ = copy rate × dent-life × fidelity, every factor already in the framework (copy rate ∝ share; dent-life from condition 1; fidelity under q-scaled noise). Sparks may be common and establishment rare (fizz below threshold); failed-chain-length statistics measure distance-to-threshold; cycling environments cross it episodically given storage. RESTRUCTURED by 16-17b and given its proper mathematics by review: offspring inherit the parent's stochastically evolving state, so reproductive events are correlated through inherited state and no scalar R0 captures the process. The correct object is a branching diffusion in trait space: with copying rate b(g), death rate d(g), and extinction probability Q(g) for a lineage started at g, the backward equation D·Q'' + v·Q' + b·(Q²−Q) + d·(1−Q) = 0 gives P_survive(g) = 1 − Q(g), incorporating diffusion, re-templating, inheritance, copying, death and extinction in one equation; the escape threshold seen in sims/core/16-17 should emerge from its solution rather than being a separate conceptual stage (derivation owed: solve for our b ∝ J, d from erasure, D from the window). Intuition preserved: escape first, compounding after; copying while rare = multiplied escape attempts. After escape: takeover is arithmetic (compounding beats accumulation, no further physics), then condition 2 resumes inside the replicator population: evolution proper, with Eigen's mutation window borrowed and its free parameter closed by q. Owed: R₀ derived as an explicit function of (share, dent-life, q); the R₀-instrument sim.

**Condition 4, portability = state travelling without its carrier.** Interpretation: the transition from locally inherited structure (offspring physically reproduce the parent's structure) to open-ended cumulative heredity (a separable token that can be copied, recombined, expressed in new contexts). Darwinian processes do not require the detached token, so portability is not used as the definition of life here; in plain-language pieces the phrase 'where life starts' is kept as shorthand for this transition. Mechanism chain, each link established or named: gating makes the store hold without the flow that wrote it (detachability; riverbed result); gated states are discrete, hence re-instantiable elsewhere (a carrier becomes possible); copying-as-refresh economics miniaturise the store toward the minimal gated token (toward a gene); catalysis reads by configuration, not position (a catalyst is a configuration-addressed rule, R2). Open: the rung-3 experiment (a detached gated parcel shapes flow where its parent never touched, above a distance-matched null) and the formal two-variable extension (advected state + configuration-addressed read; an R₀-for-travellers).

**Orthogonality.** Heredity without sorting: neutral wander (genetic drift = kick wander without share-coupling). Sorting without heredity: differences erased each turnover (the whirlpool zoo, sorted and going nowhere). Both needed; neither implies the other.

## 2. The heredity ladder (the physical realisation)

Rung 0, open flow: gradient re-templates everything; weather; heredity is rare in flows and must be earned. Rung 1, closed loop: heredity-in-time via the momentum term; one lineage; type-memory only. Rung 2, bifurcation: heredity across lineages iff the daughter's state is caused by the parent's state, not the environment (shedding is production, not replication; channel splitting and the turbulent cascade are replication at low fidelity); measured in the carved bed, excess +0.21 over the matched null at zero healing, gone by λ = 0.05 (sims/core/10); REFRAMED by the stricter null (17a): the signal is carved-line continuity, so at bifurcation inheritance and connectivity are one mechanism; detached transmission is rung 3's, shown there. Rung 3, externalised gated state: the record outlives the revolution, then the carrier; condition 4's territory.

## 1. The theorem in one non-living example, and where life enters

Take a rainy basin. A fixed amount of water falls each year and must leave by some set of channels: that is the conserved total. Each channel has a state, its width. Wider channels carry more water roughly in proportion: that is the share, Ohm's law for water. Every year each channel's banks are knocked about, silting or scouring. Nothing supplies these knocks from outside: they are the coarse-grained residue of layers the channel description cannot resolve, grain collisions, turbulent gusts, freeze-thaw, animal footfalls, deterministic all the way down and dice at the channel level (P6, demonstrated with no random generator anywhere in sims/core/08). The hidden layers deliver both moments of their influence at once: a fluctuating part, the kicks, undirected, whose size scales with contact and hence with flow (a wider, busier channel touches more churning substrate: variances of independent patches add, sims/core/09); and a mean part, the re-templating pull, the same unresolved physics steadily nudging every channel back toward the width the drive and geometry dictate. Kicks are the mutation; the pull is the forgetting; one source, two moments. How often a channel is kicked, times how hard squared, is its jitter (the diffusivity D); the pull is v; and whether the basin can inherit anything at all is the race between them (condition 1: a dent must outlive the pull long enough to matter).

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
- D2. *Gradient-rebuilt* vs *self-rebuilt* pattern: re-formed each instant from ambient physics, versus re-formed by reference to its own prior state. Both are flow; both replace their substance. The rebuild rule is the difference. Whirlpool: nudge it, the gradient restores the old shape. DNA: nudge a base, the next copy carries the nudge. Refined below.
- D2a. The heredity ladder, four rungs. (0) Open flow: no memory; the gradient re-templates every disturbance (weather; most flows; heredity is rare in flows and must be earned, not assumed). (1) Closed loop: heredity-in-time; each turnover templated by the previous one via the momentum term; one lineage, generations = turnovers, fidelity < 1 (the whirlpool, dying and reborn each cycle). (2) Bifurcation: heredity across lineages, iff the daughter's state is caused by the parent's state rather than by the environment. Vortex shedding is production, not replication (the obstacle templates each vortex); channel splitting and the turbulent cascade (eddies begetting eddies) are replication at low fidelity. (3) Externalised state: state moves into a slower substrate the flow reads and writes (bump, catalyst bed, DNA); fidelity decouples from the flow's turnover; the record outlives the revolution, then the carrier.
- D2b. The templating (sticking) condition: heredity survives at any rung exactly when the pattern's own state outcompetes the gradient as template for the next state. Twin of D6: self-routing is how much of your sustaining flux is your own doing; self-templating is how much of your successor's state is. Heredity emerges where self-templating crosses threshold: a measurable transition, not an added ingredient.
- Terminology ruling: pre-copying, the theorems deliver *sorting* (differential persistence, Vrba-Gould), not selection. Write-ups must say sorting until the copying bridge is explicitly in place.
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
- P6 (Noise): whatever an observer cannot resolve appears as irreducible noise in what they can (Mori-Zwanzig). Hidden below, dice above. *Demonstrated in-substrate:* a deterministic chaotic layer under the channels produces kicks that are dice to the coarse observer, with variance scaling as share² from contact alone, and concentration follows with no RNG anywhere (sims/core/08). Caveat learned there: selection needs activity-scaled variance, not unpredictability; a periodic substrate concentrates too. Mutation means blind and scaled, not uncaused.
- P6a, resolved into a classification (demonstrated in-substrate, sims/core/09): how D scales with J is set by how a channel grows. *Extensive* growth (throughput adds independent units: patches, transactions, members) gives kick variances that add, so D ∝ J, q = m, inside the window; measured emergent exponent 1.01 with footprint ∝ share at fixed per-patch coupling on a chaotic substrate. *Intensive/coherent* growth (same units, bigger amplitude, or one shared environmental signal) gives D ∝ J², q = 2m ≥ m+1, at or beyond the upper edge; measured 2.00. The exponent is not a free parameter; it is the geometry of growth, measurable per system. Additional finding: common-mode noise (perfectly correlated across channels) fails to select even at nominally in-window q, because selection requires noise that differentiates competitors; variation must be idiosyncratic. Original statement kept for history:
- P6a (original form, superseded above): the diffusivity of a channel's state in the privileged variable g scales as g^m, i.e. with its throughput. Equilibrium FDT does not give this; far from equilibrium FDT is generically violated (Harada-Sasa). Status: hypothesis to be derived or tested per system class. Evidence in the direction: transcription-associated mutagenesis; metabolic-rate scaling of molecular evolution. Also assumed: kicks additive and symmetric in g (the stochastic metric); reparameterization changes the apparent exponent.
- P6b (Transport): what a flow can move, it moves in proportion to itself.
- P7 (Finitude): every gradient is finite.
- P8 (Storage): configurations stable between copies can hold information (Schrödinger's aperiodic crystal); their role is stability between copies, not permanence.
- P9 (Description/constructor): cumulative replication needs a stored description plus a reader (von Neumann).
- P10 (Linear response): share of flux rises at least linearly with the state that carries it, m ≥ 1. Ohm, stream power, catalysis satisfy; diffusion alone does not.

## 4a. Lemma L1 (irreversible maintenance)

In the domain of D3 a pattern persists only by being rebuilt. Rebuilding against noise means the noised state is discarded and the pattern's state re-imposed; discarding a state is logically irreversible, hence carries the Landauer erasure cost per erased degree of freedom per rebuild. Therefore maintained order in this domain has a minimum dissipation rate proportional to (order held) × (rebuild rate). Landauer supplies the cost of erasure; the lemma supplies the claim that maintenance contains erasure. The second half is what must be checked per system, not assumed. Outside D3 (kinetically trapped order) the lemma does not apply and no floor is claimed.


## 6. Entropy: where it enters and where it does not

- The headline: entropy is produced when order degrades, not when it is created. Creation defers (production below the bare-gradient ceiling while order is banked); maintenance holds at the ceiling; degradation repays; the full cycle closes at the bare total. Structure is a timing device for entropy production.
- The resolving fact: everything ordered on Earth is higher entropy per joule than the sunlight that paid for it (5800 K light ~0.0002 J/K per joule; 300 K chemistry ~0.003). Order here is a rung down the ladder from sun to space, not a climb back up.
- A heat engine at fixed heat flow cannot increase total entropy production; the bare gradient is the ceiling. Structure acts on inputs and routes (albedo, unlocking, interception: the one door, and the ratchet), never on entropy per joule of output. A mill is a structured flow; it can dam the stream, not lower the sea.
- Hence the currency of competition is share of flux; dissipation is the bill, identical for all arrangements per captured joule over a full cycle. Full ledger, three Earths, fossil/Dyson objections: docs/entropy_ledger.md.
- Selection is Lotka's 1922 conjecture given a mechanism and a window: within the window, channels holding a larger share of the free-energy flux, and able to maintain themselves on it, persist and spread. A bias, not a maximisation.

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


## 11. Open items

Pencil: the four derivations are SKETCHED with assumptions flagged in docs/derivations.md (dent-life via Kramers, with the new tension that busy sites erase their own marks faster; R₀ = c·s·τ_dev·f with Eigen's parameter closed by q; invasion iff R₀ > 1 + δ·τ_gen, the zoo as the δ-phase, re-templating recurring at three scales; portability R₀ with transit factor, gating-necessity derived on paper). To be hand-checked at a blackboard before shipping; two new predictions registered at the end of that file. Sims done this cycle: copying-rescue (12, confirmed); rung-3 first pass (13); dent-life vs activity (14, scope-conditional); gated-vs-ungated transit (15, tunability distinction); R0 instrument v1 (16, correlated-fates finding, upgrade specified). All three owed sims done (17): stricter null (continuity reframe), R0 v2 (escape-race restructure), ungated-necessity (closed). Newly owed from results: p_esc first-passage derivation; the escape-surface map replacing the R0=1 surface. Contact: one system with J, r, σ² measured together (memristor array specified, docs/memristor_q_analysis.md); any biological q; the firms stationary-vs-transient exponent over time. Unexplained: P5 (why surplus makes more, not bigger: the splitting primitive). Terminology enforced: sorting until copying is explicit; re-templating, never "drift".

## Repository

- `docs/results_one_liners.md`: each experiment in one sentence with its figure.
- `docs/experiments.md`: what was run, what it showed, which script and figure.
- `docs/derivations.md`: the four derivations, sketch rigour, assumptions flagged, two new predictions.
- `docs/memristor_q_analysis.md`: q computed from measured memristor noise exponents; one physical system crosses the window.
- `docs/entropy_ledger.md`: the sun–Earth–space entropy ledger; three Earths (dirt, diamond, whirlpool).
- `docs/references.md`: prior art to cite and the literature check.
- `docs/papers.md`: the paper plan.
- `docs/history.md`: ΛB post-mortem and distinctions kept from the working conversation.
- `docs/substack_draft.md`: plain-English essay.
- `docs/animation_brief.md`: build brief for a one-world explainer animation (illustration, not evidence).
- `sims/core/`: the theorem and its checks (paper 1). `sims/boundaries/`: what linear systems cannot do (paper 2). Numbered in the order of the argument.
- `figures/core/`, `figures/boundaries/`: one figure per result, named for what it shows.
