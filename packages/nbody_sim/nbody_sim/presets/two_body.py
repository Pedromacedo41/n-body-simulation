import numpy as np
from nbody_sim.types import System

def two_body_circular(
    mass: float = 1.0,
    distance: float = 1.0,
    G: float = 1.0,
) -> System:
    """
    Two bodies of equal mass in circular orbit
    around their center of mass.
    """

    r = distance / 2

    positions = np.array([
        [-r, 0.0, 0.0],
        [ r, 0.0, 0.0],
    ])

    # Circular velocity
    v = np.sqrt(G * mass / (2 * r))

    velocities = np.array([
        [0.0,  v, 0.0],
        [0.0, -v, 0.0],
    ])

    masses = np.array([mass, mass])

    return System(
        positions=positions,
        velocities=velocities,
        masses=masses,
        G=G,
    )
