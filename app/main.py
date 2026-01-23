import streamlit as st
from tabs.run import run_tab
from tabs.replay import replay_tab

st.set_page_config(layout="wide", page_title="N-body Simulator")

st.subheader("N-body Simulator")

tab_run, tab_replay = st.tabs(["Run", "Replay"])

with tab_run:
    run_tab()

with tab_replay:
    replay_tab()
