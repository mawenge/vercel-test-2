import unittest

from textkit import line_count, most_common, reading_time_minutes, word_count


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


class LineCountTests(unittest.TestCase):
    def test_empty_string_has_no_lines(self):
        self.assertEqual(line_count(""), 0)

    def test_single_line_without_newline(self):
        self.assertEqual(line_count("a"), 1)

    def test_trailing_newline_does_not_add_a_line(self):
        self.assertEqual(line_count("a\n"), 1)

    def test_multiple_lines_with_trailing_newline(self):
        self.assertEqual(line_count("a\nb\n"), 2)

    def test_multiple_lines_without_trailing_newline(self):
        self.assertEqual(line_count("a\nb\nc"), 3)

    def test_blank_line_is_counted(self):
        self.assertEqual(line_count("a\n\nb"), 3)

    def test_windows_line_endings(self):
        self.assertEqual(line_count("a\r\nb\r\n"), 2)


if __name__ == "__main__":
    unittest.main()
