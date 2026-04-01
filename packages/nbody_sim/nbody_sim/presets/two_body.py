import numpy as np
from nbody_sim.types import System

def two_body_circular(
    mass: float = 1.989e30,
    distance: float = 1.0,
    G: float = 6.674e-11 * (31557600**2) / (1.496e11**3),#with kg,UA,yr,
) -> System:
    """
    Two bodies of equal mass in circular orbit
    around their center of mass.
    """

    r = distance/2

    positions = np.array([
        [-r, 0.0, 0.0],
        [ r, 0.0, 0.0],
    ])

    # Circular velocity
    v = np.sqrt(G * mass / (4 * r))
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
