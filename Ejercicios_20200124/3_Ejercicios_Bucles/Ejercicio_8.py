"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo."""

number = int(input("Input a number:\t"))

for i in range(1, number+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")