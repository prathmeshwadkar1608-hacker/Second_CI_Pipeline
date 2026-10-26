import re


def count_words(sentence):
    """Count words in a sentence."""
    return len(re.findall(r"\b[\w']+\b", sentence))