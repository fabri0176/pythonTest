def suma(num1=0,num2=0):
    return num1+num2
resultado = suma(5,5)
print(resultado)


def resta(a,b):
    return a-b

resultado = resta(10,5)
print(resultado)


def resta2(a=None,b=None):
    if(a==None or b == None):
        return None

    return a-b

print(resta2())