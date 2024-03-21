import pytest

def suma_enteros(a,b):
    resultado = a + b
    print("Se suma ", a, "+", b, "que da",resultado)

@pytest.mark.test
def test_suma_iguales():
    assert suma_enteros(2, 2) == 7
