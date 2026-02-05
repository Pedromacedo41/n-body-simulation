from dataclasses import dataclass, field
from typing import Any, Dict
import numpy as np

Array = np.ndarray

@dataclass
class System:
    vecteur: Array        # (N,3,2)
    positions: Array      # (N, 3)
    velocities: Array     # (N, 3)
    masses: Array         # (N,)
    G: float = 6.67*10**(-11)

    def copy(self) -> "System":
        return System(
            self.vecteur.copy(),
            self.masses.copy(),
            self.positions.copy(),
            self.velocities.copy(),
            self.G,
            
        )

@property
def positions(self):
    return vecteur[0]

@property
def velocities(self):
    return vecteur[1]

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
