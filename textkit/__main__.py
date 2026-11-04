import sys

from .stats import most_common, reading_time_minutes, word_count


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m textkit FILE", file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as handle:
        text = handle.read()
    print(f"words: {word_count(text)}")
    print(f"reading time (min): {reading_time_minutes(text)}")
    for word, count in most_common(text.split()):
        print(f"{word}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
