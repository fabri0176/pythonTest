from io import open

texto = "Una línea con texto\nOtra línea con texto"

fichero = open('fichero.txt','w')
fichero.write(texto)
fichero.close()
del(fichero)

fichero = open('fichero.txt','r')
texto = fichero.read()
fichero.close()
print(texto)
del(fichero)
