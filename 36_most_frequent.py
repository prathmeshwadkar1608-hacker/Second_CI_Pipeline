from collections import Counter


def most_frequent(values):
    """Return the most frequent item; ties use the first appearing item."""
    if not values:
        return None

    counts = Counter(values)
    highest_count = max(counts.values())

    for value in values:
        if counts[value] == highest_count:
            return value