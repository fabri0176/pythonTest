class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde afuera")

    def metodo_publico(self):
        self.__metodo_privado()

    def getAtributoPrivado(self):
        print(self.__atributo_privado)
e = Ejemplo()
e.metodo_publico()
e.getAtributoPrivado()