import json
import streamlit as st
import pandas as pd
from pathlib import Path

from nbody_sim.io.replay_store import list_replays, load_replay_file, delete_replay

def on_replay_change():
    st.session_state.selected_replay = st.session_state.replay_selects

def render_threejs_viewer(replay):
    with open("app/static/index.html", encoding='utf-8') as f:
        html = f.read()
    if replay.data.times is not None:
        times = replay.data.times.tolist()
    elif replay.meta.dt is not None:
        times = [i * replay.meta.dt for i in range(replay.meta.steps)]
    else:
    # Aucun dt disponible — on utilise juste les indices de frames
        times = list(range(replay.meta.steps))
    payload = {
    "positions": replay.data.positions.tolist(),
    "times": times,
    "body_configs": replay.data.body_display, 
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
            st.rerun()

    replay = load_replay_file(Path("data/replays") / selected)

    col_view1, col_meta = st.columns([4, 1.5])

    with col_view1:
        st.subheader("3D Viewer")
        render_threejs_viewer(replay)

    with col_meta:
        st.subheader("Metadata")

        meta_dict = {k: v for k, v in replay.meta.__dict__.items() if v is not None}
        meta_df = pd.DataFrame(
            meta_dict.items(),
            columns=["Field", "Value"]
        )
        meta_df["Value"] = meta_df["Value"].astype(str)
        st.table(meta_df)
