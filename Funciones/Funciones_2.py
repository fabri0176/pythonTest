def test():
    return "Una cadena retornada"

print(test())
# ------------------------------------
def calcularEdad(edad=0):
    if(edad<0):
        return False
# ------------------------------------
def retornarLista():
    return [1,2,3,4,5,6]
# ------------------------------------
print(retornarLista())
print(retornarLista()[2:])
# ------------------------------------
def testTuplaReturn():
    return "cadena",34,[3,5,5]

cadena,entero,lista = testTuplaReturn()
print(cadena)
print(entero)
print(lista)
