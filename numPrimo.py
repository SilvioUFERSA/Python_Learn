#imprimir todos os primos de 1 a 100

for num in range(101):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0 :
            div = div + 1
    
    if div == 2:
        print(num)