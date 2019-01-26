decimal = float(input("Ingresa un número decimal con . : "))
print(decimal)

valores = []
print("Introduce 4 valores: ")
for x in range(4):
    valores.append(float(input(str(x+1)+" - Ingresa un valor número decimal con punto '.' :")))

print(valores)