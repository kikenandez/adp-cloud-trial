import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tally import count_words  # noqa: E402


class TestTally(unittest.TestCase):
    def test_counts_case_insensitive(self) -> None:
        self.assertEqual(count_words("A a b."), {"a": 2, "b": 1})

    def test_empty(self) -> None:
        self.assertEqual(count_words("  "), {})


if __name__ == "__main__":
    unittest.main()
