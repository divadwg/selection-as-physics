"""Retain raw lifetime outcomes for the copying-clock comparison."""
from pathlib import Path
import hashlib
import json
import numpy as np
from .copy_clock import reproduction, offspring
from .run_heredity import write_csv


def main():
    out = Path('docs/copy_clock_results'); out.mkdir(parents=True, exist_ok=True)
    rows=[]
    for clock in ['accumulator', 'poisson']:
        for index,cost in enumerate([.45,.7,1.]):
            lifetime,attempts,viable=offspring(1,cost,1,.8,clock,100000,seed=100+index)
            target=reproduction(1,cost,1,.8,clock)
            rows.append(dict(clock=clock,cost=cost,work=1,loss=1,fidelity=.8,trials=len(viable),
                expected_offspring=target,observed_offspring=float(viable.mean()),
                standard_error=float(viable.std(ddof=1)/np.sqrt(len(viable))),
                expected_zero_offspring=1/(1+target),observed_zero_offspring=float((viable==0).mean()),
                critical_cost=float(np.log1p(.8) if clock=='accumulator' else .8)))
            if clock=='accumulator':assert np.all(attempts*cost <= lifetime+1e-12)
            np.savez_compressed(out/(clock+'_'+str(cost)+'.npz'),lifetime=lifetime,attempts=attempts,viable=viable)
    write_csv(out/'results.csv',rows)
    files=[Path(__file__),Path(__file__).with_name('copy_clock.py')]
    (out/'manifest.json').write_text(json.dumps(dict(seeds=[100,101,102],trials_per_case=100000,
        source_sha256={str(p.relative_to(Path(__file__).resolve().parents[2])):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n')
    for row in rows: print(row)


if __name__=='__main__':main()
