"""Refine the largest-exponent case after its drift diagnostic raised a concern."""
from pathlib import Path
import hashlib
import json
import numpy as np
from .hidden_audit import calibrate, drift_bins
from .run_heredity import write_csv


def sufficient_statistics(data, dt):
    ids = data[:, 0].astype(int)
    counts, sums = [], []
    for lo, hi in zip([1, 1.5, 2, 2.5], [1.5, 2, 2.5, 3]):
        keep = (data[:, 1] >= lo) & (data[:, 1] < hi)
        counts.append(np.bincount(ids[keep], minlength=256))
        sums.append(np.bincount(ids[keep], weights=data[keep, 3] / dt, minlength=256))
    return dict(counts=np.array(counts), drift_sums=np.array(sums))


def main():
    out = Path('docs/hidden_audit_results')
    rows = []
    dt = 1 / 8192
    for seed in [310, 311]:
        data, diag = calibrate(2.5, dt, seed=seed)
        np.savez_compressed(out / f'drift_refinement_seed{seed}.npz', **sufficient_statistics(data, dt), **diag)
        rows.extend(dict(q=2.5, dt=dt, seed=seed, **row) for row in drift_bins(data, dt))
        print(rows[-4:], flush=True)
    write_csv(out / 'drift_refinement.csv', rows)
    files = [Path(__file__), Path(__file__).with_name('hidden_audit.py')]
    (out / 'drift_refinement_manifest.json').write_text(json.dumps(dict(
        q=2.5, dt=dt, seeds=[310,311], burn=4, duration=4, ensembles_per_seed=256,
        sampling_stride=32, selected_after_inspecting_initial_drift=True,
        retained_data="Per-ensemble counts and sums in each drift bin; sufficient to reconstruct reported drift and cluster standard errors.",
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}), indent=2)+'\n')


if __name__ == '__main__':
    main()
