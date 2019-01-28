# python Ejercicio_3.py 2
import sys

print(sys.argv)

if (len(sys.argv) == 0):
    print("Debe ingresar un Entero positvo Ejemplo: python Ejercicio_3.py 2")
elif (len(sys.argv) < 2):
    print("Faltan Argumentos")
else:
    if (int(sys.argv[1]) < 0 or int(sys.argv[1]) > 9999):
        print("El argumento debe ser un entero positivo de [0-9999]")
    else:
        numero = sys.argv[1]
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print("{:04}".format(int(cadena[longitud - 1 - i]) * 10 ** i))

