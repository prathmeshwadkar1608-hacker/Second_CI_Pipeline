import importlib

module = importlib.import_module("31_pangram")


def test_pangram_true():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False


def test_pangram_mixed_case():
    assert module.is_pangram(
        "Pack my box with five dozen liquor jugs"
    ) is True