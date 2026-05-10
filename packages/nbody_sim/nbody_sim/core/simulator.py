
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System
import numpy as np

class Simulator:
    def __init__(self, system: System, integrator: Integrator):
        self.system = system
        self.integrator = integrator

    def step(self, dt: float):
        self.system = self.integrator.step(self.system, dt)
        return self.system
    
    def calculate_dt(self, alpha: float, dt_max: float, dt_min: float) -> float:
        #Calculate by courant condition dt=a*min(Delta ri/ Delta vi)
        #The probe is the last body of the system
        probe_pos = self.system.positions[-1]
        probe_vel = self.system.velocities[-1]
        planet_positions = self.system.positions[:-1]
        planet_velocities = self.system.velocities[:-1]
        Delta_r = np.linalg.norm(planet_positions - probe_pos, axis=1)
        Delta_v = np.maximum(np.linalg.norm(planet_velocities - probe_vel, axis=1), 1e-10)
        dt = alpha * np.min(Delta_r / Delta_v)
        return float(np.clip(dt, dt_min, dt_max))

    def run_iter(self, dt: float, steps: int):
        for step in range(steps):
            yield step, self.step(dt)

    #For adaptive step        
    def run_adaptive(self, t_total: float, dt_max: float = 0.0001,
                     dt_min: float = 1e-8, alpha: float = 0.01):
        t = 0.0
        while t < t_total:
            dt = self.calculate_dt(alpha, dt_max, dt_min)
            yield t, self.step(dt)
            t += dt


