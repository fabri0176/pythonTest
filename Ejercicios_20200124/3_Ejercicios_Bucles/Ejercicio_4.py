"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla la cuenta atrás desde ese número
hasta cero separados por comas."""

number = int(input("Enter a number:\t"))
string = ""
for num in range(number*-1, 1):
    string += "{},".format(num)

print("The numbers is{}".format(string))
