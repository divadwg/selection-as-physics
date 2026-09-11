"""Retain a pilot comparison to the continuous stationary marginal laws."""
from pathlib import Path
import hashlib,json
import numpy as np
from .hidden_map import simulate
from .run_heredity import write_csv


def cdf_power(g,exponent,upper):
    a=exponent+1
    return np.log(g)/np.log(upper) if abs(a)<1e-12 else np.expm1(a*np.log(g))/np.expm1(a*np.log(upper))


def main():
    out=Path('docs/hidden_map_results');out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for q in [.5,1.5,2.5]:
        for dt in [1/128,1/512]:
            for seed in [0,1]:
                snapshots,corr=simulate(q,dt,seed=seed)
                np.savez_compressed(out/f'q{q}_dt{dt}_seed{seed}.npz',**{f't{t}':g for t,g in snapshots.items()})
                for t,g in snapshots.items():
                    cut=np.linspace(1,3,101)
                    base=cdf_power(cut,-q,3);flow=cdf_power(cut,1-q,3)
                    occupancy=7/8*base+flow/8
                    observed_p=np.array([(g<=a).mean() for a in cut])
                    share=g/g.sum(axis=1,keepdims=True)
                    observed_f=np.array([(share*(g<=a)).sum(axis=1).mean() for a in cut])
                    rows.append(dict(q=q,dt=dt,seed=seed,time=t,replicas=len(g),
                        occupancy_cdf_error=float(np.max(abs(observed_p-occupancy))),
                        flow_cdf_error=float(np.max(abs(observed_f-flow))),
                        lag_one_driver_product=corr))
                print(rows[-1],flush=True)
    write_csv(out/'results.csv',rows)
    files=[Path(__file__),Path(__file__).with_name('hidden_map.py')]
    (out/'manifest.json').write_text(json.dumps(dict(n=8,m=1,upper=3,horizon=16,replicas=512,
        seeds=[0,1],q=[.5,1.5,2.5],dt=[1/128,1/512],initial_g=2,
        source_sha256={str(p.relative_to(Path(__file__).resolve().parents[2])):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n')


if __name__=='__main__':main()
