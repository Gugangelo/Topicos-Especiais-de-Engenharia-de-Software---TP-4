# Equipe: Francisco Alexandro, Gustavo Angelo, Matheus Ferreira

class ManipuladorDeString:
    def __init__(self):
        pass

    def inverter(self, str):
        return str[::-1]

    def contar_caracteres(self, str):
        return len(str)

    def minuscularizar(self, str):
        return str.lower()

    def maiuscularizar(self, str):
        return str.upper()

    def capitalizar(self, str):
        return str.title()

    def substituir(self, str, antiga, nova):
        return str.replace(antiga, nova)

StrFuncs = ManipuladorDeString()

ex = "Vamos para a UECE"


print("String original:", ex)
print("String invertida:", StrFuncs.inverter(ex))
print("Número de caracteres:", StrFuncs.contar_caracteres(ex))
print("String em minúsculas:", StrFuncs.minuscularizar(ex))
print("String em maiúsculas:", StrFuncs.maiuscularizar(ex))
print("String capitalizada:", StrFuncs.capitalizar(ex))
print("String substituída:", StrFuncs.substituir(ex, "ex", "amostra"))
