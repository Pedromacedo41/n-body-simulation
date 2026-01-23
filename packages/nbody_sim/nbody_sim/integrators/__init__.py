from nbody_sim.integrators.euler import Euler

INTEGRATORS = {
    "euler": Euler,
}

def list_integrators():
    return INTEGRATORS

def get_integrator(name: str):
    return INTEGRATORS[name]()

