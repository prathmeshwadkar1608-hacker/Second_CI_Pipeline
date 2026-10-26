import importlib

find_missing_number = (
    importlib.import_module("38_missing_number_xor").find_missing_number
)


def test_missing_middle_number():
    assert find_missing_number([3, 0, 1]) == 2


def test_missing_zero():
    assert find_missing_number([1, 2, 3]) == 0


def test_missing_last_number():
    assert find_missing_number([0, 1, 2]) == 3