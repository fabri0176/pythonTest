#Recursión

def cuenta_atras(num):
    num -= 1
    if(num > 0):
        print(num)
        cuenta_atras(num)
    else:
        print("Booooom!")
    print("Fin de la función", num)

cuenta_atras(10)
print("# ---------------------------------")
def factorial(num):
    print("Valor Inicial = "+str(num))
    if(num > 1):
        num = num * factorial(num-1)
    print("Valor Final = " + str(num))
    return num
print(factorial(9))
print("# ---------------------------------")

