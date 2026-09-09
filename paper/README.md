# Paper draft

[Read the paper (PDF)](finite_noise_window.pdf). The editable source is
[finite_noise_window.tex](finite_noise_window.tex).

**A finite noise window for concentration of a shared flow: deterministic
disturbance and steps toward selection**, David Galbraith, revised 9 September 2026.
This is a working paper, not a peer-reviewed publication. The
originality of the full model and correction has not been established by a
comprehensive literature review. Known results for power laws and deterministic
effective noise do not by themselves establish that the combined physical
proposal has already been demonstrated.

The concise manuscript distinguishes channel formation, sorting, persistent flow
patterns, reproduction with inherited differences, and portable information. Its
main mathematical result concerns sorting. The existing pole-and-lattice model
is the simple example of a flow responding to a persistent irregularity.

Detailed [spatial checks](../docs/construction_results/README.md),
[heredity audits](../docs/heredity_audit.md) and
[secondary threshold predictions](../docs/heredity_results/README.md) stay in the
repository. The longer previous discussion is archived in
[the expanded section](../docs/thought_experiments_expanded_2026-09-09.tex).
The models demonstrate separate possibilities and conditional consequences;
they do not yet establish the complete physical connection.

The upper threshold is presented as an application of established moment
mathematics. The draft does not claim discovery of a new power-law threshold or
empirical confirmation of its physical interpretation.

## Build

From the repository root, using Python 3.10 or later and Tectonic:

```sh
python -m pip install -r paper/requirements.txt
python paper/make_figure_data.py
cd paper
tectonic finite_noise_window.tex
```

Tectonic may download TeX packages on its first build. ReportLab draws the vector
figure from the exact formula. The committed CSV and PDFs let readers inspect
the paper without installing a build environment. Figure 1 plots exact formula
evaluations; it does not claim simulations at large state ranges.

## Reproduce the underlying checks

From the repository root:

```sh
python -m unittest discover -s tests -v
python -m sims.validation.run_validation
python -m sims.validation.run_validation --intervals 8 --output docs/validation_results/finer_grid
python -m sims.validation.run_validation --channels 40 --intervals 8 --output docs/validation_results/forty_channels
```

The runner overwrites results in the selected output directory. Use a different
`--output` directory to preserve the retained runs. Validation details and limits
are in [the model note](../docs/conserved_flow_validation.md); the paper's numerical
table comes from the three [retained runs](../docs/validation_results/README.md),
whose underlying implementation was committed as `e802c6f`.
