import pickle
print("==================================================")
print("Crear fichero pickle")
lista = [1,2,3,4,5]

for i in range(100000):
    lista.append(i)

fichero_name = 'lista.pckl'
fichero = open(fichero_name,'wb')

pickle.dump(lista,fichero)
fichero.close()
print("==================================================")
print("Abrir fichero pickle")
fichero = open(fichero_name,'rb')
lista = pickle.load(fichero)
print(lista)
fichero.close()

print("==================================================")
print("Guardar Objetos")

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

nombres = ["Hector","Mario","Marta","Nestor","Fabricio","Hectore","Marios","Martas","Nestore","Fabricios"]

personas = []
for n in nombres:
    p = Persona(n)
    personas.append(p)

print(personas)

fichero = open('personas.pckl','wb')
pickle.dump(personas,fichero)
fichero.close()

fichero = open('personas.pckl','rb')
personas = pickle.load(fichero)

for p in personas:
    print(p)