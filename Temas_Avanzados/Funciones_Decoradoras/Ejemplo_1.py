def hola():
    numero = 50
    def bienvenido():
        return "Hola!"

    print( locals() )

    return bienvenido

print(hola())
