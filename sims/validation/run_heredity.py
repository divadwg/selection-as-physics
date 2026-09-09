"""Retain raw outcomes, settings and source hashes for the heredity audit."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
from .heredity import trait_model, transfer_assay, generations


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('docs/heredity_results'))
    parser.add_argument('--trials', type=int, default=1000)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    branching, raw = [], []
    for c in [.08, .22, .4]:
        for restoring in [0., .7]:
            g, model = trait_model(c, restoring)
            eventual, residual = model.eventual_extinction()
            initial = int(np.argmin(abs(g-1.5)))
            for horizon in [2., 8., 20.]:
                q = model.extinction(horizon)
                refined = model.extinction(horizon, dt=.0025)
                outcomes = dict(extinct=0, alive_at_horizon=0, censored=0)
                for seed in range(args.trials):
                    result = model.trial(initial, horizon, seed)
                    outcomes[result] += 1
                    raw.append(dict(copy_rate=c, restoring=restoring, horizon=horizon, seed=seed, outcome=result))
                branching.append(dict(copy_rate=c, restoring=restoring, horizon=horizon,
                    initial_trait=g[initial], reproduction_radius=model.reproduction_radius(),
                    survival_at_horizon=1-q[initial], eventual_survival=1-eventual[initial],
                    timestep_difference=float(max(abs(q-refined))), residual=residual,
                    trials=args.trials, **outcomes,
                    mc_survival_lower=outcomes['alive_at_horizon']/args.trials,
                    mc_survival_upper=(outcomes['alive_at_horizon']+outcomes['censored'])/args.trials))
            print(f'Lineage rates {c}, {restoring}: complete', flush=True)
    write_csv(args.output/'branching.csv', branching)
    write_csv(args.output/'branching_trials.csv', raw)
    transport, family = [], []
    for mode in ['gated', 'slow_dial', 'fast_dial']:
        for distance in [0, 10, 40, 100]:
            for seed in range(10):
                transport.append(dict(mode=mode, distance=distance, seed=seed,
                                      **transfer_assay(mode, distance, seed)))
        for control in ['faithful', 'shuffled', 'neutral']:
            for seed in range(20):
                for row in generations(mode, control, seed):
                    family.append(dict(mode=mode, control=control, seed=seed, **row))
    write_csv(args.output/'transport.csv', transport)
    write_csv(args.output/'generations.csv', family)
    files = [Path(__file__), Path(__file__).with_name('heredity.py')]
    manifest = dict(python=platform.python_version(), numpy=np.__version__, trials=args.trials,
        branching=dict(intervals=8, horizons=[2,8,20], cap=128, initial_trait=1.5,
                       diffusivity='.02*g', death=.4, dt=.005, refined_dt=.0025),
        transport=dict(samples=10000, seeds=list(range(10)), distances=[0,10,40,100],
                       flip_rate=.005, slow_decay=.005, fast_decay=.3, sigma=.1),
        generations=dict(population=256, generations=40, seeds=list(range(20)), distance=10,
                         total_flow=1, copy_cost=1, funding='pooled fixed budget'),
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    (args.output/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print('Transport and generations: complete', flush=True)


if __name__ == '__main__':
    main()
