# TUPLAS
tupla = (100,"Hola",[1,2,3,4],-50)

print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])

len(tupla)
len(tupla[2])

for item in tupla:
    print(item)

print(tupla.index('Hola'))

tupla.count(100) # verificar si esta en la tupla

tupla.count('Algo') # Verificar si esta en la tupla

print("=============================================")
tupla_3 = (1,)
print(tupla_3)
print("=============================================")


try:
    tupla_3[1]
except IndexError:
    try:
        tupla_3[1] = 0
    except TypeError:
        print("Error")

print(tupla_3[1])