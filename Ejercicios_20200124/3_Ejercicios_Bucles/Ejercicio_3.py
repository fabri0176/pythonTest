"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números impares desde 1
hasta ese número separados por comas."""

number = int(input("Enter a number:\t"))


if number > 0:
    numberNoEven = ""
    for num in range(number):
        numCalc = num + 1
        isPar = numCalc % 2
        if isPar == 1:
            numberNoEven = numberNoEven + "{},".format(numCalc)

    print("The number {} is not even".format(numberNoEven))
else:
    print("Enter a positive number")
