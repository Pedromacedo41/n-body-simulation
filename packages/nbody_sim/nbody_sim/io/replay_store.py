from pathlib import Path
from typing import List
from datetime import datetime

from nbody_sim.types import Replay
from nbody_sim.io.replay import load_replay

REPLAY_DIR = Path("data/replays")


def ensure_replay_dir():
    REPLAY_DIR.mkdir(parents=True, exist_ok=True)


def list_replays() -> List[Path]:
    ensure_replay_dir()
    return sorted(
        REPLAY_DIR.glob("*.json"),
        key=lambda p: p.stat().st_ctime,
        reverse=True,
    )


def load_replay_file(path: Path) -> Replay:
    return load_replay(path)


def delete_replay(path: Path):
    path.unlink()
