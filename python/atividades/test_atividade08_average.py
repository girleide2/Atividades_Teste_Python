import pytest
from atividade08_average import calculate_average

def test_calculate_average_with_valid_list():
    numbers = [1, 2, 3, 4, 5]
    assert calculate_average(numbers) == 3.0

def test_calculate_average_with_single_number():
    numbers = [5]
    assert calculate_average(numbers) == 5.0

def test_calculate_average_with_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    assert calculate_average(numbers) == -3.0

def test_calculate_average_with_zero():
    numbers = [0, 0, 0, 0, 0]
    assert calculate_average(numbers) == 0.0

def test_calculate_average_with_empty_list():
    with pytest.raises(ValueError, match="The list of numbers cannot be empty"):
        calculate_average([])

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade08_average.py","-vv"])
