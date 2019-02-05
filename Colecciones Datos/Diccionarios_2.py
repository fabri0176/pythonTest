# Diccionarios 2
colores = {"amarillo":"yellow","azul":"blue","verde":"green","rojo":"reed",}
print(colores['amarillo'])
print(colores.get("amarillo","no se encuentra"))
print(colores.get("negro","no se encuentra"))

# Buscar en colores
print('negro' in colores)

print(colores.keys())
print(colores.values())

print(colores.items())

for color in colores:
    print(colores[color])

for color in colores.keys():
    print(color)

for color in colores.values():
    print(color)

for clave,valor in colores.items():
    print(clave,valor)

# Diccionario de colores
print(colores.pop("amarillo","no se ha encontrado"))

print(colores.pop("negro","no se ha encontrado"))

colores.clear()
print(colores)

