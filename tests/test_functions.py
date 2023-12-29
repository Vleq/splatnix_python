from src.functions import (
    add_numbers,
	subtract_numbers.
)


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_subtract_numbers():
    assert subtract_numbers(3, 2) == 1
