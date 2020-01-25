# http://aprendeconalf.es/python/ejercicios/condicionales.html
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la
# contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.

password = "Inglaterra.12".lower()
getPass = input("Enter your password:\t")
getPass = getPass.strip()


if len(getPass) > 0:
    if(getPass.lower() == password):
        print("Su contraseña es correcta")
    else:
        print("Su contraseña no es correcta")
else:
    print("Debe ingresar una cotraseña valida")