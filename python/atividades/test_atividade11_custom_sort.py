import pytest
from atividade11_custom_sort import custom_sort

def test_custom_sort_regular_list():
    assert custom_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

def test_custom_sort_sorted_list():
    assert custom_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_custom_sort_reverse_sorted_list():
    assert custom_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_custom_sort_empty_list():
    assert custom_sort([]) == []

def test_custom_sort_single_element_list():
    assert custom_sort([42]) == [42]

def test_custom_sort_with_negative_numbers():
    assert custom_sort([3, -1, 4, 1, -5, 9, 2, -6, 5, 3, 5]) == [9, 5, 5, 4, 3, 3, 2, 1, -1, -5, -6]

def test_custom_sort_with_duplicates():
    assert custom_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

def test_custom_sort_with_floats():
    assert custom_sort([3.1, 2.4, 5.5, 3.3, 2.1]) == [5.5, 3.3, 3.1, 2.4, 2.1]

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade11_custom_sort.py","-vv"])
