#outra forma de fazer uma calculadora sem precisar colocar uma intância para os valores

class Calculadora:

    def __init__(self):
        pass 
    
    def soma (self, valor1, valor2):
        return valor1 + valor2

    def subtracao (self, valor1, valor2):
        return valor1 - valor2
    
    def multiplicacao (self, valor1 , valor2):
        return valor1 * valor2

    def divisao (self, valor1, valor2):
        return valor1 / valor2

calculadora = Calculadora () #tiramos os valor da instancia em que antes tribuiamos no __init__

print(calculadora.soma(6,3)) #e agora passamos diretamente como parametro para os metodos
print(calculadora.subtracao(6,3))
print(calculadora.multiplicacao(6,3))
print(int(calculadora.divisao(6,3)))