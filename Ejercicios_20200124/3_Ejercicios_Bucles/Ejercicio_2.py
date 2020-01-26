"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad)."""

edad = int(input("Cual es su edad?:\t"))

for year in range(edad):

    print("Year {}".format(year+1))
