try:
    colores = {'rojo':'red','verde':'green','negro':'black'}
    colores['blanco']
except KeyError:
    print("Error: Indice del diccionario no válido")