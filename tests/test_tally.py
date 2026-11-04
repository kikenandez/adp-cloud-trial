import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tally import count_words, top_words  # noqa: E402


class TestTally(unittest.TestCase):
    def test_counts_case_insensitive(self) -> None:
        self.assertEqual(count_words("A a b."), {"a": 2, "b": 1})

    def test_empty(self) -> None:
        self.assertEqual(count_words("  "), {})

    def test_top_words_orders_by_frequency(self) -> None:
        self.assertEqual(
            top_words("b a b c b a", 2), [("b", 3), ("a", 2)]
        )

    def test_top_words_ties_alphabetical(self) -> None:
        self.assertEqual(
            top_words("pear apple fig apple pear fig", 2),
            [("apple", 2), ("fig", 2)],
        )

    def test_top_words_n_larger_than_vocabulary(self) -> None:
        self.assertEqual(top_words("Cat dog cat.", 10), [("cat", 2), ("dog", 1)])

    def test_top_words_zero_or_empty(self) -> None:
        self.assertEqual(top_words("a b", 0), [])
        self.assertEqual(top_words("", 3), [])


if __name__ == "__main__":
    unittest.main()
