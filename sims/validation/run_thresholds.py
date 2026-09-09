"""A model-specific prediction: copying-cost threshold with state loss and transit.

Birth attempts b=c*g; viable transmission probability exp(-r*g**q*tau).
A failed copy leaves no viable offspring. This is an additional hypothesis about
carrier damage, not a consequence of channel diffusivity or of the noise window.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from .heredity import trait_model, Branching
from .run_heredity import write_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path('docs/heredity_results'))
    args = parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    rows, trials, raw = [], [], []
    for restoring in [0., .7]:
        for transit in [0., 10., 40.]:
            for intervals in [8,16,32]:
                g, base = trait_model(1.,restoring,intervals)
                fidelity = np.exp(-.02*g*transit)
                model = Branching(base.transition,base.birth,base.death,np.diag(fidelity))
                critical = 1/model.reproduction_radius()
                rows.append(dict(restoring=restoring,transit=transit,intervals=intervals,
                                 critical_copy_coefficient=critical,critical_cost_at_unit_funding=1/critical))
                if intervals != 8:
                    continue
                initial = int(np.argmin(abs(g-1.5)))
                for ratio in [.8,1.2]:
                    tested = Branching(base.transition,base.birth*critical*ratio,base.death,np.diag(fidelity))
                    q, residual = tested.eventual_extinction()
                    qt = tested.extinction(20.)
                    counts = dict(extinct=0,alive_at_horizon=0,censored=0)
                    for seed in range(1000):
                        status = tested.trial(initial,20.,seed)
                        counts[status] += 1
                        raw.append(dict(restoring=restoring,transit=transit,ratio_to_critical=ratio,seed=seed,outcome=status))
                    trials.append(dict(restoring=restoring,transit=transit,ratio_to_critical=ratio,
                        initial_trait=g[initial],reproduction_radius=tested.reproduction_radius(),
                        eventual_survival=1-q[initial],survival_at_20=1-qt[initial],residual=residual,
                        trials=1000,**counts))
            print(f'Threshold: restoration {restoring}, transit {transit}',flush=True)
    write_csv(args.output/'thresholds.csv',rows)
    write_csv(args.output/'threshold_checks.csv',trials)
    write_csv(args.output/'threshold_trials.csv',raw)
    reversal = []
    for intervals in [16,32,64]:
        for transit in [0.,20.,30.,40.,60.]:
            for damage in ['state_dependent','constant']:
                for restoring in [0.,.7]:
                    g, base = trait_model(1.,restoring,intervals)
                    rate = .02*g if damage == 'state_dependent' else np.full(len(g),.02)
                    model = Branching(base.transition,base.birth,base.death,np.diag(np.exp(-rate*transit)))
                    reversal.append(dict(intervals=intervals,transit=transit,damage=damage,restoring=restoring,critical_copy_coefficient=1/model.reproduction_radius()))
    write_csv(args.output/'restoration_reversal.csv',reversal)
    files = [Path(__file__),Path(__file__).with_name('heredity.py')]
    (args.output/'threshold_manifest.json').write_text(json.dumps(dict(
        carrier_damage_rate='.02*g',copy_fidelity='exp(-.02*g*transit)',
        death=.4,state_diffusion='.02*g',initial_trait=1.5,horizon=20,trials=1000,
        seeds=list(range(1000)),cap=128,dt=.005,source_sha256={
            p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n')


if __name__=='__main__':
    main()
