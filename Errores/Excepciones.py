print("----------------------")
try:
    n = float(input("Ingrese un número: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Error desconocido")

print("----------------------")

while(True):
    try:
        n = float(input("Ingrese un número: "))
        m = 4
        print("{}/{}={}".format(n, m, n / m))
        break
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo a funcionado correctamente")
        break

print("----------------------")
print("----------------------")

while(True):
    try: #Captura cualquier error
        n = float(input("Ingrese un número: "))
        m = 4
        print("{}/{}={}".format(n, m, n / m))
        break
    except: #defino código expecional
        print("Ha ocurrido un error, introduce bien el número")
    else: #definir codigo sino hay error
        print("Todo a funcionado correctamente")
        break
    finally: #Ejecutar codigo haya o no haya error
        print("Fin de la iteración")
print("----------------------")