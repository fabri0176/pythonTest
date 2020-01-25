# http://aprendeconalf.es/python/ejercicios/tipos-datos.html
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
# muestre por pantalla el capital obtenido en la inversión.

dineroInversion = input("Dinero a invertir:\t")
dineroInversion = float(dineroInversion)

interesAnual = input("Interes anual:\t")
interesAnual = float(interesAnual)

numAnyos = input("Número de años:\t")
numAnyos = float(numAnyos)

capitalObtenido = round(dineroInversion*(interesAnual/100+1)**numAnyos,2)

print("De la inversion en ${} a interes {} en {} años, el capital obtenido es de {}".format(dineroInversion,interesAnual,numAnyos,capitalObtenido))