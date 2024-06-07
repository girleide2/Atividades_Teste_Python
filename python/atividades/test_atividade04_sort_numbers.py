import pytest
from atividade04_sort_numbers import sort_numbers

def test_sort_numbers_with_unsorted_list():
    assert sort_numbers([3, 1, 2]) == [1, 2, 3]

def test_sort_numbers_with_mixed_list():
    assert sort_numbers([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_sort_numbers_with_empty_list():
    assert sort_numbers([]) == []

def test_sort_numbers_with_sorted_list():
    assert sort_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_numbers_with_reversed_list():
    assert sort_numbers([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_numbers_with_duplicate_elements():
    assert sort_numbers([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

def test_sort_numbers_with_negative_numbers():
    assert sort_numbers([-1, -3, -2, 0, 2, 1]) == [-3, -2, -1, 0, 1, 2]

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade04_sort_numbers.py","-vv"])