# conjuntos -> definido por {}

conjunto = {1, 2 ,3 ,5 ,7 }

conjunto.add(11)
conjunto.discard(1)

conjunto2 = {7 ,13 , 17 ,19 }

conjunto_uniao = conjunto.union(conjunto2)

print(conjunto)

print(conjunto_uniao)

conjunto_intercessao = conjunto.intersection(conjunto2)
print(conjunto_intercessao)

conjunto_diference = conjunto.difference(conjunto2)
print(conjunto_diference)