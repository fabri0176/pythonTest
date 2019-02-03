lista_original = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

def modificar(lista):
    print("====================================")
    print("Lista original",lista)
    # Borrar elementos duplicados
    lista = list(set(lista))
    print("====================================")
    print("Lista sin elementos duplicados",lista)

    #Ordenar la lista de mayor a menor
    lista.sort(reverse=True)
    print("====================================")
    print("Lista ordenada de mayor a menor", lista)

    #Eliminar todos los numeros impares
    for indice,valor in enumerate(lista):
        if valor % 2 != 0:
            del(lista[indice])
    print("====================================")
    print("Elimiando números impares de la lista", lista)

    # realizar la suma de todos los numeros que quedan
    suma = sum(lista)
    print("====================================")
    print("La suma de la lista es igual {}".format(lista))

    lista.insert(0,suma)
    # Devolver la lista

    return lista

lista = modificar(lista_original)

print("====================================")
print("Lista retorna =",lista)
print("Lista Original =",lista_original)

print(lista[0] == sum(lista[1:]))