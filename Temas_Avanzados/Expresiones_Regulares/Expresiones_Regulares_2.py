import re
print("==============================================")
print("Si queremos comprobar varias posibilidades, podemos utilizar una tubería | a modo de OR. Generalmente pondremos el listado de alternativas entre paréntesis ():")
texto = "hola adios hello bye"

print(re.findall('hola|hello', texto))

print("==============================================")
def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )

patrones = ['hla', 'hola', 'hoola']
print(buscar(patrones, texto))
print("==============================================")
patrones = ['ho*', 'ho+']

print(buscar(patrones, texto))
print("==============================================")
patrones = ['ho*', 'ho+', 'ho?', 'ho?la']

print(buscar(patrones, texto))
print("==============================================")
texto = "hala hela hila hola hula"

patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
print(buscar(patrones, texto))
print("==============================================")