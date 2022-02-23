from turtle import pensize


print("hello word")
a = int ( input('primeiro valor: ') )
b = int ( input('\nsgundo valor:') )
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print ('soma : {}' .format(soma))
# ou print('soma : ' + str(soma))
print('subtracao : {}' .format(subtracao))
# ou print('soma : ' + str(subtracao))

# ou podemos usar: 

resultado = ('Soma : {} \nSubtracao : {}  \nDivisao : {} \nMultiplicacao : {} \nResto : {}' .format(soma, subtracao, multiplicacao, divisao, resto ))

print(resultado)

#print ('multiplicacao : ' + str(multiplicacao))
#print ('divisao : ' + str(divisao))
#print('resto : ' + str(resto))