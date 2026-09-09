"""Retain spatial construction checks and their numerical controls."""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
from .construction import landscape,gray_scott
from .run_heredity import write_csv


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path('docs/construction_results'))
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    rows=[]
    for exponent in [0.,.5]:
        for seed in range(5):
            initial,z,q,records=landscape(exponent,seed)
            rows += [dict(exponent=exponent,seed=seed,**r) for r in records]
            if seed==0:
                np.savez_compressed(args.output/f'landscape_{exponent}.npz',initial=initial,elevation=z,flow=q)
    write_csv(args.output/'landscape.csv',rows)
    print('Landscape checks complete',flush=True)
    rows=[]
    settings=[('seeded',1.,1.,seed,96.) for seed in range(3)]
    settings += [(mode,1.,1.,0,96.) for mode in ['unseeded','small_noise','no_reaction','no_feed']]
    settings += [('seeded',1.,.5,0,96.),('seeded',.5,.25,0,96.),('seeded',1.,1.,0,144.)]
    for mode,dx,dt,seed,size in settings:
        records,snaps=gray_scott(seed=seed,dx=dx,dt=dt,size=size,mode=mode)
        rows += [dict(mode=mode,dx=dx,dt=dt,seed=seed,size=size,**r) for r in records]
        tag=f'{mode}_dx{dx}_dt{dt}_seed{seed}_size{size}'
        np.savez_compressed(args.output/(tag+'.npz'),**snaps)
        print(tag,records[-1]['spots_0.2'],flush=True)
    write_csv(args.output/'reaction_diffusion.csv',rows)
    files=[Path(__file__),Path(__file__).with_name('construction.py')]
    manifest=dict(python=platform.python_version(),numpy=np.__version__,
        landscape=dict(n=48,steps=600,seeds=list(range(5)),rain_total=1,exponents=[0,.5],
            initial_slope=.04,initial_roughness=.003,base_erosion=.03,maximum_fractional_drop=.25),
        reaction_diffusion=dict(feed=.03,kill=.062,Du=.16,Dv=.08,duration=4000,
            initial_radius=5,initial_u=.5,initial_v=.25,initial_noise=.01,
            settings=settings,thresholds=[.15,.2,.25],minimum_spot_area=5,boundary='periodic'),
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    (args.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__=='__main__':main()
