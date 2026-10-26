import importlib
import pytest

transpose_matrix = (
    importlib.import_module("39_transpose_matrix").transpose_matrix
)


def test_square_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_rectangular_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]


def test_empty_matrix():
    assert transpose_matrix([]) == []


def test_ragged_matrix_raises_error():
    with pytest.raises(ValueError):
        transpose_matrix([[1, 2], [3]])