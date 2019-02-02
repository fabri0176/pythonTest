class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas


    def __str__(self):
        return "color {}, {} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)

        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc".format(self.color,self.velocidad,self.ruedas,self.cilindrada)

c = Coche("azul",150,4,1200)
print(c)



class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def __str__(self):
        return  super().__str__()+", {} kg de carga".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return  super().__str__()+", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad, cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

        def __str__(self):
            return super().__str__() + ", {} k/h con {} cc cilindrada ".format(self.velocidad, self.cilindrada)

    def __str__(self):
        return  super().__str__()+", {}".format(self.tipo)

vehiculos = [
    Coche("Azuk",4,150,1250),
    Camioneta("Blanco",4,100,1400,1500),
    Bicicleta("Verde",2,"Urbana"),
    Motocicleta("Negro",2,"Deportiva",180,900)
]

# def catalogar(lista):
#     for vehiculo in lista:
#         # print(type(vehiculo).__name__)
#          print("{} {}".format(type(vehiculo).__name__,vehiculo))


# catalogar(vehiculos)

def catalogar(lista, Ruedas = None):
    contador = 0
    if Ruedas != None:

        for v in lista:
            if (v.ruedas == Ruedas):
                contador += 1

        print("Se han encontrado {} resultados con ".format(contador,Ruedas))
        print("============================================================")

    for vehiculo in lista:
        # print(type(vehiculo).__name__)
        if(Ruedas==None):
            print("{} {}".format(type(vehiculo).__name__,vehiculo))
        else:
            if (vehiculo.ruedas == Ruedas):
                print("{} {}".format(type(vehiculo).__name__, vehiculo))

    print("")


catalogar(vehiculos,4)