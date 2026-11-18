import json
import unittest

from tools.replay_states import ROOT, replay


class ReplayTests(unittest.TestCase):
    def test_nominal_scenario(self):
        events = json.loads((ROOT / "examples/nominal.json").read_text(encoding="utf-8"))
        self.assertEqual(
            replay(events), ["initializing", "patrol", "approach", "follow", "return", "patrol"]
        )

    def test_sensor_loss_returns_to_patrol(self):
        events = json.loads((ROOT / "examples/target_lost.json").read_text(encoding="utf-8"))
        self.assertEqual(replay(events), ["initializing", "patrol", "approach", "patrol"])

    def test_invalid_transition_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid in initializing"):
            replay(["return_reached"])


if __name__ == "__main__":
    unittest.main()
