from nbody_sim.integrators.euler import Euler
from nbody_sim.integrators.RK4 import RK4
from nbody_sim.integrators.leap_frog import leap_frog

INTEGRATORS = {
    "euler": Euler,
    "RK4":RK4,
    "leap_frog":leap_frog
}

def list_integrators():
    return INTEGRATORS

def get_integrator(name: str):
    return INTEGRATORS[name]()

