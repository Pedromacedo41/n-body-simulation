from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System


class Euler(Integrator):
    name = "euler"

    def step(self, system: System, dt: float) -> System:
        a = gravitational_forces(system)
        system.velocities += a * dt
        system.positions += system.velocities * dt
        return system
