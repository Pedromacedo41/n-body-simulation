import numpy as np
from nbody_sim.types import System
from skyfield.api import load
from skyfield.framelib import ecliptic_J2000_frame
from nbody_sim.presets.Solar_system import BODY_DISPLAY


SPK_FILES = {
    "default": "de440.bsp",
    "jupiter_satellites": "jup365.bsp",  # Io, Europa, Ganymède, Callisto, Amalthée
    "saturn_satellites": "sat441.bsp",   # Dione, Mimas, Encelade, Téthys,Titan
}

BODY_MAP = {
    # Planets
    "sun": "Sun",
    "mercury": "Mercury Barycenter",
    "venus": "Venus Barycenter",
    "earth": "Earth Barycenter",
    "mars": "Mars Barycenter",
    "jupiter": "Jupiter Barycenter",
    "saturn": "Saturn Barycenter",
    "uranus": "Uranus Barycenter",
    "neptune": "Neptune Barycenter",
    # Jupiter satellites
    "io": "Io",
    "europa": "Europa",
    "ganymede": "Ganymede",
    "callisto": "Callisto",
    "amalthea": "Amalthea",
    # Saturn satellites
    "titan": 606,
    "dione": "Dione",
    "mimas": "Mimas",
    "enceladus": "Enceladus",
    "tethys": "Tethys",
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
    "io":       8.932e22,
    "europa":   4.800e22,
    "ganymede": 1.482e23,
    "callisto": 1.076e23,
    "amalthea": 2.080e18,
    "titan": 1.345e23,
    "dione":    1.095e21,
    "mimas":    3.749e19,
    "enceladus":1.080e20,
    "tethys":   6.175e20,
}

BODY_DISPLAY = {
    "sun":      {"name": "Soleil",   "color": "#FFD700", "size": 0.08},
    "mercury":  {"name": "Mercure",  "color": "#B5B5B5", "size": 0.03},
    "venus":    {"name": "Vénus",    "color": "#E8C98A", "size": 0.04},
    "earth":    {"name": "Terre",    "color": "#4B9CD3", "size": 0.04},
    "mars":     {"name": "Mars",     "color": "#C1440E", "size": 0.035},
    "jupiter":  {"name": "Jupiter",  "color": "#C88B3A", "size": 0.07},
    "saturn":   {"name": "Saturne",  "color": "#E4D191", "size": 0.06},
    "uranus":   {"name": "Uranus",   "color": "#7DE8E8", "size": 0.05},
    "neptune":  {"name": "Neptune",  "color": "#4B70DD", "size": 0.05},
    
    "io":       {"name": "Io",       "color": "#FFE566", "size": 0.02},
    "europa":   {"name": "Europa",   "color": "#C8E0FF", "size": 0.02},
    "ganymede": {"name": "Ganymède", "color": "#A0A0A0", "size": 0.025},
    "callisto": {"name": "Callisto", "color": "#6B5A3E", "size": 0.025},
    "amalthea": {"name": "Amalthée", "color": "#CC4400", "size": 0.01},
    "titan": {"name": "Titan", "color": "#E8A830", "size": 0.018},
    "dione":    {"name": "Dioné",    "color": "#D0D0D0", "size": 0.015},
    "mimas":    {"name": "Mimas",    "color": "#B0B0B0", "size": 0.01},
    "enceladus":{"name": "Encelade", "color": "#FFFFFF", "size": 0.012},
    "tethys":   {"name": "Téthys",   "color": "#C8C8C8", "size": 0.013},
    "probe":    {"name": "Sonde",    "color": "#FF4444", "size": 0.02},
}

VOYAGER1_CONFIGS = {
    "Système solaire complet": [
        "sun", "earth", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"
    ],
    "Jovian Syteme": [
        "sun", "jupiter", "io", "europa", "ganymede", "callisto", "amalthea"
    ],
    "Saturnian System": [
        "sun", "saturn", "dione", "mimas", "enceladus", "tethys","titan"
    ],
}

SATELLITES_JUPITER = {"io", "europa", "ganymede", "callisto", "amalthea"}
SATELLITES_SATURN = {"dione", "mimas", "enceladus", "tethys", "titan"}

from skyfield.api import load
from skyfield.framelib import ecliptic_J2000_frame


SPK_FILES = {
    "default": "de440.bsp",
    "jupiter_satellites": "jup365.bsp",  # Io, Europa, Ganymède, Callisto, Amalthée
    "saturn_satellites": "sat441.bsp",   # Dione, Mimas, Encelade, Téthys
}

SATELLITES_JUPITER = {"io", "europa", "ganymede", "callisto", "amalthea"}
SATELLITES_SATURN = {"dione", "mimas", "enceladus", "tethys","titan"}

def Probe(
    departure_time,
    initial_state,
    name=None,
    probe_mass=0,
    G=6.674e-11 * (31557600**2) / (1.495978707e11**3)
) -> System:

    if name is None:
        name = ["sun", "earth", "mars", "venus", "mercury", "jupiter", "saturn", "uranus", "neptune"]

    ts = load.timescale()
    t = ts.tdb_jd(departure_time)

    names = [k.lower() for k in name]
    names_set = set(names)
    planets = load("de440.bsp")

    if names_set & SATELLITES_JUPITER:
        jup = load("jup365.bsp")
    if names_set & SATELLITES_SATURN:
        sat = load("sat441.bsp")
    def get_body(k):
        if k in SATELLITES_JUPITER:
            return jup[BODY_MAP[k]]
        elif k in SATELLITES_SATURN:
            return sat[BODY_MAP[k]]
        else:
            return planets[BODY_MAP[k]]

    bodies = [get_body(k) for k in names]

    positions = np.array([body.at(t).frame_xyz(ecliptic_J2000_frame).m for body in bodies]) / 1.495978707e11
    velocities = np.array([body.at(t).frame_xyz_and_velocity(ecliptic_J2000_frame)[1].km_per_s for body in bodies]) * 31557600 / 1.495978707e8
    masses = np.array([MASSES[k] for k in names])

    positions = np.vstack([positions, initial_state[0] / 1.495978707e8])
    velocities = np.vstack([velocities, initial_state[1] * 31557600 / 1.495978707e8])
    masses = np.append(masses, probe_mass)

    return System(
        positions=positions,
        velocities=velocities,
        masses=masses,
        G=G,
        body_display=[BODY_DISPLAY.get(n, BODY_DISPLAY["probe"]) for n in names] + [{"name": "Voyager 1", "color": "#FF4444", "size": 0.02}],
    )


def Voyager1(departure_jd: float = None, config: str = "Système solaire complet") -> System:
    from nbody_sim.data.voyager1_trajectory import VOYAGER1_TRAJECTORY

    jd = departure_jd if departure_jd is not None else Departure_time["Voyager1"]
    data = VOYAGER1_TRAJECTORY[jd]

    UA_KM = 1.495978707e8
    S_PER_YEAR = 31557600.0

    pos_km = np.array(data["pos"]) * UA_KM
    vel_kms = np.array(data["vel"]) * UA_KM / S_PER_YEAR

    name = VOYAGER1_CONFIGS[config]

    return Probe(
        departure_time=jd,
        initial_state=np.array([pos_km, vel_kms]),
        probe_mass=721.9,
        name=name,
    )



