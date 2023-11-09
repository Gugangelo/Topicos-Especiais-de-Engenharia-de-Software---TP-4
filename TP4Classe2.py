# Equipe: Francisco Alexandro, Gustavo Angelo, Matheus Ferreira

class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        pass

    def adicao(self):
        return self.n1 + self.n2

    def subtracao(self):
        return self.n1 - self.n2

    def multiplicacao(self):
        return self.n1 * self.n2

    def divisao(self):
        if self.n2 == 0:
            print("Divisor não pode ser zero.")
        else:
            return self.n1 / self.n2

    def divisaoInteira(self):
        if self.n2 == 0:
            print("Divisor não pode ser zero.")
        else:
            return self.n1 // self.n2
        
    def potencia(self):
        return self.n1 ** self.n2



calc = Calculadora(5, 3)

print("Resultado da adição:", calc.adicao())
print("Resultado da subtração:", calc.subtracao())
print("Resultado da multiplicação:", calc.multiplicacao())
print("Resultado da divisão:", calc.divisao())
print("Resultado da divisão inteira:", calc.divisaoInteira())
print("Resultado da potencia:", calc.potencia())
