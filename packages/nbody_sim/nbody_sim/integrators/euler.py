from nbody_sim.core.forces import gravitational_forces
from nbody_sim.integrators.base import Integrator
from nbody_sim.types import System

#Euler semi-implicite
class Euler(Integrator):
    name = "euler"

    def step(self, system: System, dt: float) -> System:
        a = gravitational_forces(system)
        nouveau_vecteur_etat = system.vecteur_etat.copy()
        nouveau_vecteur_etat[0] += a * dt
        nouveau_vecteur_etat[1] += nouveau_vecteur_etat[0] * dt
        system.vecteur_etat = nouveau_vecteur_etat
        return system
