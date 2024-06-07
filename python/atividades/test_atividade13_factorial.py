import pytest
from atividade13_factorial import factorial

def test_factorial_with_positive_integer():
    assert factorial(5) == 120

def test_factorial_with_zero():
    assert factorial(0) == 1

def test_factorial_with_negative_integer():
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        factorial(-5)

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade13_factorial.py","-vv"])
