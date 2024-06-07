import pytest
from atividade03_find_max import find_max

def test_find_max_with_positive_numbers():
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_with_negative_numbers():
    assert find_max([-1, -2, -3, -4, -5]) == -1

def test_find_max_with_empty_list():
    assert find_max([]) == None

def test_find_max_with_mixed_numbers():
    assert find_max([-1, 0, 1, -2, 2]) == 2

def test_find_max_with_single_element():
    assert find_max([42]) == 42

def test_find_max_with_repeated_elements():
    assert find_max([3, 3, 3, 3, 3]) == 3

def test_find_max_with_large_numbers():
    assert find_max([1000000, 5000000, 10000000, 2000000]) == 10000000

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade03_find_max.py","-vv"])