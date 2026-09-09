"""Recheck the existing pole experiment with steady-flow and tracer controls."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from .run_heredity import write_csv


def load_sim():
    source=Path(__file__).resolve().parents[1]/'boundaries/01_lattice_flow_loops_above_threshold.py'
    spec=importlib.util.spec_from_file_location('pole',source)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.Sim,source


def trace_returns(ux,uy,solid,xc,yc,r,steps=32000,dt=2.):
    """Numerical return in a frozen velocity field, not proof of time-dependent trapping."""
    x,y=np.meshgrid(np.linspace(xc+r+1,xc+4*r,10),np.linspace(yc-r,yc+r,12))
    x=x.ravel();y=y.ravel();x0=x.copy();y0=y.copy();angle=np.zeros(len(x));path=np.zeros(len(x))
    valid=np.ones(len(x),bool);returned=np.zeros(len(x),bool);previous=None
    tracks=[]
    for t in range(steps):
        valid &= (x>=0)&(x<ux.shape[0]-1)&(y>=0)&(y<ux.shape[1]-1)
        xi=np.clip(x.astype(int),0,ux.shape[0]-2);yi=np.clip(y.astype(int),0,ux.shape[1]-2)
        valid &= ~solid[xi,yi]
        a=x-xi;b=y-yi
        def sample(f):return (1-a)*(1-b)*f[xi,yi]+a*(1-b)*f[xi+1,yi]+(1-a)*b*f[xi,yi+1]+a*b*f[xi+1,yi+1]
        vx=sample(ux);vy=sample(uy);speed=np.hypot(vx,vy);valid &= speed>1e-8
        direction=np.arctan2(vy,vx)
        if previous is not None:angle+=np.where(valid,np.angle(np.exp(1j*(direction-previous))),0)
        previous=direction
        path+=np.where(valid,speed*dt,0)
        x+=np.where(valid,vx*dt,0);y+=np.where(valid,vy*dt,0)
        returned |= valid&(abs(angle)>2*np.pi)&(path>2*r)&(np.hypot(x-x0,y-y0)<1.)
        if t%100==0:tracks.append(np.column_stack([x.copy(),y.copy()]))
    return int(returned.sum()),np.array(tracks),returned


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path('docs/construction_results'))
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    Sim,source=load_sim();rows=[]
    settings=[(2,False,True,180,60,6),(20,False,True,180,60,6),
              (20,True,True,180,60,6),(20,False,False,180,60,6),
              (20,False,True,240,80,8),
              (40,False,True,180,60,6),(40,True,True,180,60,6),
              (40,False,True,240,80,8)]
    for re,linear,obstacle,nx,ny,r in settings:
        sim=Sim(re,nx=nx,ny=ny,r=r,u0=.03,linear=linear,obstacle=obstacle)
        # Comparable numbers of obstacle advection times on both grids.
        total=int(12000*r/6);sim.step(total,record_from=total//2)
        first=sim.ux.copy();sim.step(int(2000*r/6),record_from=total//2)
        result=sim.result();count,tracks,returned=trace_returns(sim.ux,sim.uy,sim.solid,sim.cxo,sim.cyo,r)
        tag=f'pole_Re{re}_linear{linear}_obstacle{obstacle}_r{r}'
        np.savez_compressed(args.output/(tag+'.npz'),**result,tracks=tracks,returned=returned)
        rows.append(dict(Re=re,linear=linear,obstacle=obstacle,nx=nx,ny=ny,r=r,steps=sim.t,
            tau=sim.tau,reverse_fraction=result['reversed_frac'],probe_std=result['probe_amp'],
            relative_field_change=float(np.max(abs(sim.ux-first))/.03),returning_tracers=count,tracers=120,
            rho_min=float(sim.f.sum(0).min()),rho_max=float(sim.f.sum(0).max())))
        print(tag,rows[-1],flush=True)
    write_csv(args.output/'pole_flow.csv',rows)
    files=[source,source.with_name('lg.py'),Path(__file__)]
    (args.output/'pole_manifest.json').write_text(json.dumps(dict(settings=settings,u0=.03,
        total_steps='14000*r/6',tracer_steps=32000,tracer_dt=2,return_radius=1,
        minimum_turn=2*np.pi,minimum_path='2*r',boundary='open x, periodic y',
        source_sha256={str(p.relative_to(Path(__file__).resolve().parents[2])):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n')


if __name__=='__main__':main()
