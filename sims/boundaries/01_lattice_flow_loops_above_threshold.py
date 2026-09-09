"""Flow past a pole: repaired D2Q9 implementation of the existing experiment.

Open x boundaries are reapplied after streaming to prevent periodic wraparound.
The transverse direction is periodic. No random draws occur during evolution.
Recirculation is checked using reverse flow and frozen-field tracer returns,
not by counting vorticity patches. This is lattice Boltzmann, not molecular gas
trajectories, and the pole is supplied. It is not a heredity or reproduction test.
"""
import numpy as np
from sims.boundaries.lg import cx, cy, w, opp, equilibrium

class Sim:
    def __init__(self, Re, nx=300, ny=90, r=9, u0=0.05, linear=False, seed=0, obstacle=True):
        nu=u0*2*r/Re; self.tau=3*nu+0.5; self.omega=1/self.tau
        self.Re,self.nx,self.ny,self.r,self.u0,self.linear=Re,nx,ny,r,u0,linear
        X,Y=np.meshgrid(np.arange(nx),np.arange(ny),indexing='ij')
        self.cxo,self.cyo=nx//5,ny//2+0.5
        self.solid=(X-self.cxo)**2+(Y-self.cyo)**2<r*r
        if not obstacle: self.solid[:]=False
        self.obstacle=obstacle
        self.f=equilibrium(np.ones((nx,ny)),np.zeros((nx,ny)),np.zeros((nx,ny)),linear)
        self.t=0; self.ts=[]; self.probe=(int(self.cxo+4*r), ny//2)
    def step(self, n, record_from=12000):
        f=self.f; ny=self.ny; omega=self.omega; solid=self.solid; linear=self.linear
        for _ in range(n):
            t=self.t
            rho=f.sum(0); ux=(cx[:,None,None]*f).sum(0)/rho; uy=(cy[:,None,None]*f).sum(0)/rho
            uin=self.u0*min(1.0,t/1000.0)
            ux[0,:]=uin; uy[0,:]=0
            feq=equilibrium(rho,ux,uy,linear); f=f-omega*(f-feq)
            f[:,0,:]=equilibrium(np.ones((1,ny)),ux[0:1,:],uy[0:1,:],linear)[:,0,:]
            f[:,-1,:]=f[:,-2,:]
            fs=f[:,solid]; f[:,solid]=fs[opp]
            for i in range(9): f[i]=np.roll(np.roll(f[i],cx[i],axis=0),cy[i],axis=1)
            # Overwrite the open boundaries after streaming, removing wrapped data.
            f[:,0,:]=equilibrium(np.ones((1,ny)),np.full((1,ny),uin),np.zeros((1,ny)),linear)[:,0,:]
            f[:,-1,:]=f[:,-2,:]
            if not np.isfinite(f).all() or np.min(f.sum(0))<=0:
                raise ArithmeticError('Flow became unstable')
            if t>=record_from: self.ts.append(uy[self.probe])
            self.t+=1
        self.f=f; self.ux,self.uy=ux,uy
    def result(self):
        om=np.gradient(self.uy,axis=0)-np.gradient(self.ux,axis=1); om[self.solid]=0
        xc=int(self.cxo); wake=self.ux[xc+self.r:xc+4*self.r,:]
        ts=np.array(self.ts)
        return dict(Re=self.Re,tau=self.tau,ux=self.ux,uy=self.uy,om=om,solid=self.solid,ts=ts,
                    probe_amp=float(ts.std()) if len(ts) else 0.0,linear=self.linear,
                    reversed_frac=float((wake<-0.01*self.u0).mean()),obstacle=self.obstacle)

if __name__=="__main__":
    import argparse
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--re',type=float,default=20)
    parser.add_argument('--linear',action='store_true')
    parser.add_argument('--steps',type=int,default=12000)
    parser.add_argument('--output',type=Path,default=Path('work/pole_flow.npz'))
    args=parser.parse_args()
    sim=Sim(args.re,linear=args.linear)
    sim.step(args.steps,record_from=args.steps//2)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(args.output,**sim.result())
    print('Wake reverse-flow fraction:',sim.result()['reversed_frac'])
