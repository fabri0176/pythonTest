# 1;Carlos;Pérez;05/01/1989
# 2;Manuel;Heredia;26/12/1973
# 3;Rosa;Campos;12/06/1961
# 4;David;García;25/07/2006
from io import open

fichero = open('personas.txt','r', encoding="utf8")
lineas = fichero.readlines()
fichero.close()

personas = []
for linea in lineas:
    # Borramos los saltos de línea y separamos
    campos = linea.replace("\n", "").split(";")  
    persona = {"id": campos[0], "nombre": campos[1], "apellido": campos[2], "nacimiento": campos[3]}
    personas.append(persona)

for p in personas:
    print("(id={}) {} {} => {} ".format(p['id'], p['nombre'], p['apellido'], p['nacimiento']))