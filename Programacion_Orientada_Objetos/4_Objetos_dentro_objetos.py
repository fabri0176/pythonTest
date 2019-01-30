class Pelicula:

    # Constructor
    def __init__(self,titulo = None,duracion = None, lanzamiento = None):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        if(titulo is not None):
            print("Se ha creado la película",self.titulo)

    # Redefinir el metodo string
    def __str__(self):
        return "{} ({})".format(self.titulo, self.lanzamiento)

class Catalogo:
    peliculas:[]

    def __init__(self,peliculas=[]):
        self.peliculas = peliculas

    def agregar(self,p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(str(p))

print('-----------------------------')
p1 = Pelicula(titulo="El padrino",lanzamiento=1992,duracion=120)
c = Catalogo([p1])
c.mostrar()
print('-----------------------------')
c.agregar(Pelicula(titulo="ET",lanzamiento=1993,duracion=190))
c.mostrar()
print('-----------------------------')
