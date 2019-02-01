#Herencia Multiple
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este metodo lo heredo de a")

class B:
    def __init__(self):
        print("Soy de clase B")

    def b(self):
        print("Este metodo lo heredo de b")

class C(A,B):
    pass

    def c(self):
        print("Este metodo es de c")

C = C()

