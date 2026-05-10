from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System
import numpy as np

class leap_frog(Integrator):
    #They are two step for one incrementation
    #ai=f(xi) ; xi+1=xi + vi*dt + ai * (dt**2)/2;
    #ai+1=f(xi+1) ; vi+1=( ai+a(i+1) )*dt/2
    name = "leap_frog"

    def __init__(self):
        self.a0 = None  
    def step(self, system: System, dt: float) -> System:
        if self.a0 is None:
            self.a0 = gravitational_forces(system)
        #Compute xi+1
        new_state = system.state.copy()
        new_state[0]+= new_state[1]*dt + self.a0*(dt**2)/2
        #Compute ai+1
        system.state = new_state
        a1 = gravitational_forces(system)
        #compute vi+1
        new_state[1] += (a1+self.a0)*dt/2
        self.a0 = a1
        return system
