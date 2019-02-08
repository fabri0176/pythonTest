from io import open

texto = ""

for i in range(25):
    texto += "Linea " + str(i)+"\n"

    print(texto)
print("==================================================")
fichero = open('fichero.txt','w+')
fichero.write(texto)
fichero.close()

print("==================================================")
fichero = open('fichero.txt','r')
fichero.seek(20) #ir al caracter 20
print(fichero.read())
fichero.seek(0) #ir al caracter 0
print(fichero.read(5)) #Leer 5 caracteres
print(fichero.read()) #Leer 5 caracteres
print("==================================================")
# Leer todo el texto y posicionarse en la mitda
fichero.seek(0) #ir al caracter 0
texto = fichero.read() #Leer 5 caracteres
print(fichero.seek(len(texto)/2))
print(fichero.read())
print("==================================================")
#Situarse al final de la primera linea
fichero.seek(0) #ir al caracter 0
print(fichero.seek(len(fichero.readline())))
print(fichero.read())
fichero.close()
print("==================================================")
#Abrir fuchichero y posicionarse en la primera posición
fichero = open('fichero.txt','r+')
fichero.write('Linea 1 Custom')
print(fichero.read())
fichero.close()
print("==================================================")
fichero = open('fichero.txt','r+')
lineas = fichero.readlines()
lineas[2] = "Esta linea la he modificado en memoria"
fichero.seek(0)
fichero.writelines(lineas)
fichero.close()
