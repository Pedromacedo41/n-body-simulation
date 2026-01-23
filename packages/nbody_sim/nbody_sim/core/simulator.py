
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System

class Simulator:
    def __init__(self, system: System, integrator: Integrator):
        self.system = system
        self.integrator = integrator

    def step(self, dt: float):
        self.system = self.integrator.step(self.system, dt)
        return self.system

    def run_iter(self, dt: float, steps: int):
        for step in range(steps):
            yield step, self.step(dt)



