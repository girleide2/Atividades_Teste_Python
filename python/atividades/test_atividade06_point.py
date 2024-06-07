import pytest
from atividade06_point import Point

def test_distancia_ao_mesmo_ponto():
    p1 = Point(1, 1)
    assert p1.distance_to(p1) == 0

def test_distancia_a_pontos_diferentes():
    p1 = Point(1, 1)
    p2 = Point(4, 5)
    assert p1.distance_to(p2) == pytest.approx(5.0, abs=1e-2)

def test_distancia_a_pontos_negativos():
    p1 = Point(-1, -1)
    p2 = Point(-4, -5)
    assert p1.distance_to(p2) == pytest.approx(5.0, abs=1e-2)

def test_distancia_a_linha_horizontal():
    p1 = Point(1, 1)
    p2 = Point(5, 1)
    assert p1.distance_to(p2) == 4

def test_distancia_a_linha_vertical():
    p1 = Point(1, 1)
    p2 = Point(1, 5)
    assert p1.distance_to(p2) == 4

def test_distancia_com_argumento_invalido():
    p1 = Point(1, 1)
    with pytest.raises(ValueError):
        p1.distance_to(42)
        
if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade06_point.py","-vv"])
