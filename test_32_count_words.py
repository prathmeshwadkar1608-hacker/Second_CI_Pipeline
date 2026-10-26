import importlib

count_words = importlib.import_module("32_count_words").count_words


def test_normal_sentence():
    assert count_words("Python is easy to learn") == 5


def test_empty_string():
    assert count_words("") == 0


def test_extra_spaces_and_punctuation():
    assert count_words("  Hello,   world! ") == 2
    