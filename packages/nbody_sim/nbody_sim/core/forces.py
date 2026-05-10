from nbody_sim.types import System
import numpy as np

def gravitational_forces(system: System) -> np.ndarray:
    #use vector to optimize
    pos = system.positions  # (N, 3)
    m = system.masses       # (N,)
    r = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    dist = np.linalg.norm(r, axis=2)
    np.fill_diagonal(dist, 1.0)
    acc = system.G * m[np.newaxis, :, np.newaxis] * r / dist[:, :, np.newaxis]**3
    np.fill_diagonal(dist, 0.0)
    mask = (dist == 0)
    acc[mask] = 0.0
    return acc.sum(axis=1)
