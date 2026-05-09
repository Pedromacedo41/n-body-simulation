from nbody_sim.presets.two_body import two_body_circular
from nbody_sim.presets.Solar_system import Solar_system
from nbody_sim.presets.Probe import Voyager1
from nbody_sim.presets.Probe import Voyager2
from nbody_sim.presets.Probe import Cassini
from nbody_sim.presets.Probe import New_Horizon
from nbody_sim.presets.Probe import Rosetta
from nbody_sim.presets.Probe import Messenger

PRESETS = {
    "two_body_circular": two_body_circular,
    "Solar systeme":Solar_system,
    "Voyager1":Voyager1,
    "Voyager2":Voyager2,
    "Cassini":Cassini,
    "Rosetta":Rosetta,
    "Messenger":Messenger
}

def list_presets():
    return PRESETS

def get_preset(name: str):
    return PRESETS[name]
