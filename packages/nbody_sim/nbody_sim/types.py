from dataclasses import dataclass, field
from typing import Any, Dict
import numpy as np

Array = np.ndarray

@dataclass
class System:
    positions: Array      # (N, 3)
    velocities: Array     # (N, 3)
    masses: Array         # (N,)
    G: float = 6.674e-11 * (31557600**2) / (1.495978707e11**3)
    @property
    def state(self): # Use state for vectorial operations
        return np.stack([ self.positions,self.velocities], axis=0)

    @state.setter
    def state(self, value): #update velocities and position according to the value of state
        self.velocities = value[1]
        self.positions  = value[0]

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
    steps: int
    integrator: str
    preset: str
    dt: float = None
    duration: float = None
    alpha: float = None
    dt_max: float = None
    dt_min: float = None


@dataclass
class ReplayData:
    positions: Array  # (T, N, 3)
    times: Array = None  # (T,) — None pour anciens replays

@dataclass
class Replay:
    meta: ReplayMeta
    data: ReplayData
