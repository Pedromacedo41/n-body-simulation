import json
import numpy as np
from nbody_sim.types import Replay

def replay_to_dict(replay: Replay) -> dict:
    return {
        "meta": replay.meta.__dict__,
        "data": {
            "positions": replay.data.positions.tolist()
        }
    }

def replay_from_dict(d: dict) -> Replay:
    from nbody_sim.types import ReplayMeta, ReplayData

    return Replay(
        meta=ReplayMeta(**d["meta"]),
        data=ReplayData(
            positions=np.array(d["data"]["positions"])
        )
    )

def save_replay(path: str, replay: Replay):
    with open(path, "w") as f:
        json.dump(replay_to_dict(replay), f)

def load_replay(path: str) -> Replay:
    with open(path) as f:
        return replay_from_dict(json.load(f))
