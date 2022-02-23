
#calculo da media e validação de INPUT

n1 = float(input('digite a nota 1: '))
if n1 > 10.0 or n1 < 0.0:
    n1 = float(input('a nota eh invalidade. Digite a nota 1: '))

n2 = float(input('digite a nota 2: '))
if n2 > 10.0 or n2 < 0.0:
    n2 = float(input('a nota eh invalidade. Digite a nota 2: '))

n3 = float(input('digite a nota 3: '))
if n3 > 10.0 or n3 < 0.0:
    n3 = float(input('a nota eh invalidade. Digite a nota 3: '))

n4 = float(input('digite a nota 4: '))
if n4 > 10.0 or n4 < 0.0:
    n4 = float(input('a nota eh invalidade. Digite a nota 4: '))

nTotal = n1 + n2 + n3 +n4

media = nTotal/4

print('A media do aluno eh: {}'.format(media))

