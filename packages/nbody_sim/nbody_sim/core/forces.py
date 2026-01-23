from nbody_sim.types import System
import numpy as np

def gravitational_forces(system: System) -> np.ndarray:
    pos = system.positions
    m = system.masses
    n = len(m)

    forces = np.zeros_like(pos)

    for i in range(n):
        r = pos - pos[i]
        dist = np.linalg.norm(r, axis=1) + 1e-9
        mask = dist > 0

        forces[i] = system.G * np.sum(
            (m[mask, None] * r[mask]) / dist[mask, None]**3,
            axis=0
        )

    return forces
