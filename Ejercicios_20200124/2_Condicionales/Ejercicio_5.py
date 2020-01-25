# http://aprendeconalf.es/python/ejercicios/condicionales.html
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y
# el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el
# grupo que le corresponde.

name = input("Enter your name:\t")
name = (name.strip()).lower()

gender = input("Enter your gender [F] - [M]:\t")
gender = gender.upper()

if gender == "F" or gender == "M":
    if gender == "F":
        if name[0] < "m":
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
    elif gender == "M":

        if name[0] > "n":
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
else:
    print("No valid gender")


