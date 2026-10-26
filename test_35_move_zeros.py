import importlib

move_zeros = importlib.import_module("35_move_zeros").move_zeros


def test_zeros_move_to_end():
    assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_no_zeros():
    assert move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros_and_empty_list():
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([]) == []