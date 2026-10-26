import importlib

most_frequent = importlib.import_module("36_most_frequent").most_frequent


def test_most_frequent_item():
    assert most_frequent([1, 2, 2, 3]) == 2


def test_tie_uses_first_appearance():
    assert most_frequent(["b", "a", "a", "b"]) == "b"


def test_empty_list():
    assert most_frequent([]) is None