from collections import Counter


def word_count(text: str) -> int:
    """Return the number of words in ``text``.

    Words are separated by whitespace.
    """
    return len(text.split())


def most_common(words: list[str], n: int = 3) -> list[tuple[str, int]]:
    """Return the ``n`` most frequent words with their counts.

    Words are compared case-insensitively; the result is ordered from most to
    least frequent.
    """
    return Counter(w.lower() for w in words).most_common(n)


def reading_time_minutes(text: str, words_per_minute: int = 200) -> int:
    """Estimate the reading time of ``text`` in whole minutes."""
    return word_count(text) // words_per_minute
