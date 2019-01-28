# Argumentos Por valor y referencia

def doblarValores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
    return numeros

num = [1,2,3]
doblarValores(num)
print(num)

num = [1,2,3]
num2 = doblarValores(num[:])
print(num)
print(num2)



