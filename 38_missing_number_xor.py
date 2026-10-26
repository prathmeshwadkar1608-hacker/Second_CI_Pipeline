def find_missing_number(values):
    """Find the missing integer from the range 0 through n."""
    n = len(values)
    missing = n

    for index, value in enumerate(values):
        missing ^= index ^ value

    return missing