num_1 = float(input("Ingrese un número: "))
num_2 = float(input("Introduce otro número: "))

print("Seleccione la opción a mostrar")
print("1 - Suma de dos números: ")
print("2 - Resta de dos números")
print("3 - Multiplicación de los números")

opcion = int(input("Introduce una opción: "))
if opcion==1:
    print("la suma de num_1 + num_2 = ",num_1+num_2)
elif opcion==2:
    print("la resta de num_1 - num_2 = ",num_1-num_2)
elif opcion==3:
    print("La multiplicación de num_1 x num_2 = ",num_1*num_2)
else:
    print("Opción no válida")



