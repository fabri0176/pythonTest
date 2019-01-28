# -------------------------------------
def saludar():
    return "Este print es desde saludar"

print(saludar())
# ------------------------------------
def dibujarTablaCinco(multiplicar):
    for i in range(11):
        print(" "+str(multiplicar)+" x "+str(i)+" = "+str(i*multiplicar))

dibujarTablaCinco(5)
# ------------------------------------
def test():
    n = 10
    return n
print(test())
# ------------------------------------
m = 2
def test2():
    return m

print(test2())