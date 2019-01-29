try:
    lista = [1,2,3,4,5]
    lista[10]
except IndexError:
    print("Error, el indice no existe, ingrese un indice correcto")