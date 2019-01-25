num_introducir = int(input("Cuantos números desea introducir?: "))
suma = 0

for x in range(num_introducir):
    suma += float(input("Introduce el número "+ str(x) +" : "))

print("La suma de los "+str(x)+" números es "+str(suma)+" y la media es "+str(suma/num_introducir))