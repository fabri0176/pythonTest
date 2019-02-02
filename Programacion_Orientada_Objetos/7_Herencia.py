class Producto:
    def __init__(self,referencia, nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t\t{}
NOMBRE\t\t\t{}
PVP\t\t\t\t{}
DESCRIPCIÓN\t\t{}
PRODUCTOR\t\t{}
DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion,self.productor,self.distribuidor)

class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t\t{}
NOMBRE\t\t\t{}
PVP\t\t\t\t{}
DESCRIPCIÓN\t\t{}
ISBN\t\t\t{}
AUTOR\t\t\t{}""".format(self.referencia, self.nombre, self.pvp,self.descripcion, self.isbn, self.autor)


ad = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")
print(ad)

a1 = Alimento(2034,"Botella Aceita Extra",5,"250 ML")
a1.productor = "La Aceitera"
a1.distribuidor = "Distribuiciones SA"
print(a1)


l1 = Libro(2036,"El carnal",6,"Libro el carnal")
l1.autor = "Juan Cobo"
l1.isbn = "44455259"
print(l1)



productos = [a1,ad]
productos.append(l1)

print(productos)

for producto in productos:
    print("-------------------------------")
    print("Producto:",type(producto))
    print(producto)

for producto in productos:

    print("-------------------------------")

    if(isinstance(producto,Adorno)):
        print(producto.referencia,producto.nombre)
    elif( isinstance(producto,Alimento) ):
        print(producto.referencia,producto.nombre,producto.productor)
    elif( isinstance(producto,Libro) ):
        print(producto.referencia, producto.nombre, producto.isbn)
print("-------------------------------")
print("-------------------------------")

def rebajar_producto(p,rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio"""

    p.pvp = p.pvp -(p.pvp/100 * rebaja)

    return p

al_rebajado = rebajar_producto(ad,60)
print(al_rebajado)
print("-------------------------------")
print("-------------------------------")
print(ad)

copia_ad = ad

l = [1,2,3]
l2 = l
#Los objetos se pasan por referencia
import  copy

copia_ad = copy.copy(ad)
print(copia_ad)

