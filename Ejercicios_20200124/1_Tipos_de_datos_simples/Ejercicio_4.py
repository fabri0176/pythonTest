# http://aprendeconalf.es/python/ejercicios/tipos-datos.html
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en
# líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Nombre: {}\n".format(nombre)*edad)
print("Edad: {}".format(edad))