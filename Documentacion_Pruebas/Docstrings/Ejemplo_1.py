def hola(arg):
    """Este es docstring de la función"""
    print("Hola",arg,"!")

hola("amor")
help(hola)

print("=================================================")
class Clase:
    """Este es el docstring de la clase"""
    def __init__(self):
        """Este es el docstring del inicializador"""
        pass

    def metodo(self):
        """Este es el docstring del metodo de clase"""
        pass

o = Clase()
help(o)
print("=================================================")


