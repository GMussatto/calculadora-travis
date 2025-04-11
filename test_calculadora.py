from calculadora import somar, subtrair, multiplicar, dividir, calcular
import pytest

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 2) == 3

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_calcular_soma():
    assert calcular("soma", 1, 1) == 2

def test_calcular_soma():
    assert calcular("soma", 1, 2) == 3

def test_calcular_subtracao():
    assert calcular("subtrai", 5, 3) == 2

def test_calcular_multiplicacao():
    assert calcular("multiplica", 3, 3) == 9

def test_calcular_divisao():
    assert calcular("divide", 8, 2) == 4

def test_calcular_operacao_invalida():
    with pytest.raises(ValueError):
        calcular("raiz", 2, 2)
