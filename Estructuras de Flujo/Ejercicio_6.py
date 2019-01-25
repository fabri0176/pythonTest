# AGREGAR A LA 3 LISTA LETRAS QUE NO SE REPITEN DE LAS DOS LISTAS
lista_1 = ["h",'o','l','a',' ','m','u','n','d','o']
lista_2 = ["h",'o','l','a',' ','m','u','n','a']

lista_3 = []

print(lista_3)

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3 :
        lista_3.append(letra)

print(lista_3)
    