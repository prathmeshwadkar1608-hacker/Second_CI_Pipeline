import importlib

first_non_repeating_char = (
    importlib.import_module("33_first_non_repeating").first_non_repeating_char
)


def test_example():
    assert first_non_repeating_char("swiss") == "w"


def test_first_character_is_unique():
    assert first_non_repeating_char("abcd") == "a"


def test_no_unique_character():
    assert first_non_repeating_char("aabb") is None