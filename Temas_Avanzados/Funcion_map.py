class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

personas = map(lambda p: Persona(p.nombre, p.edad+1), personas)

for persona in personas:
    print(persona)

# Multiplicar listas
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

resultLista = list( map(lambda x,y : x*y, a,b) )

print(resultLista)

c = [11, 12, 13, 14, 15]

terslitas = list( map(lambda x,y,z : x*y*z, a,b,c) )

print(terslitas)