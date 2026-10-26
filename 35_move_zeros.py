def move_zeros(values):
    """Return a new list with zeros moved to the end."""
    non_zeros = [value for value in values if value != 0]
    zeros = [value for value in values if value == 0]

    return non_zeros + zeros