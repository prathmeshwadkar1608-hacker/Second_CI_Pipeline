import importlib

rotate_string = importlib.import_module("37_rotate_string").rotate_string


def test_left_rotation():
    assert rotate_string("abcdef", 2) == "cdefab"


def test_rotation_larger_than_length():
    assert rotate_string("abc", 5) == "cab"


def test_empty_string_and_negative_rotation():
    assert rotate_string("", 3) == ""
    assert rotate_string("abcd", -1) == "dabc"