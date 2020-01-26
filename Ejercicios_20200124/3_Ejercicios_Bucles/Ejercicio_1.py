"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""Escribir un programa que pida al usuario una palabra y la muestre por
pantalla 10 veces."""

palabra = input("Ingrese una palabra:\t")

for x in range(1, 11):
    print("{} - {}".format(x, palabra))
