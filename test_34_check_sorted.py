import importlib

is_sorted = importlib.import_module("34_check_sorted").is_sorted


def test_sorted_list():
    assert is_sorted([1, 2, 2, 5]) is True


def test_unsorted_list():
    assert is_sorted([1, 4, 3]) is False


def test_empty_and_single_item_lists():
    assert is_sorted([]) is True
    assert is_sorted([7]) is True