# Diccionarios
vacio = {}
print(vacio)

print(type(vacio))

colores = {'amarillo':'yellow','azul':'blue','verde':'green'}

print(colores['azul'])
print(colores['amarillo'])
print(colores['azul'])


colores['amarillo'] = 'white'
print(colores)

del(colores['amarillo'])
print(colores)

edades = {"Hector":27,"Juan":45,"Maria":30}
print(edades)
print(len(edades))


print(edades)
print(len(edades))

for clave in edades:
    print("La edad de "+clave+" es "+str(edades[clave]))

for clave,valor in edades.items():
    print("La edad de " + clave + " es " + str(valor))

# LISTA DE PERSONAJES
personajes = []
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}

personajes.append({'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'})
personajes.append({'Nombre':'Néstor','Clase':'Ing','Raza':'Gato'})
personajes.append({'Nombre':'Legolas','Clase':'Mago','Raza':'Enano'})

print(personajes)

for personajes in personajes:
    print("El personaje "+personajes['Nombre']+" es "+personajes['Clase']+" Raza "+personajes['Raza'])