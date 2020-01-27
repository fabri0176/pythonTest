"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""
Escribir un programa que pida al usuario un número entero y muestre 
por pantalla un triángulo rectángulo como el de más abajo, de altura 
el número introducido."""

numberLines = int(input("Enter number lineas: "))
i = 1
if numberLines > 0:
    for line in range(numberLines):
        print("*"*i)
        i += 1
else:
    print("ERROR")