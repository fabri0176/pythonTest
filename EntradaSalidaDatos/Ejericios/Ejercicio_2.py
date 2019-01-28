# python Ejercicio_2.py 2 5
import sys

print(sys.argv)

if(len(sys.argv) == 3):
    filas = int(sys.argv[1])
    columna = int(sys.argv[2])

    if((filas >=1 and filas <= 9 ) and (columna >= 1 and columna <= 9)):
        print("Correcto")
        for f in range(filas):
            for c in range(columna):
                print("*",end='')
            print("")
    else:
        print("Filas o Columnas incorrecto")
else:
    print("Argumentos incorrectos")