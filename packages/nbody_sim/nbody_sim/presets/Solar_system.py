import numpy as np
from nbody_sim.types import System
from skyfield.api import load

def Solar_system(name =["sun","earth","moon"], 
                 time:tuple = (1980,1,1),
                 G: float = 6.674*(10**-11),
                ) -> System:

    ts = load.timescale()
    t = ts.utc(*time)
    Planets = load('de421.bsp')
    Body = [Planets[k] for k in name]
    positions=np.array([body.at(t).position.m for body in Body])
    velocities=np.array([body.at(t).velocity.km_per_s/1000 for body in Body])

    MASSES = {
    "sun":     1.988e30,
    "earth":   5.972e24,
    "moon":    7.35e22,
    "mars":    6.418e23,
    "venus":   4.867e24,
    "jupiter": 1.898e27,
    "saturn":  5.683e26,
    "mercury": 3.301e23,
    "uranus":  8.681e25,
    "neptune": 1.024e26,}

    masses = np.array([MASSES[k] for k in name])
    return System(
        positions=positions,
        velocities=velocities,
        masses=masses,
        G=G,
    )