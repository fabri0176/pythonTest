from io import open
import datetime

texto = "Una línea con texto\nOtra línea con texto"

fichero = open('fichero.txt','w+')
fichero.write(texto)
fichero.close()
del(fichero)

fichero = open('fichero.txt','r')
texto = fichero.read()
fichero.close()
print(texto)
del(fichero)


def write_log(cadena,nombre):
    fecha_actual = datetime.datetime.now()
    file_name = fecha_actual.strftime("log_%Y_%m_%d")+".log"
    log = "[{}][{}]: {}\n".format(fecha_actual.strftime("%Y-%m-%d %H:%M:%S"),nombre,cadena)
    fichero = open(file_name,'a')
    fichero.write(log)
    fichero.close()


for i in range(100):
    write_log("Línea "+str(i),"write_log")

# Leer todas las lineas de un fichero
fichero = open('fichero.txt','r')
lineas = fichero.readlines()
fichero.close()

print(lineas)

if len(lineas)>0:
    for linea in lineas:
        write_log("Agregando Linea " + str(i), "write_log")
        print(linea)

fichero = open('fichero.txt','r')
l = fichero.readline()

fichero.close()

with open('fichero.txt','r') as fichero:
    for linea in fichero:
        print(linea)