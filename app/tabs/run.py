from pathlib import Path
from nbody_sim.core.simulator import Simulator
from nbody_sim.integrators import get_integrator, list_integrators
from nbody_sim.io.replay import save_replay
from nbody_sim.presets import get_preset, list_presets
from nbody_sim.types import Replay, ReplayMeta, ReplayData
import numpy as np
import streamlit as st



def run_simulation():
    duration = st.session_state.duration
    step_mode = st.session_state.step_mode

    preset_fn = get_preset(st.session_state.preset)
    system = preset_fn()
    integrator = get_integrator(st.session_state.integrator)
    simulator = Simulator(system.copy(), integrator)

    positions = []
    times = []
    progress = st.progress(0)
    status = st.empty()

    if step_mode == "Adaptatif":
        iterator = simulator.run_adaptive(
            t_total=duration,
            alpha=st.session_state.alpha,
            dt_max=st.session_state.dt_max,
            dt_min=st.session_state.dt_min,
        )
        for i, (t, state) in enumerate(iterator):
            if i % st.session_state.save_every == 0:
                positions.append(state.positions.copy())
                times.append(t)
            progress.progress(min(t / duration, 1.0))
            status.text(f"t={t:.4f} / {duration:.2f} ans")

    else:
        dt = st.session_state.dt
        steps = int(duration / dt)
        for step, state in simulator.run_iter(dt=dt, steps=steps):
            if step % st.session_state.save_every == 0:
                positions.append(state.positions.copy())
                times.append(step * dt)
            progress.progress((step + 1) / steps)
            status.text(f"step {step+1}/{steps}")

    progress.empty()
    status.empty()
    save_replay_from_positions(positions, times)


def save_replay_from_positions(positions: list, times: list):
    step_mode = st.session_state.step_mode

    replay = Replay(
        meta=ReplayMeta(
            name=st.session_state.replay_name,
            steps=len(positions),
            integrator=st.session_state.integrator,
            preset=st.session_state.preset,
            duration=st.session_state.duration,
            dt=st.session_state.get("dt", None),
            alpha=st.session_state.get("alpha", None),
            dt_max=st.session_state.get("dt_max", None),
            dt_min=st.session_state.get("dt_min", None),
        ),
        data=ReplayData(
            positions=np.array(positions),
            times=np.array(times),
        )
    )
    save_replay(Path("data/replays") / f"{replay.meta.name}.json", replay)



def run_tab():
    st.subheader("Simulation parameters")

    st.text_input("Replay file name", key="replay_name", placeholder="two_body_test")

    presets = list(list_presets().keys())
    integrator_names = list(list_integrators().keys())

    st.selectbox("Preset", presets, key="preset")

    st.number_input("Duration (years)", min_value=0.01, max_value=1e6, value=5.0, key="duration")

    st.selectbox("Integrator", integrator_names, key="integrator")

    # --- MODE DE PAS ---
    st.selectbox("step mode", ["Adaptive", "Constant"], key="step_mode")

    if st.session_state.step_mode == "Adaptive":
        st.number_input("Alpha - Courant step integration constant", min_value=1e-6, max_value=1.0, value=0.01, key="alpha", format="%.6f")
        st.number_input("max dt (years)", min_value=1e-6, max_value=0.01, value=0.0001, key="dt_max", format="%.6f")
        st.number_input("min dt  (years)", min_value=1e-12, max_value=1e-6, value=1e-8, key="dt_min", format="%.2e")
    else:
        st.number_input("dt (years)", min_value=1e-6, max_value=1.0, value=0.0001, key="dt", format="%.6f")

    st.number_input("Save on frame over N", min_value=1, max_value=1000, value=100, key="save_every")

    st.button("Run", on_click=run_simulation)
    st.divider()