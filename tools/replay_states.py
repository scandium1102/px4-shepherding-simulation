"""Check the documented simulator states against offline event fixtures."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSITIONS = {
    ("initializing", "setup_complete"): "patrol",
    ("patrol", "simulated_target_seen"): "approach",
    ("approach", "target_lost"): "patrol",
    ("approach", "response_triggered"): "follow",
    ("follow", "target_lost"): "patrol",
    ("follow", "response_finished"): "return",
    ("return", "return_reached"): "patrol",
}


def replay(events):
    if not isinstance(events, list) or not events:
        raise ValueError("provide a nonempty array of events")
    states = ["initializing"]
    for index, event in enumerate(events, start=1):
        if not isinstance(event, str):
            raise ValueError(f"event {index} must be text")
        state = states[-1]
        next_state = TRANSITIONS.get((state, event))
        if next_state is None:
            raise ValueError(f"event {index}: {event!r} is invalid in {state}")
        states.append(next_state)
    return states


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=ROOT / "examples/nominal.json")
    args = parser.parse_args()
    try:
        events = json.loads(args.fixture.read_text(encoding="utf-8"))
        print(" -> ".join(replay(events)))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
