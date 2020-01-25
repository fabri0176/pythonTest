# http://aprendeconalf.es/python/ejercicios/condicionales.html
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el
# programa debe mostrar un error.

dividendo = float(input("Ingrese número 1: "))
divisor = float(input("Ingrese número 2: "))
if divisor != 0.0:
    resultado = round(dividendo/divisor,2)
    print("El resultado de {}/{} = {}".format(dividendo,divisor,resultado))
else:
    print("Error el divisor no puede ser sero o vacio")
