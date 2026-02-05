from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System

class Euler(Integrator):
    name = "euler"

    def step(self, system: System, dt: float) -> System:
        a = gravitational_forces(system)
            
        system.vecteur[1] += a * dt
        system.vecteur[0] += system.vecteur[0] * dt
        print(system.vecteur[0])
        print(system.vecteur)
        return system
