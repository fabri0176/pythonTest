def separar(lista):
    lista.sort()
    pares=[]
    impares=[]

    for numero in lista:
        if numero %2==0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares,impares



lista = [-12,84,13,20,-33,101,9]
pares, impares = separar(lista)
print("Pares = "+ pares.__str__())
print("Impares ="+impares.__str__())