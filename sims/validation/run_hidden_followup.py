"""Wider-range checks and ensemble bootstrap uncertainty, without refitting outcomes."""
from pathlib import Path
import hashlib
import json
import numpy as np
from .hidden_audit import heldout, predict, assess
from .run_heredity import write_csv


def sampling_radius(g, cuts, seed=1400, draws=2000):
    """95th percentile of centred CDF error, resampling whole ensembles.

    This estimates held-out sampling error only, not calibration uncertainty,
    reference integration error, time discretisation or incomplete relaxation.
    """
    rng = np.random.default_rng(seed)
    indicators = g[:, :, None] <= cuts
    occupancy = indicators.mean(axis=1)
    flow = (indicators * (g / g.sum(axis=1, keepdims=True))[:, :, None]).sum(axis=1)
    weights = rng.multinomial(len(g), np.full(len(g), 1 / len(g)), size=draws) / len(g)
    return [float(np.quantile(np.max(abs(weights @ a - a.mean(axis=0)), axis=1), .95))
            for a in [occupancy, flow]]


def main():
    out = Path('docs/hidden_audit_results')
    rows = []
    dt = 1 / 2048
    for q in [.5, 1., 1.5, 2.5]:
        tag = f'q{q}_dt{dt}'
        prediction = np.load(out / (tag + '_prediction.npz'))
        for initial in ['low', 'middle', 'high']:
            for time in [16., 32.]:
                sample = np.load(out / (tag + f'_{initial}_t{time}.npz'))
                radii = sampling_radius(sample['g'], prediction['cuts'])
                rows.append(dict(q=q, upper=3, initial=initial, time=time,
                    occupancy_sampling_radius_95=radii[0], flow_sampling_radius_95=radii[1]))
    write_csv(out / 'sampling_uncertainty.csv', rows)
    checks = []
    for q in [.5, 2.5]:
        beta = np.load(out / f'q{q}_dt{dt}_calibration.npz')['beta']
        cuts, p, f, ess = predict(beta, upper=6)
        np.savez_compressed(out / f'wide_q{q}_prediction.npz', cuts=cuts, occupancy=p, flow=f)
        for index, initial in enumerate(['low', 'high']):
            for time, g in heldout(q, dt, initial, seed=1010+index, upper=6, horizon=64).items():
                ep, ef, op, of = assess(g, cuts, p, f)
                rp, rf = sampling_radius(g, cuts)
                checks.append(dict(q=q, upper=6, dt=dt, initial=initial, time=time,
                    occupancy_cdf_error=ep, flow_cdf_error=ef,
                    occupancy_sampling_radius_95=rp, flow_sampling_radius_95=rf))
                np.savez_compressed(out / f'wide_q{q}_{initial}_t{time}.npz', g=g, occupancy=op, flow=of)
                print(checks[-1], flush=True)
    write_csv(out / 'wider_range.csv', checks)
    files = [Path(__file__), Path(__file__).with_name('hidden_audit.py')]
    (out / 'followup_manifest.json').write_text(json.dumps(dict(
        heldout_seeds=[1010,1011], bootstrap_seed=1400, bootstrap_draws=2000,
        upper=6, horizon=64, dt=dt, ensembles=256,
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}), indent=2)+'\n')


if __name__ == '__main__':
    main()
