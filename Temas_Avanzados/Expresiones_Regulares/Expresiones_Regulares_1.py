import re

texto = "En esta cadena se encuentra una palabra mágica"

print(re.search('mágica', texto))

print("==============================================")
palabra = "mágica"

encontrado = re.search(palabra,  texto)

if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra)
print("==============================================")
# Posición donde empieza la coincidencia
print( encontrado.start() )
# Posición donde termina la coincidencia
print( encontrado.end() )
# Tupla con posiciones donde empieza y termina la coincidencia
print( encontrado.span() )
# Cadena sobre la que se ha realizado la búsqueda
print( encontrado.string )
print("==============================================")
texto = "Hola mundo"

re.match('Hola', texto)
print("==============================================")
print("DIVIDIR CADENA")
texto = "Vamos a dividir esta cadena"

print(re.split(' ', texto))
print("==============================================")
print("re.sub: sustituye todas las coincidencias en una cadena:")
texto = "Hola amigo"

print(re.sub('amigo', 'amiga', texto))
print("==============================================")
print("re.findall: busca todas las coincidencias en una cadena:")
texto = "hola adios hola hola"

re.findall('hola', texto)
print("==============================================")