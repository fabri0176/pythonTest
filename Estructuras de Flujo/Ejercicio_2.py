lista = list(range(0,101,2))
print(sum(lista))

suma = 0
for num in lista:
    suma += num
print(suma)
suma = 0
i = 0
while(i<len(lista)):
    suma += lista[i]
    i += 1

print(suma)