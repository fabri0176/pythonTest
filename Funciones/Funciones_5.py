#Funciones Argumentos y parametros indetermindos
def indeterminados_posicion(*args):

    for arg in args:
        print(arg)
indeterminados_posicion(5,9,6,[1,23,4],"hola")
# ----------------------------

print("# ---------------------------------")
def indeterminados_nombre(**kwargs):
    print(kwargs)



print(indeterminados_nombre(valor=5,nombre="Nestor"))
print("# ---------------------------------")
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

print(indeterminados_nombre(valor=5,nombre="Nestor"))

# ---------------------------------
print("# ---------------------------------")
def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatoria = "+str(t))

    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

super_funcion(10,50,-1,1.56,344,3434,3434,34,nombre="Hector",edad=27)