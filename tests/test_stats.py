import unittest

from textkit import char_count, most_common, reading_time_minutes, word_count


class WordCountTests(unittest.TestCase):
    def test_counts_words_separated_by_single_spaces(self):
        self.assertEqual(word_count("one two three"), 3)


class MostCommonTests(unittest.TestCase):
    def test_orders_by_frequency(self):
        self.assertEqual(most_common(["a", "b", "a"], 1), [("a", 2)])

    def test_is_case_insensitive(self):
        self.assertEqual(most_common(["A", "a"], 1), [("a", 2)])


class ReadingTimeTests(unittest.TestCase):
    def test_long_text_takes_several_minutes(self):
        text = " ".join(["word"] * 600)
        self.assertEqual(reading_time_minutes(text), 3)


class CharCountTests(unittest.TestCase):
    def test_default_counts_all_characters(self):
        self.assertEqual(char_count("a b\tc\n"), 6)

    def test_include_spaces_true_matches_default(self):
        self.assertEqual(char_count("a b\tc\n", include_spaces=True), 6)

    def test_exclude_spaces_skips_whitespace(self):
        self.assertEqual(char_count("a b\tc\n", include_spaces=False), 3)

    def test_empty_string_is_zero(self):
        self.assertEqual(char_count(""), 0)
        self.assertEqual(char_count("", include_spaces=False), 0)

    def test_whitespace_only(self):
        self.assertEqual(char_count("  \t\n"), 4)
        self.assertEqual(char_count("  \t\n", include_spaces=False), 0)


if __name__ == "__main__":
    unittest.main()
