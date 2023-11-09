# Equipe: Francisco Alexandro, Gustavo Angelo, Matheus Ferreira

import pytest
from TP4Classe2 import Calculadora

calc = Calculadora(5, 3)

def test_adicao():
    resultado = calc.adicao()
    assert resultado == 8

def test_subtracao():
    resultado = calc.subtracao()
    assert resultado == 2

def test_multiplicacao():
    resultado = calc.multiplicacao()
    assert resultado == 15

def test_divisao():
    resultado = calc.divisao()
    assert resultado == 1.6666666666666667

def test_divisaoInteira():
    resultado = calc.divisaoInteira()
    assert resultado == 2

def test_potencia():
    resultado = calc.potencia()
    assert resultado == 125

if __name__ == '__main__':
    pytest.main()
