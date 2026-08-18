"""
Stage 2: hybrid substrate.
Flow layer : D2Q9 lattice flow, periodic in x, driven by a body force (the gradient).
Matter layer: per-cell solid fraction s in [0,1] (bed). Slow variable.
Coupling   : bed -> flow via partial bounce-back (a cell with s reflects fraction s of tokens).
             flow -> bed via erosion where speed high, transport as suspended load q, settling where slow.
Nothing tells the bed to make ripples or the flow to make loops. Both are free.
"""
import numpy as np, pickle, os, sys
cx = np.array([0, 1, 0,-1, 0, 1,-1,-1, 1]); cy = np.array([0, 0, 1, 0,-1, 1, 1,-1,-1])
w  = np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36]); opp = np.array([0,3,4,1,2,7,8,5,6])

def feq_fn(rho, ux, uy, linear=False):
    cu = 3*(cx[:,None,None]*ux + cy[:,None,None]*uy)
    if linear: return w[:,None,None]*rho*(1+cu)
    return w[:,None,None]*rho*(1+cu+0.5*cu**2-1.5*(ux**2+uy**2))

class Hyb:
    def __init__(self, nx=240, ny=64, tau=0.53, F=2.0e-6, bed=6, seed=0, linear=False,
                 uc=0.004, ke=0.3, vs=0.1, kt=80, sed_every=4, erodible=True, init='rough', bump=None):
        self.nx,self.ny,self.tau,self.F,self.linear=nx,ny,tau,F,linear
        self.omega=1/tau; self.uc,self.ke,self.vs,self.kt,self.sed_every,self.erodible=uc,ke,vs,kt,sed_every,erodible
        rng=np.random.default_rng(seed); self.rng=rng
        s=np.zeros((nx,ny)); s[:, :bed]=1.0
        if init=='rough': s[:, bed]=rng.uniform(0,0.15,nx)          # tiny random roughness on surface
        if bump is not None:                                          # single seed bump
            x0,h=bump; s[x0-2:x0+3, bed:bed+h]=1.0
        s[:, -1]=1.0                                                  # fixed top wall
        self.fixed=np.zeros((nx,ny),bool); self.fixed[:, -1]=True; self.fixed[:, :2]=True
        self.s=s; self.q=np.zeros((nx,ny))
        # start from the Poiseuille profile so we don't wait H^2/nu steps for spin-up
        nu=(tau-0.5)/3; y=np.arange(ny); y0,y1=bed-0.5,ny-1.5
        prof=np.clip(F/(2*nu)*(y-y0)*(y1-y),0,None); ux0=np.tile(prof,(nx,1))*(s<0.5)
        self.f=feq_fn(np.ones((nx,ny)),ux0,np.zeros((nx,ny)),linear)
        self.t=0; self.hist=[]
    def macro(self):
        f=self.f; rho=f.sum(0); ux=(cx[:,None,None]*f).sum(0)/rho; uy=(cy[:,None,None]*f).sum(0)/rho
        return rho,ux,uy
    def step(self,n):
        f=self.f; om=self.omega; s=self.s
        for _ in range(n):
            rho,ux,uy=self.macro()
            uxf=ux+self.tau*self.F                     # body force in +x
            feq=feq_fn(rho,uxf,uy,self.linear); f=f-om*(f-feq)
            # partial bounce-back where s>0
            m=s>0
            fb=f[:,m]; f[:,m]=(1-s[m])*fb+s[m]*fb[opp]
            for i in range(9): f[i]=np.roll(np.roll(f[i],cx[i],axis=0),cy[i],axis=1)
            self.f=f
            if self.erodible and self.t%self.sed_every==0: self.sediment(ux,uy)
            self.t+=1
        self.ux,self.uy=ux,uy
    def sediment(self,ux,uy):
        s,q=self.s,self.q; Ufl=np.hypot(ux,uy)*(1-s)
        U=np.maximum(Ufl, np.roll(Ufl,-1,axis=1))     # material feels the flow in the cell above it (surface shear)
        # erosion from cells that hold material, exposed to fast flow
        e=self.ke*np.clip(U-self.uc,0,None)*np.minimum(s,1.0); e[self.fixed]=0
        s-=e; q+=np.roll(e,1,axis=1)   # eroded material is lifted into the cell above
        # transport: suspended load moves with the flow (upwind split), fraction ~ speed
        cxs=np.clip(np.abs(ux)*self.kt,0,1); cys=np.clip(np.abs(uy)*self.kt,0,1)
        qx=q*cxs*(1-cys); qy=q*cys*(1-cxs); q-= (qx+qy)
        q+= np.roll(np.where(ux>0,qx,0),1,axis=0)+np.roll(np.where(ux<=0,qx,0),-1,axis=0)
        q+= np.roll(np.where(uy>0,qy,0),1,axis=1)+np.roll(np.where(uy<=0,qy,0),-1,axis=1)
        # gravity: load drifts down; if the cell below is (near) solid it deposits here
        below=np.roll(s,1,axis=1)                       # s at y-1
        landing=below>0.7
        drop=self.vs*q
        dep=np.where(landing,drop,0); fall=np.where(landing,0,drop)
        q-=drop; s+=dep; q+=np.roll(fall,-1,axis=1)
        # settle where flow is slow, on exposed surface
        slow=np.clip(self.uc-U,0,None)/self.uc
        d=0.5*slow*q*landing; q-=d; s+=d
        # cap
        over=np.clip(s-1,0,None); s-=over; q+=over
        s[self.fixed]=1.0; s[:, -1]=1.0
        np.clip(s,0,1,out=s)
    def bed_profile(self): return self.s[:, :-1].sum(1)
    def loops(self):
        # reversed x-flow in the fluid region above the bed = closed circulation present
        fluid=(self.s<0.5); ux=self.ux
        rev=(ux<-0.05*np.abs(ux).max())&fluid
        return float(rev.mean()), rev
    def snap(self):
        h=self.bed_profile(); h=h-h.mean()
        amp=float(h.std()); spec=np.abs(np.fft.rfft(h))**2; spec[0]=0
        k=int(np.argmax(spec[1:]))+1; lam=self.nx/k
        return dict(t=self.t,amp=amp,lam=lam,rev=self.loops()[0])

def run_chunk(tag,n,total,**kw):
    ck=f"/home/claude/hyb_{tag}.pkl"
    sim=pickle.load(open(ck,'rb')) if os.path.exists(ck) else Hyb(**kw)
    m=min(n,total-sim.t); sim.step(m); sim.hist.append(sim.snap()); pickle.dump(sim,open(ck,'wb'))
    return sim

if __name__=="__main__":
    tag=sys.argv[1]; n=int(sys.argv[2]); total=int(sys.argv[3]); kw=eval(sys.argv[4]) if len(sys.argv)>4 else {}
    sim=run_chunk(tag,n,total,**kw)
    print(tag, sim.snap(), 'done' if sim.t>=total else '')
