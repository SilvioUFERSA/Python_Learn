# LAÇOS DE REPETIÇÃO : FOR, WHILE, RANGE

#exemplo: calculo do numero primo com um for

# um dos jeitos dos numero ser primo é ter certeza que ele so pode ser divisivel por 1 e por ele mesmo, ou seja  não pode ser divisível por mais do que 2 condições.

a = int(input('digite um nuermo: '))

div = 0

for x in range(1, a+1):
    resto = a % x
    print(x , resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print('o numero {} eh primo'. format(a))
else:
    print('o numero {} nao eh primo'. format (a))



#imprimir todos os primos de 1 a 100

#num = 100
#div = 0

#for num in range ( 101 ):
 #   for x in range ( 1, num + 1):
 #       resto = num % x

  #      if resto == 2:
   #         print(num)