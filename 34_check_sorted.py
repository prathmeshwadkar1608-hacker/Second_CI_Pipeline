def is_sorted(values):
    """Return True if values are in non-decreasing order."""
    return all(
        values[index] <= values[index + 1]
        for index in range(len(values) - 1)
    )