"""Retain the binary-material construction and matched controls."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from .material import initial_material, MaterialFlow, bonds
from .construction import components
from .run_pole_flow import trace_returns
from .run_heredity import write_csv


SETTINGS = {
    'patch_0': dict(seed=0), 'patch_1': dict(seed=1), 'patch_2': dict(seed=2),
    'dispersed': dict(seed=0, dispersed=True), 'uncoupled': dict(seed=0, coupled=False),
    'low_drive': dict(seed=0, re=2), 'block_2': dict(seed=0, block=2),
    'no_cohesion': dict(seed=0, cohesive=False),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('docs/material_results'))
    parser.add_argument('--cases', nargs='+', default=list(SETTINGS), choices=list(SETTINGS))
    args = parser.parse_args(); args.output.mkdir(parents=True, exist_ok=True)
    for name in args.cases:
        settings = SETTINGS[name]; block = settings.get('block', 4)
        material = initial_material(seed=settings['seed'], block=block, dispersed=settings.get('dispersed', False))
        material.cohesive = settings.get('cohesive', True)
        initial = material.bits.copy(); initial_s = material.coarse(); count = int(initial.sum())
        flow = MaterialFlow(material, re=settings.get('re', 40), coupled=settings.get('coupled', True))
        history = []; snapshots = [initial_s]; first_u = None; first_s = None
        for batch in range(140):
            moves = material.sweep()
            assert int(material.bits.sum()) == count
            flow.step(100)
            s = material.coarse()
            labels, ids = components(s >= .5, periodic=True)
            sizes = np.bincount(labels.ravel())
            history.append(dict(step=flow.t,material_sweeps=material.t,mass=int(material.bits.sum()),
                                bonds=bonds(material.bits),accepted_exchanges=moves,
                                largest_dense_component=max((int(sizes[i]) for i in ids), default=0),
                                initial_overlap=float(np.minimum(s, initial_s).sum()/initial_s.sum())))
            if flow.t % 2000 == 0:
                snapshots.append(s.copy())
                print(name, history[-1], flush=True)
            if flow.t == 12000:
                first_u = flow.velocity()[0].copy(); first_s = s.copy()
        ux, uy = flow.velocity(); s = material.coarse()
        # Exclude any coarse material from the return test, not just dense cells.
        returning, tracks, returned = trace_returns(ux, uy, s > 0 if flow.coupled else s < 0, 36, 30.5, 6)
        result = dict(case=name, **{**settings, 'block': block}, steps=flow.t, material_sweeps=material.t,
            initial_mass=count, final_mass=int(material.bits.sum()), initial_bonds=bonds(initial),
            final_bonds=bonds(material.bits), largest_dense_component=history[-1]['largest_dense_component'],
            initial_overlap=history[-1]['initial_overlap'],
            final_material_change=float(np.abs(s-first_s).sum()/s.sum()),
            relative_field_change=float(np.max(abs(ux-first_u))/.03),
            relative_wake_change=float(np.max(abs(ux-first_u)[42:60])/.03),
            returning_tracers=returning, tracers=120,
            reverse_fraction=float((ux[42:60] < -.0003).mean()),
            rho_min=float(flow.f.sum(0).min()), rho_max=float(flow.f.sum(0).max()))
        np.savez_compressed(args.output/(name+'.npz'), initial_bits=initial, final_bits=material.bits,
                            coarse_snapshots=np.array(snapshots), ux=ux, uy=uy, fraction=s,
                            tracks=tracks, returned=returned)
        write_csv(args.output/(name+'_history.csv'), history)
        (args.output/(name+'.json')).write_text(json.dumps(result, indent=2)+'\n')
        print(result, flush=True)
    files = [Path(__file__), Path(__file__).with_name('material.py'),
             Path(__file__).with_name('construction.py'), Path(__file__).with_name('run_pole_flow.py'),
             Path(__file__).parents[1]/'boundaries/lg.py']
    (args.output/'manifest.json').write_text(json.dumps(dict(settings=SETTINGS,
        grid=[180,60], r=6, u0=.03, default_re=40, default_block=4,
        material_sweep_every_fluid_steps=100, fluid_steps=14000,
        tracer_steps=32000, tracer_dt=2, tracer_exclusion='any material occupancy',
        source_sha256={str(p.relative_to(Path(__file__).resolve().parents[2])):
                       hashlib.sha256(p.read_bytes()).hexdigest() for p in files}), indent=2)+'\n')


if __name__ == '__main__':
    main()
