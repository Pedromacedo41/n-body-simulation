from nbody_sim.presets.two_body import two_body_circular

PRESETS = {
    "two_body_circular": two_body_circular,
}

def list_presets():
    return PRESETS

def get_preset(name: str):
    return PRESETS[name]
