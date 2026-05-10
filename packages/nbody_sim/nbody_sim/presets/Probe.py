import numpy as np
from nbody_sim.types import System
from skyfield.api import load
from skyfield.framelib import ecliptic_J2000_frame
from nbody_sim.presets.Solar_system import BODY_DISPLAY

BODY_MAP = {
    "sun": "Sun",
    "mercury": "Mercury Barycenter",
    "venus": "Venus Barycenter",
    "earth": "Earth Barycenter",
    "mars": "Mars Barycenter",
    "jupiter": "Jupiter Barycenter",
    "saturn": "Saturn Barycenter",
    "uranus": "Uranus Barycenter",
    "neptune": "Neptune Barycenter",
}
#Time in TDB
Departure_time = {
    "Voyager1": 2443392.082921099,
    "Voyager2": 2443376.147594711,
    "New_Horizon": 2453755.333333333,
    "Messenger": 2453220.833333333,
    "Cassini": 2450736.916666667,
    "Rosetta": 2453066.916666667 ,
}
# Units: km-s 


Initial_state = {
    "Voyager1": np.array([[1.447289329190070e+08, -4.424029803569365e+07, -1.103055189367570e+04],
                 [1.621225177117242e+01, 4.048629375968122e+01, 8.055511810827731e-01]]) ,
    "Voyager2": np.array([[1.284217712795806e+08, -8.128714645786889e+07, -1.046506872986257e+04],
                          [2.169464837750677e+01, 3.697902911583400e+01, 5.268110990850753e+00]]),
    "New_Horizon": np.array([[-7.199377531660764e+07, 1.284234129934585e+08, -2.466356942029297e+04],
                            [-3.869441366080978e+01,-2.170079967368258E+01, 4.554003508899855E-01]]),
    "Messenger": np.array([[1.007036310558317e+08, -1.143210966815167e+08, 6.978482902571559e+03],
                          [2.352225420766961e+01, 1.583410807020548e+01, 5.675299008992395E+00]]),
    "Cassini": np.array([[ 1.370334461031973e+08, 5.677101731151015e+07, 2.942095853897184e+04],
                        [-5.695471605701647e+00, 2.321188607301631e+01, 8.858620486573923e-01]]),
    "Rosetta": np.array([[-1.405592638508469e+08, 4.516318810087898e+07,-4.464647830955684e+03],
                        [-2.754117517785368e+00, -3.173088890467699e+01, 1.321650044677128e+00]])
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

def Probe(
    departure_time,
    initial_state,
    name=None,
    probe_mass=0 ,
    G=6.674e-11 * (31557600**2) / (1.495978707e11**3)
    ) -> System:

    if name is None:
        name = ["sun", "earth", "mars", "venus", "mercury", "jupiter", "saturn", "uranus", "neptune"]

    ts = load.timescale()
    t = ts.tdb_jd(departure_time)
    planets = load("de440.bsp")

    names = [k.lower() for k in name]
    bodies = [planets[BODY_MAP[k]] for k in names]

    positions = np.array([body.at(t).frame_xyz(ecliptic_J2000_frame).m for body in bodies]) / 1.495978707e11
    velocities = np.array([body.at(t).frame_xyz_and_velocity(ecliptic_J2000_frame)[1].km_per_s for body in bodies]) * 31557600 / 1.495978707e8
    masses = np.array([MASSES[k] for k in names])

    positions = np.vstack([positions, initial_state[0]/ 1.495978707e8]) 
    velocities = np.vstack([velocities, initial_state[1]* 31557600 / 1.495978707e8])
    masses=np.append(masses, probe_mass)
    return System(
        positions=positions,
        velocities=velocities,
        masses=masses,
        G=G,
        body_display=[BODY_DISPLAY.get(n, BODY_DISPLAY["probe"]) for n in names] + [{"name": "Voyager 1", "color": "#FF4444", "size": 0.02}],
    )



def Voyager1() -> System:
    return Probe(Departure_time["Voyager1"],
    Initial_state["Voyager1"],
    probe_mass=721.9,
    name = ["sun", "earth","venus", "mars", "jupiter", "saturn", "uranus", "neptune"])




