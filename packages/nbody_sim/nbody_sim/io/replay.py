import json
import numpy as np
from nbody_sim.types import Replay
from nbody_sim.types import Replay, ReplayMeta, ReplayData

def replay_to_dict(replay: Replay) -> dict:
    return {
        "meta": replay.meta.__dict__,
        "data": {
            "positions": replay.data.positions.tolist(),
            "times": replay.data.times.tolist() if replay.data.times is not None else None,
            "body_display": replay.data.body_display,
            "velocities": replay.data.velocities.tolist() if replay.data.velocities is not None else None,
        }
    }

def replay_from_dict(d):
    return Replay(
        meta=ReplayMeta(**d["meta"]),
        data=ReplayData(
            positions=np.array(d["data"]["positions"]),
            times=np.array(d["data"]["times"]) if "times" in d["data"] else None,
            body_display=d["data"].get("body_display", None),
            velocities=np.array(d["data"]["velocities"]) if d["data"].get("velocities") is not None else None,
        )
    )

def save_replay(path: str, replay: Replay):
    with open(path, "w") as f:
        json.dump(replay_to_dict(replay), f)

def load_replay(path: str) -> Replay:
    with open(path) as f:
        return replay_from_dict(json.load(f))
