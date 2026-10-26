import importlib

find_gcd = importlib.import_module("40_gcd").find_gcd


def test_positive_numbers():
    assert find_gcd(12, 18) == 6


def test_coprime_numbers():
    assert find_gcd(7, 13) == 1


def test_zero_and_negative_values():
    assert find_gcd(0, 5) == 5
    assert find_gcd(-24, 18) == 6