from pathlib import Path
from nbody_sim.core.simulator import Simulator
from nbody_sim.integrators import get_integrator, list_integrators
from nbody_sim.io.replay import save_replay
from nbody_sim.presets import get_preset, list_presets
from nbody_sim.types import Replay, ReplayMeta, ReplayData
from nbody_sim.data.voyager1_trajectory import VOYAGER1_TRAJECTORY
from nbody_sim.presets.Probe import VOYAGER1_CONFIGS
from datetime import datetime
import numpy as np
import streamlit as st



def run_simulation():
    duration = st.session_state.duration
    step_mode = st.session_state.step_mode

    preset_fn = get_preset(st.session_state.preset)
    if st.session_state.preset == "Voyager1":
        system = preset_fn(
            departure_jd=st.session_state.get("voyager1_jd"),
            config=st.session_state.get("voyager1_config", "Système solaire complet")
        )
    else:
        system = preset_fn()
    integrator = get_integrator(st.session_state.integrator)
    simulator = Simulator(system.copy(), integrator)

    positions = []
    velocities = []
    times = []
    progress = st.progress(0)
    status = st.empty()

    if step_mode == "Adaptive":
        iterator = simulator.run_adaptive(
            t_total=duration,
            alpha=st.session_state.get("alpha", 0.01),
            dt_max=st.session_state.get("dt_max", 0.0001),
            dt_min=st.session_state.get("dt_min", 1e-8),)
        for i, (t, state) in enumerate(iterator):
            if i % st.session_state.save_every == 0:
                positions.append(state.positions.copy())
                velocities.append(state.velocities.copy())
                times.append(t)
            progress.progress(min(t / duration, 1.0))
            status.text(f"t={t:.4f} / {duration:.2f} ans")

    else:
        dt = st.session_state.get("dt", 0.0001)
        steps = int(duration / dt)
        for step, state in simulator.run_iter(dt=dt, steps=steps):
            if step % st.session_state.save_every == 0:
                positions.append(state.positions.copy())
                velocities.append(state.velocities.copy())
                times.append(step * dt)
            progress.progress((step + 1) / steps)
            status.text(f"step {step+1}/{steps}")

    progress.empty()
    status.empty()
    save_replay_from_positions(positions, times, system.body_display, velocities)


def save_replay_from_positions(positions: list, times: list, body_display: list = None, velocities: list = None):
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
            body_display=body_display,
            velocities=np.array(velocities) if velocities else None,
        )
    )
    save_replay(Path("data/replays") / f"{replay.meta.name}.json", replay)

def run_tab():
    st.subheader("Simulation parameters")

    st.text_input("Replay file name", key="replay_name", placeholder="two_body_test")

    presets = list(list_presets().keys())
    integrator_names = list(list_integrators().keys())

    st.selectbox("Preset", presets, key="preset")
    if st.session_state.get("preset") == "Voyager1":
        st.selectbox(
            "Configuration des corps",
            list(VOYAGER1_CONFIGS.keys()),
            key="voyager1_config"
        )

        # Sélecteur de date
        date_options = {}
        for jd, data in VOYAGER1_TRAJECTORY.items():
            raw = data["date"][:16]
            try:
                dt = datetime.strptime(raw, "%Y-%b-%d %H:%M")
                label = dt.strftime("%Y:%m:%d %Hh%M")
            except:
                label = raw
            date_options[label] = jd

        selected_date = st.selectbox(
            "Date de départ",
            list(date_options.keys()),
            index=0,
            key="voyager1_date"
        )
        st.session_state["voyager1_jd"] = date_options[selected_date]
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