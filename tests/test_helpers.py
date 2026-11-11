"""Basic offline tests using synthetic values only."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class HelpersTest(unittest.TestCase):
    def test_durations(self):
        m = load("check_durations")
        self.assertIsNone(m.check(3, [2, 4, 3], 9))
        self.assertIsNotNone(m.check(3, [2, 4, 3], 8))
        self.assertIsNone(m.check(3, [2, 4, 3, 0], 9, True))
    def test_token_check(self):
        self.assertEqual(load("check_text").unknown_symbols("abc", {"a", "b"}), ["c"])
    def test_speaker_split(self):
        m = load("split_corpus")
        result = m.split([("a","x"),("b","x"),("c","y"),("d","z")], seed=3, dev=0.3, test=0.3)
        assignments = {}
        for group, ids in result.items():
            for uid in ids:
                assignments[uid]=group
        self.assertEqual(assignments["a"], assignments["b"])
        self.assertEqual(len(assignments),4)
    def test_publication_scan_safe(self):
        mod=load("publication_audit")
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/"safe.txt").write_text("path/to/dataset", encoding="utf-8")
            self.assertEqual(mod.scan(Path(d)), [])

if __name__ == "__main__":
    unittest.main()
