conjunto = set() #Creando un cojunto vacio
conjunto.add(1)
conjunto.add(2)
print(conjunto)

# Descartar valor de un conjunto
conjunto.discard(1)

# Copiar conjunto a otro conjunto
conjunto2 = conjunto.copy()

# clear, limpiar
conjunto2.clear()
print(conjunto2)

# Metodo para saber si un conjunto disjunto,
conjunto_1 = {1,2,3}
conjunto_2 = {3,4,5}
conjunto_3 = {-1,99}
conjunto_4 = {1,2,3,4,5}

print(conjunto_1.isdisjoint(conjunto_3))
print(conjunto_1.isdisjoint(conjunto_2))
print(conjunto_1.isdisjoint(conjunto_4))
print(conjunto_4.issuperset(conjunto_1))
print(conjunto_4.issuperset(conjunto_2))
print(conjunto_4.issuperset(conjunto_3))

# Metodos para relaizar uniones entre conjuntos
print(conjunto_1.union(conjunto_2) == conjunto_4)

conjunto_1.update(conjunto_2)
print(conjunto_1)

# Buscar elemntos no comunes
print(conjunto_1.difference(conjunto_2))

# Guarda los elementos que no tiene el conjunto 1 del conjunto 2
conjunto_1.difference_update(conjunto_2)
print(conjunto_1)
conjunto_1.intersection(conjunto_3)

# Ver elementos simetricos, que no concuerdan entre conjuntos, retorna todos los elementos que no cocncuerdan entre los conjuntos
print(conjunto_1.symmetric_difference(conjunto_2))
