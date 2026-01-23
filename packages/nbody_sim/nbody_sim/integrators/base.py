from abc import ABC, abstractmethod
from nbody_sim.types import System

class Integrator(ABC):
    name: str

    @abstractmethod
    def step(self, system: System, dt: float) -> System:
        pass
