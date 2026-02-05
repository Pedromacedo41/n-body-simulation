from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System


class RK4(Integrator):
    name = "RK4"
    a1: Array      # (N, 3)
    a2: Array      # (N, 3)
    a3: Array      # (N, 3)
    def step(self, system: System, dt: float) -> System:
        initial_position = system.positions
        initial_velocities= system.velocities
        a0 = gravitational_forces(system)/system.masses
        
        system.velocities += a * dt/2
        system.positions += system.velocities * dt/2
        return system
    def step(self, system: System, dt: float) -> System:
        a = gravitational_forces(system)
        system.velocities += a * dt
        system.positions += system.velocities * dt
        return system