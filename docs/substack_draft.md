# I had the entropy question backwards. Here is what natural selection is actually made of.

For most of my adult life I have been circling one question: is natural selection a fact about biology, or a fact about physics that biology happens to exhibit? I wrote an essay on it in 2008, another in 2023, and last year a computational paper that was, in hindsight, a mess. This year, over several long working sessions, the mess got taken apart and rebuilt from the bottom, and what came out is smaller, sharper, and different from what I expected. Part of what changed is that I had a basic piece of thermodynamics wrong, in the same way I think most people who love this topic have it wrong. So this is partly a confession and partly a result.

## The intuition, and why it is wrong

Here is the story everyone tells. Life is order. The second law says disorder must increase. So life must be paying for its order by producing extra disorder somewhere, and the more order life builds, the more entropy it must be pumping out. From there it is one step to a principle: maybe systems evolve to maximise entropy production, and living things are just the universe's most efficient way of turning sunlight into waste heat.

I believed a version of that. It is elegant. It is also wrong, and the way it is wrong is instructive.

Take one square metre of Earth. About 240 watts of sunlight are absorbed on it, averaged over day and night. Those watts arrive as high quality light from a 5800 degree sun and leave as low quality infrared at about minus 18 Celsius, the temperature at which Earth radiates to space. That fall, from hot light to cold light, is a fixed amount of entropy production per second. Call it sigma. Now ask: what determines sigma? Only two things. How much power comes in, and the temperature it leaves at. And the leaving temperature is not a free choice. It is set by the requirement that out equals in. Absorb 240 watts and you must radiate 240 watts, and a body radiating 240 watts per square metre is at minus 18. That is just the physics of glowing.

Now put life on the square metre. A leaf catches a photon that would have hit rock. The photon's energy goes into sugar, then into an animal, then into soil, then into heat. Every step is a partial degradation. But at the end of the chain the same 240 watts leave as the same minus 18 degree infrared. Entropy in: unchanged. Entropy out: unchanged. Sigma: unchanged. What life did was change where inside the square metre the degradation happens, and over what time. The rock did it all at the surface in an instant. The forest does some in the leaf, some in the deer, some in the fungus, over years. Same total.

I found this hard to accept and had to write the ledger out several times before it stuck, so let me give you the version that finally worked for me.

## Three Earths

Imagine three planets, all absorbing the same 240 watts per square metre, all radiating at minus 18.

The first is made of dirt. High entropy, nothing interesting. Sunlight thermalises at the surface. Entropy production sigma, all at the surface, every second.

The second is a single giant diamond. Extraordinarily low entropy, a perfect crystal the size of a world. Sunlight thermalises at the surface exactly as on the dirt. Entropy production sigma, all at the surface. The diamond's low entropy is a state, paid for once when it formed, and it costs nothing per second because a diamond does not decay on any timescale that matters. So the diamond planet has vastly lower entropy than the dirt planet and exactly the same entropy production. Low entropy and low entropy production are simply different things.

The third is a giant sustained whirlpool, driven by the sunlight, made of nothing but flow. It has no trapped order at all. Its low entropy is a standing pattern that decays continuously and is rebuilt continuously out of the absorbed 240 watts. Every second some of its order is lost to friction and every second the flow re-imposes it, dumping the disorder as heat. Its entropy per second: minus something, plus the same something, net zero. Its entropy production: still sigma, spread through the vortex over its turnover time rather than dumped at the surface. What is different about the whirlpool planet is not the total. It is that this arrangement has a running cost, and the running cost is paid out of the flux. You can only have as much whirlpool as 240 watts will keep spinning.

Three planets, three wildly different entropies, one entropy production. And the third one is the only one that has to earn its order every second, which turns out to be the only one where anything like selection can happen.

## The heat engine argument

If you want it in one line: a heat engine placed between a hot reservoir and a cold one, with a fixed heat flow between them, cannot increase the total entropy production. It can only match it, by wasting everything, or fall below it, by extracting work and storing or exporting order. The bare gradient, with nothing in the middle, is already the maximum. Earth is a heat engine between the sun and space. Life is the working fluid. Nothing life does at fixed inflow can push the total above what dead rock already achieves.

So the compensation for local order, which the second law does require, is real, but it is not extra. It is drawn from a budget that was already being spent in full. A leaf pays for its order by degrading light that would have been degraded on the rock. It moved the spending; it did not raise it.

I want to be careful here, because there is one door out of the fixed budget, and it matters. Structure can change how much comes in. A dark forest on pale ground absorbs light that would have been reflected, so absorbed power rises and sigma rises with it. Fire spreading into fresh fuel unlocks a gradient that would have sat dormant. In our terms, structure acts on inputs and routes. It cannot act on outputs, because outputs are pinned by where the flow ends up, the sea, or space at minus 18. A mill is a structured flow. It can dam the stream and deepen the channel. It cannot lower the sea.

