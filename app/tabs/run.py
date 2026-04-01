from pathlib import Path
from nbody_sim.core.simulator import Simulator
from nbody_sim.integrators import get_integrator, list_integrators
from nbody_sim.io.replay import save_replay
from nbody_sim.presets import get_preset, list_presets
from nbody_sim.types import Replay, ReplayData, ReplayMeta
import numpy as np
import streamlit as st


def run_simulation():
    dt = st.session_state.dt
    steps = int(st.session_state.duration / dt)

    preset_fn = get_preset(st.session_state.preset)
    system = preset_fn()

    integrator = get_integrator(st.session_state.integrator)
    simulator = Simulator(system.copy(), integrator)

    positions = []
    progress = st.progress(0)
    status = st.empty()

    for step, state in simulator.run_iter(dt=dt, steps=steps):
        positions.append(state.positions.copy())
        progress.progress((step + 1) / steps)
        status.text(f"Running simulation... step {step+1}/{steps}")

    progress.empty()
    status.empty()
    save_replay_from_positions(positions)


def save_replay_from_positions(positions: list):
    replay = Replay(
        meta=ReplayMeta(
            name=st.session_state.replay_name,
            dt=st.session_state.dt,
            steps=len(positions),
            integrator=st.session_state.integrator,
            preset=st.session_state.preset,
        ),
        data=ReplayData(positions=np.array(positions))
    )
    save_replay(Path("data/replays") / f"{replay.meta.name}.json", replay)


def run_tab():
    st.subheader("Simulation parameters")

    st.text_input(
        "Replay file name",
        key="replay_name",
        placeholder="two_body_test",
    )

    presets = list(list_presets().keys())
    integrator_names = list(list_integrators().keys())

    st.selectbox("Preset", presets, key="preset")

    st.number_input(
        "Time step (dt) in years",
        min_value=0.0001,
        max_value=10.0,
        value=0.001,
        key="dt",
    )

    st.number_input(
        "Duration (years)",
        min_value=0.01,
        max_value=1e6,
        value=1.0,
        key="duration",
    )

    st.selectbox("Integrator", integrator_names, key="integrator")

    st.button("Run", on_click=run_simulation)

    st.divider()
