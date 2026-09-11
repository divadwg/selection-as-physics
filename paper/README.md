# Two working papers

David Galbraith, revised 11 September 2026.

| Paper | Main argument | Status |
|---|---|---|
| [A noise-scaling window for concentration of a shared flow](finite_noise_window.pdf) ([source](finite_noise_window.tex)) | Uniform contact activity can yield differential disturbance; an exact conserved-flow model predicts a scaling window and finite-population correction. | Theoretical prediction with bounded numerical checks. Physical applicability and priority of the complete mechanism remain to be established. |
| [From driven flow to inherited growth](flow_to_selection.pdf) ([source](flow_to_selection.tex)) | Separate physical steps, with conditional establishment predictions that depend on copying clocks and inherited-state lifetime. | Methods and research-programme draft. A common physical construction or discriminating empirical result is still needed for a stronger publication claim. |

Both drafts use established mathematics explicitly. Neither claims a new universal
law of noise or a completed first-principles derivation of biological selection.
The first paper stands independently of the second paper's copying assumptions.
The [scope note](../docs/two_paper_scope.md) states what would make each publishable
on its intended terms. The previous combined source is retained in
[the archive](../docs/paper_archive/combined_draft_2026-09-10.tex), alongside its
included section; it is historical, not a separate current manuscript.

## Build

From the repository root, with Python 3.10 or later and Tectonic:

```sh
python -m pip install -r paper/requirements.txt
python paper/make_figure_data.py
cd paper
tectonic finite_noise_window.tex
tectonic flow_to_selection.tex
```

Tectonic may download TeX packages on its first build. The first paper uses the
committed exact-formula figure. The second paper's table comes from
[retained copying-clock histories](../docs/copy_clock_results/README.md).

## Reproduce checks

```sh
python -m unittest discover -s tests
python -m sims.validation.run_validation
python -m sims.validation.run_copy_clock
```

The copying-clock runner overwrites its retained output directory. The existing
[stationary](../docs/conserved_flow_validation.md),
[deterministic contact](../docs/research_examples/README.md),
[spatial](../docs/construction_results/README.md),
[material](../docs/material_results/README.md) and
[heredity](../docs/heredity_results/README.md) notes give their own commands,
parameters and limits. The repository currently has 26 passing unit tests;
these check the specified models rather than establish physical applicability.
