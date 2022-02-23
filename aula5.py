#listas e tuplas

from turtle import pensize


lista = [1 , 7 ,13 , 19]
lista_comida = ['bolo' , 'chocolate', 'pao']


for i in lista:
  print(i)

print('maior numero: {}' .format(max(lista)))
print('menor numero: {}' .format(min(lista)))
print('soma da lista: {}'.format(sum(lista)))


print('por ordem alfabetica min lista str: {}'.format(min(lista_comida)))
print('por ordem alfabetica max lista str: {}'.format(max(lista_comida)))

if 7 in lista:
    print('existe o 7 na lista')
else:
    print('nao existe o 7 na lista')

if 27 in lista:
    print('exite o 27 na lista')
else:
    print('nao existe o 27 na lista')
    lista.append(27)

print(lista)
print('o 27 fooi incluido na lista')

#lista.pop() -> remove o ultimo conteudo e posição da lista ou posso especificar a posição para remover

#lista.sort() -> ordem a lista

#tupla é uma lista que é imutavel, é usado parenteses ao inves de colchetes

tupla = (1 , 2 ,3, 13)