# aula de métodos, funções e classes.
# um metodo eh parecido com uma func , para usar o metodo utilizamos a palavra reservada DEF

class Calculadora:

    def __init__(self, num1, num2): #construtor -> passando as informações recebidas para serem usadas nas class atras vez de valor1 e valor2
        self.valor1 = num1 #passando meu 6 para a class usar em valor1
        self.valor2 = num2 #passando meu 3 para a class usar em valor2
    
    def soma (self):
        return self.valor1 + self.valor2

    def subtracao (self):
        return self.valor1 - self.valor2
    
    def multiplicacao (self):
        return self.valor1 * self.valor2

    def divisao (self):
        return self.valor1 / self.valor2

calculadora = Calculadora (6 , 3)

print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(int(calculadora.divisao()))