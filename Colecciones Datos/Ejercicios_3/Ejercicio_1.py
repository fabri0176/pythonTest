lista_articulos = list()

print("-------------Bienvenido a la Lista de Compras-------------")
print("")
while True:
    print("Estas son las operaciones que puedes realizar: ")
    print("\t1 - Agregar Articulo")
    print("\t2 - Remover Articulo")
    print("\t3 - Ver los Articulo")
    print("\t4 - Salir")
    operacion = int(input(": "))

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else:
        break
    print("Gracias por usar nuestra lista de compras")
    print("Vuelve pronto")


def agregar_articulo():
    articulo = input("Nombre del articulo: ")
    lista_articulos.append(articulo)

def remover_articulo():
    print("Remover articulos")

def ver_articulos():
    for articulo in lista_articulos:
        print(articulo)