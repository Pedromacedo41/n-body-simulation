from dataclasses import dataclass, field
from typing import Any, Dict
import numpy as np

Array = np.ndarray

@dataclass
class System:
    positions: Array      # (N, 3)
    velocities: Array     # (N, 3)
    masses: Array         # (N,)
    G: float = 1.0

    def copy(self) -> "System":
        return System(
            self.positions.copy(),
            self.velocities.copy(),
            self.masses.copy(),
            self.G,
        )

@dataclass
class ReplayMeta:
    name: str
    dt: float
    steps: int
    integrator: str
    preset: str

@dataclass
class ReplayData:
    positions: Array  # (T, N, 3)



@dataclass
class Replay:
    meta: ReplayMeta
    data: ReplayData
