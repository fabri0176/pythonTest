class Galleta:
    chocolate = False


    def __init__(self,sabor=None,color=None):
        self.sabor = sabor
        self.color = color
        if(sabor is not None and color is not  None):
            print("Se acaba de crear una galleta sabor {} y color {}".format(sabor, color))

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una galleta chocolateada")
        else:
            print("Soy una galleta sin chocolate")

una_galleta = Galleta(color = 'Marron',sabor='Salada')
una_galleta.sabor = "Salado"
una_galleta.color = "Marron"
print(una_galleta.chocolate)
print(una_galleta.chocolatear())
print(una_galleta.chocolate)
print("El sabor de esta galleta es salado: "+una_galleta.sabor)
una_galleta.tiene_chocolate()

una_galleta = Galleta()

