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

exemplo = "Amo muito tudo isso"


print("String original:", exemplo)
print("String invertida:", StrFuncs.inverter(exemplo))
print("Número de caracteres:", StrFuncs.contar_caracteres(exemplo))
print("String em minúsculas:", StrFuncs.minuscularizar(exemplo))
print("String em maiúsculas:", StrFuncs.maiuscularizar(exemplo))
print("String capitalizada:", StrFuncs.capitalizar(exemplo))
print("String substituída:", StrFuncs.substituir(exemplo, "exemplo", "amostra"))
