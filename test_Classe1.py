# Equipe: Francisco Alexandro, Gustavo Angelo, Matheus Ferreira

import pytest
from TP4Classe1 import ManipuladorDeString

StrFuncs = ManipuladorDeString()

def test_inverter():
    resultado = StrFuncs.inverter("Ola")
    assert resultado == "alO"

def test_contar_caracteres():
    resultado = StrFuncs.contar_caracteres("Vamos para a UECE hoje")
    assert resultado == 22

def test_minuscularizar():
    resultado = StrFuncs.minuscularizar("MAIÚSCULAS")
    assert resultado == "maiúsculas"

def test_maiuscularizar():
    resultado = StrFuncs.maiuscularizar("minúsculas")
    assert resultado == "MINÚSCULAS"

def test_capitalizar():
    resultado = StrFuncs.capitalizar("gato de botas 2")
    assert resultado == "Gato de Botas 2"

def test_substituir():
    resultado = StrFuncs.substituir("Amo muito tudo isso", "tudo isso", "todo mundo")
    assert resultado == "Amo muito todo mundo"

if __name__ == '__main__':
    pytest.main()
