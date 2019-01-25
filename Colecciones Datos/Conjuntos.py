#Conjuntos "Colecciones desordenadas"
conjunto = set()
print(conjunto)

conjunto = {1,2,3,4,5}
conjunto.add(9)
print(conjunto)

conjunto.add(0)
print(conjunto)

conjunto.add('h')
print(conjunto)

conjunto.add('a')
print(conjunto)

conjunto.add('z')
print(conjunto)

grupo = {'Hector','Juan','Mario'}
print('Hector' in grupo)
print('Maria' in grupo)
print('Hector' not in grupo)

test = {'Hector','Hector','Hector'}
print(test)

l = [1,2,1,2,2,3,4,5]
print(l)

c = set(l)
print(c)

l = list(c)
print(l)

s = "Al pan pan y al vino vino"
print(set(s))