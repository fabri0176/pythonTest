"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
import sys
if len(sys.argv) == 3:
    for arg in sys.argv:
        print("Argumentos correctos {}".format(arg))
else:
    print("Error faltan parametros")