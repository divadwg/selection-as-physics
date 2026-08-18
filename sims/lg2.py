import numpy as np, os
from lg import cx, cy, w, opp, equilibrium, count_loops

class Sim:
    def __init__(self, Re, nx=300, ny=90, r=9, u0=0.05, linear=False, seed=0):
        nu=u0*2*r/Re; self.tau=3*nu+0.5; self.omega=1/self.tau
        self.Re,self.nx,self.ny,self.r,self.u0,self.linear=Re,nx,ny,r,u0,linear
        X,Y=np.meshgrid(np.arange(nx),np.arange(ny),indexing='ij')
        self.cxo,self.cyo=nx//5,ny//2+0.5
        self.solid=(X-self.cxo)**2+(Y-self.cyo)**2<r*r
        self.rng=np.random.default_rng(seed)
        self.f=equilibrium(np.ones((nx,ny)),np.zeros((nx,ny)),np.zeros((nx,ny)),linear)
        self.t=0; self.ts=[]; self.probe=(int(self.cxo+4*r), ny//2)
    def step(self, n, record_from=12000):
        f=self.f; ny=self.ny; omega=self.omega; solid=self.solid; linear=self.linear
        for _ in range(n):
            t=self.t
            rho=f.sum(0); ux=(cx[:,None,None]*f).sum(0)/rho; uy=(cy[:,None,None]*f).sum(0)/rho
            uin=self.u0*min(1.0,t/1000.0)
            ux[0,:]=uin*(1+1e-3*self.rng.standard_normal(ny)); uy[0,:]=0
            feq=equilibrium(rho,ux,uy,linear); f=f-omega*(f-feq)
            f[:,0,:]=equilibrium(np.ones((1,ny)),ux[0:1,:],uy[0:1,:],linear)[:,0,:]
            f[:,-1,:]=f[:,-2,:]
            fs=f[:,solid]; f[:,solid]=fs[opp]
            for i in range(9): f[i]=np.roll(np.roll(f[i],cx[i],axis=0),cy[i],axis=1)
            if t>=record_from: self.ts.append(uy[self.probe])
            self.t+=1
        self.f=f; self.ux,self.uy=ux,uy
    def result(self):
        om=np.gradient(self.uy,axis=0)-np.gradient(self.ux,axis=1); om[self.solid]=0
        xc=int(self.cxo); wake=self.ux[xc+self.r:xc+4*self.r,:]
        ts=np.array(self.ts)
        return dict(Re=self.Re,tau=self.tau,ux=self.ux,uy=self.uy,om=om,solid=self.solid,ts=ts,
                    probe_amp=float(ts.std()) if len(ts) else 0.0,linear=self.linear,
                    reversed_frac=float((wake<-0.01*self.u0).mean()),nloops=count_loops(om,self.solid))

if __name__=="__main__":
    import sys, pickle
    Re=int(sys.argv[1]); linear=sys.argv[2]=='linear'; total=int(sys.argv[3]); chunk=int(sys.argv[4])
    tag=f"{'lin' if linear else 'full'}_{Re}"; ck=f"/home/claude/ck_{tag}.pkl"
    sim=pickle.load(open(ck,'rb')) if os.path.exists(ck) else Sim(Re,linear=linear)
    n=min(chunk,total-sim.t); sim.step(n); pickle.dump(sim,open(ck,'wb'))
    if sim.t>=total:
        r=sim.result(); np.savez(f"/home/claude/res_{tag}.npz",**r)
        print(f"DONE {tag}: tau={r['tau']:.3f} amp={r['probe_amp']:.2e} loops={r['nloops']} rev={r['reversed_frac']:.3f} nan={np.isnan(r['ux']).any()}")
    else: print(f"{tag} at t={sim.t}")
