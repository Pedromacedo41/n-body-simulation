from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System
import numpy as np

class RK4(Integrator):
    name = "RK4"

    def step(self, system: System, dt: float) -> System:
        a0 = gravitational_forces(system)
        #Caculus f0
        original_state = system.state.copy()
        f0=np.array([original_state[1],a0])
        #Calculus f1
        new_state = original_state + f0* dt/2
        system.state = new_state
        a1 = gravitational_forces(system)
        f1=np.array([new_state[1],a1])
        #Calculus f2
        new_state = original_state +  f1* dt/2
        system.state = new_state
        a2 = gravitational_forces(system)
        f2=np.array([new_state[1],a2])
        #Calculus f3
        new_state= original_state + f2 * dt
        system.state = new_state
        a3 = gravitational_forces(system)
        f3=np.array([new_state[1],a3])
        #Caculus X(t+dt)
        new_state = original_state+ dt*(f0+2*f1+2*f2+f3)/6
        system.state = new_state
        return system
