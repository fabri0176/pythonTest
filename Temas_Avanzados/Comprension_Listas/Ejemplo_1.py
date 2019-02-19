lista = []
for letra in 'casa':
    lista.append(letra)

print(lista)

lista = [letra for letra in 'casa']
print(lista)

lista2 = [letra*2 for letra in range(0,66)]
print(lista2)

lista3 = [numero**2 for numero in range(0,20) if numero%2 ==0]
print(lista3)

# Con comprensión de listas
lista = [numero for numero in 
            [numero**2 for numero in range(0,11)]
                if numero % 2 == 0 ]
print(lista)

