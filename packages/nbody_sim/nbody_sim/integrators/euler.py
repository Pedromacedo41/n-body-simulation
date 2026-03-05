from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System

#Semi-implicit Euler
class Euler(Integrator):
    name = "euler"

    def step(self, system: System, dt: float) -> System:
        a = gravitational_forces(system)
        new_state = system.state.copy()
        new_state[1] += a * dt
        new_state[0] += new_state[1] * dt
        system.state = new_state
        return system
