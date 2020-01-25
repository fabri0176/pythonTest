# http://aprendeconalf.es/python/ejercicios/tipos-datos.html
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y
# lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
# índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Ingrese su peso en kg:\t"))
estatura = float(input("Ingrese su estatura en Metros:\t"))

indiceMasaCorporal = round((peso/(estatura**2)),2)

print("Su IMC:\t{}".format(indiceMasaCorporal))