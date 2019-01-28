from collections import deque
#SIMULAR PILAS
pila = [3,4,5]
pila.append(6)
pila.append(7)

print(pila)

#Extraer elemenots de una pila
n = pila.pop() #Último elemento y lo borra
print(pila)
print(n)

while len(pila) > 0:
    eliminado = pila.pop()
    print(eliminado)

#COLAS
cola = deque()
print(cola)

cola = deque(['Hector','Juan','Migue'])
print(cola)

cola.append('Maria')
cola.append('Arnaldo')
print(cola)

#Sacar elemento de la cola
salio = cola.popleft()
print(salio)
print(cola)


while len(cola) > 0:
    salio = cola.popleft()
    print("Salio del turno: "+salio)









