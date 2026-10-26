def first_non_repeating_char(text):
    """Return the first character that occurs once, or None."""
    for char in text:
        if text.count(char) == 1:
            return char

    return None