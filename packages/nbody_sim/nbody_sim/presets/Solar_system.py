import numpy as np
from nbody_sim.types import System
from skyfield.api import load

BODY_MAP = {
    "sun": "Sun",
    "mercury": "Mercury",
    "venus": "Venus",
    "earth": "Earth",
    "mars": "Mars",
    "jupiter": "Jupiter Barycenter",
    "saturn": "Saturn Barycenter",
    "uranus": "Uranus Barycenter",
    "neptune": "Neptune Barycenter",
}

MASSES = {
    "sun": 1.988e30,
    "mercury": 3.301e23,
    "venus": 4.867e24,
    "earth": 5.972e24,
    "mars": 6.418e23,
    "jupiter": 1.898e27,
    "saturn": 5.683e26,
    "uranus": 8.681e25,
    "neptune": 1.024e26,
}

def Solar_system(
    name=None,
    time=(1980, 1, 1),
    G=6.674e-11 * (31557600**2) / (1.495978707e11**3),
) -> System:
    if name is None:
        name = ["sun", "earth", "mars", "venus", "jupiter", "saturn", "uranus", "neptune", "mercury"]

    ts = load.timescale()
    t = ts.utc(*time)
    planets = load("de421.bsp")

    names = [k.lower() for k in name]
    bodies = [planets[BODY_MAP[k]] for k in names]

    positions = np.array([body.at(t).position.m for body in bodies]) / 1.495978707e11
    velocities = np.array([body.at(t).velocity.km_per_s for body in bodies]) * 31557600 / 1.495978707e8
    masses = np.array([MASSES[k] for k in names])

    return System(
        positions=positions,
        velocities=velocities,
        masses=masses,
        G=G,
    )