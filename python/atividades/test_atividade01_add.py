import pytest
from atividade01_add import add

def test_add_numeros_positivos():
    assert add(1, 2) == 3

def test_add_numeros_negativos():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positivo_e_negativo():
    assert add(1, -1) == 0

def test_add_numeros_grandes():
    assert add(1000, 2000) == 3000
    
if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade01_add.py","-vv"])