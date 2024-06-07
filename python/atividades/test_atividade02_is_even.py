import pytest
from atividade02_is_even import is_even

def test_is_even_with_even_number():
    assert is_even(4) == True

def test_is_even_with_odd_number():
    assert is_even(5) == False

def test_is_even_with_zero():
    assert is_even(0) == True

def test_is_even_with_negative_even_number():
    assert is_even(-4) == True

def test_is_even_with_negative_odd_number():
    assert is_even(-5) == False

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade02_is_even.py","-vv"])