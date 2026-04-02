from nbody_sim.presets.two_body import two_body_circular
from nbody_sim.presets.Solar_system import Solar_system
from nbody_sim.presets.Probe import Probe

PRESETS = {
    "two_body_circular": two_body_circular,
    "Solar systeme":Solar_system,
    "Probe":Probe
}

def list_presets():
    return PRESETS

def get_preset(name: str):
    return PRESETS[name]
