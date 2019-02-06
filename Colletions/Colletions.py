from collections import Counter
from collections import defaultdict
l = [1,2,3,4,5,6,1,2,3,4,4,4,7 ,7 ,8 ,8]
print(l)
print(Counter(l))

p = "Palabra"
print(Counter(p))

animales = "gato perro canario perro canario"

print(Counter(animales.split()))
c = Counter(animales.split())

print(c.most_common(1))
print(c.most_common())
print(c.values())
print(list(c))

# Tipo diccionario
print(dict(c))

# Diccionarios por defecto
d = defaultdict(object,{'algo':'hoy'})
print(d['algo'])

print(d['despues'])

dListaDefecto = defaultdict(int)
print(dListaDefecto['33434'])

n = {}
n['dos'] = 'two'
n['uno'] = 'one'
n['tres'] = 'tree'

from  collections import OrderedDict

print(OrderedDict(n))

from  collections import namedtuple
Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Hector",apellido="Costa",edad=27)
print("================================")
print(p.nombre)
print(p.apellido)
print(p.edad)
print("================================")
print(p[0])
print(p.apellido)
print(p.edad)
print("================================")

