class Pelicula:
    def __init__(self,titulo = None,duracion = None, lanzamiento = None):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        if(titulo is not None):
            print("Se ha creado la película",self.titulo)

    # Desctructor de clase
    def __del__(self):
        print("Se está borrando la película")

    # Redefinir el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} mimnutos".format(self.titulo,self.lanzamiento,self.duracion)

    # Redefinir metodo len
    def __len__(self):
        return self.duracion

p = Pelicula(titulo="El Padrino",duracion=175,lanzamiento=1992)
print(str(p))
print(len(p))



