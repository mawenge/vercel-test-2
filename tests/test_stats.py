import unittest

from textkit import most_common, reading_time_minutes, word_count


class WordCountTests(unittest.TestCase):
    def test_counts_words_separated_by_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_collapses_repeated_spaces(self):
        self.assertEqual(word_count("hello  world"), 2)

    def test_ignores_leading_whitespace(self):
        self.assertEqual(word_count(" hi"), 1)

    def test_ignores_trailing_whitespace(self):
        self.assertEqual(word_count("hi "), 1)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)

    def test_all_whitespace_text_has_no_words(self):
        self.assertEqual(word_count(" \t\n "), 0)

    def test_counts_words_separated_by_tabs_and_newlines(self):
        self.assertEqual(word_count("one\ttwo\nthree"), 3)


class MostCommonTests(unittest.TestCase):
    def test_orders_by_frequency(self):
        self.assertEqual(most_common(["a", "b", "a"], 1), [("a", 2)])

    def test_is_case_insensitive(self):
        self.assertEqual(most_common(["A", "a"], 1), [("a", 2)])


class ReadingTimeTests(unittest.TestCase):
    def test_long_text_takes_several_minutes(self):
        text = " ".join(["word"] * 600)
        self.assertEqual(reading_time_minutes(text), 3)


if __name__ == "__main__":
    unittest.main()
