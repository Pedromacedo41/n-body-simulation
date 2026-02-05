from nbody_sim.integrators.euler import Euler
from nbody_sim.integrators.RK4 import RK4
INTEGRATORS = {
    "euler": Euler,
    "RK4": RK4
}

def list_integrators():
    return INTEGRATORS

def get_integrator(name: str):
    return INTEGRATORS[name]()

