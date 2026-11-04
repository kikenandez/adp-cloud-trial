"""tally — a tiny word counter used to trial ADP in a cloud project."""


def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        word = word.strip(".,;:!?\"'()")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most frequent words, ties broken alphabetically."""
    if n <= 0:
        return []
    ranked = sorted(count_words(text).items(), key=lambda item: (-item[1], item[0]))
    return ranked[:n]
