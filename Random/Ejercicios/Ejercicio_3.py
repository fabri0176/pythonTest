# Generador

def leer_numero(ini, fin,mensaje):
    while True:
        try:
            valor = int( input("Ingrese un número: ") )
        except TypeError:
            print("Número no válido")
        else:
            if valor >= ini and valor <= fin:
                break
    return  valor

leer_numero(3,5,"Exacelente")

def generador():
    numeros = leer_numero(1,20,"¿Cuantos número quieres generar?")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al Alza [2]A la baja [3]Normal:")

generador()