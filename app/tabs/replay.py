import json
import streamlit as st
import pandas as pd
from pathlib import Path

from nbody_sim.io.replay_store import list_replays, load_replay_file, delete_replay

def on_replay_change():
    st.session_state.selected_replay = st.session_state.replay_selects

def render_threejs_viewer(replay):
    with open("app/frontend/replay_viewer.html") as f:
        html = f.read()

    payload = {
        "positions": replay.data.positions.tolist(),
        "dt": replay.meta.dt,
    }

    html = html.replace(
        "window.REPLAY_DATA;",
        f"window.REPLAY_DATA = {json.dumps(payload)};"
    )

    st.components.v1.html(
        html,
        height=900,
    )

def replay_tab():
    replays = list_replays()

    if not replays:
        st.info("No replays found")
        return

    replay_names = [p.name for p in replays]

    col_select, col_delete = st.columns([4, 1])

    with col_select:
        selected = st.selectbox(
            "Select replay sample",
            replay_names,
        )

    with col_delete:
        st.write("")
        st.write("")
        if st.button("Delete"):
            path = Path("data/replays") / selected
            delete_replay(path)
            st.experimental_rerun()

    replay = load_replay_file(Path("data/replays") / selected)

    col_view1, col_meta = st.columns([4, 1.5])

    with col_view1:
        st.subheader("3D Viewer")
        render_threejs_viewer(replay)

    with col_meta:
        st.subheader("Metadata")

        meta_df = pd.DataFrame(
            replay.meta.__dict__.items(),
            columns=["Field", "Value"]
        )

        st.table(meta_df)

