def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Error tipo dato no válido")
    else:
        return r

def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Error tipo dato no válido")
    else:
        return r

def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print("Error tipo dato no válido")
    else:
        return r

def division(a,b):
    try:
        r = a / b
    except TypeError:
        print("Error tipo dato no válido")
    except ZeroDivisionError:
        print("No es posible dividir por 0 (Cero)")
    else:
        return r