## Why this fixes what selection is made of

Once you see that entropy production is a property of the gradient, the same for every arrangement of channels on it, you see that it cannot be what selection sorts by. Selection can only act on what differs between competitors, and total dissipation does not. What differs is share: how much of the flow passes through this channel rather than that one. And that turned out to be enough.

Here is the mechanism, in a picture that has no biology in it.

A basin with fixed rainfall. Many channels carry the water out. Each channel has a width, and wider channels carry more water, roughly in proportion. Every year each channel's banks get knocked about at random, silting or scouring, and a channel carrying more water gets disturbed more often. Now count two things.

Count channels, and over time most are narrow. A channel that silts up carries little, is rarely disturbed, and stays as it is. The population drifts to where it is least disturbed. This is a result Rolf Landauer proved in 1975, sometimes called the blowtorch theorem, and it is all he claimed: where things pile up is set by the noise along the way, not by how good the destinations are.

Count water, and it is carried by the few wide channels, because share follows width and the wide ones, however few, are still wide. Population says trickles. Water says a handful of rivers. The two counts disagree, and they disagree more and more over time, as long as the disturbance grows at least in proportion to width.

That disagreement is the shape Darwin described: many are born, a few carry the future, and the few are not a random sample. And here it appears with nothing alive, from a fixed flow, undirected noise, and one physical premise, that busier channels are disturbed more. Fitness is nothing but share of the flow.

Then two more steps, still without biology. Let a channel wider than its stable size split, each branch inheriting its parent's cross-section, or let a wide channel erode into its neighbour's catchment and take its water. Both are copying at a rate that rises with share, and both make the basin's channels widen on average over the years. That is descent with modification, and it is Price's equation with nothing alive. And if a channel's own flow can rewrite its width, then among the channels whose flow scours them wider and the channels whose flow silts them narrower, the first kind takes over. Nobody told it to. Reading, in the sense of a channel consulting a state it wrote itself, is what selection does to any feedback whose sign is free.

We built all of this as small simulations, forty channels at a time, and each step behaved as the argument said. Then someone with a sharper mathematical eye than mine went through it and found that the result is cleaner than a single boundary. What matters is not how often a channel is disturbed but how much it jitters, which is how often times how hard. Selection happens inside a window: the jitter must grow at least in proportion to the state, and not more than one power faster than the flow does. Too little state-dependent noise and nothing concentrates. Too much, and the high states are emptied so thoroughly that even the flow ends up down low. That is a two-sided phase diagram with two ways to be wrong, and both are testable in a real system by measuring three things separately: how flow depends on state, how disturbance frequency depends on state, and how disturbance size does. It reproduces two known results, Zipf's law for cities and the power laws of growing networks, and makes a nearly right quantitative call on firm sizes, with a specific residual to chase.

## Where life starts

Rivers can do almost all of it. What rivers cannot do is carry width as a number. A channel's state travels only with the channel, by splitting or conquest. It cannot be handed to a different channel, stored, varied, and handed on again. Grass does that: a tuft drops seed, and the seed carries the root plan without carrying the root. The state has become portable, and once it is portable it accumulates. Not just a few wide channels, but a basin whose channels are wider than any parent, generation on generation.

That single row is where the theory says life begins. Not at metabolism, not at reproduction, both of which a river manages after its fashion, but at the point where a channel's state can travel without the channel. And notice that this row is not needed for selection. Concentration, the disagreement between the two counts, and even the population-wide climb by splitting and capture, all happen without it. Portable state is what selection produces when there is something that can carry a state away from its carrier.

## What I got wrong, precisely

I thought life was on the output side of the ledger, that it existed to degrade energy faster and that evolution's arrow was toward more dissipation. It is on the input side. Life takes share of a flow that was going to be degraded anyway, pays its rent from that share, and competes for more of it. Total dissipation on a fixed gradient does not move; what moves is who is in the way of the flow, and how much of the leak they have taken. Complexity rises not because complexity is dissipative but because capturing share buys structure and structure captures more share, until the leak is gone or the gradient fails, and then it stops, or reverses. Life is invisible in the planet's entropy budget and loud in its spectrum. That is a decent summary of the whole thing.

Is this natural selection as physics? In the smallest systems that can carry it, yes, provably. The window is a theorem, checked. Whether biology sits inside the window is a measurement nobody has made, and it needs a system where you can weigh flow, disturbance rate and disturbance size against each other. Until then the honest sentence is that selection is a theorem of non-equilibrium physics with a stated boundary, and that the currency of that theorem is share of the flow, not the heat. I spent fifteen years looking on the wrong side of the ledger. The right side was the sea the river cannot lower, and the mills fighting for what runs past.

*The full logic, the code, and the entropy ledger are on GitHub. Corrections welcome, especially from people who can measure jitter.*
