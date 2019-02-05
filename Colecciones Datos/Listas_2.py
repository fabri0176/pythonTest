lista = []
lista.append(6)

print(lista)

lista.clear()

print(lista)

l1 = [1,2,3]
l2 = [4,5,6]

print(l1)
print(l2)

# Union de listas
l1.extend(l2)
print(l1)

#contar cuantas veces aparece un elemento en un lista
lista_2 = ["Hola","mundo","mundo"]
print("La palabra mundo aparece {} veces".format(lista_2.count("mundo")))

# Buscar el indice donde aparece una ocurrrencia en una lista
lista_3 = ["Hola","mundo","mundo"]
print(lista_3.index("Hola"))
print(lista_3.index("mundo"))

#Agregar un elemnto a lista en una posicion
l1 = [1,2,3]
l1.insert(0,0)
print(l1)

#Ante penultimo insert
l2=[5,10,15,25]
l2.insert(-1,20)
print(l2)

l2.insert(6,30)
print(l2)

# Sacar valor de lista con indicando indice
l = [10,20,30,40,50]
print(l.pop())
print(l.pop(1))

# eliminar indicando valor de la lista
l.remove(30)
print(l)

# Reverse. dar reversa a una lista
l.reverse()
print(l)

lista = list("Hola Mundo")
lista.reverse()
print(lista)

cadena = "".join(lista)
print(cadena)

lista = [5,-10,35,0,-65,100]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


