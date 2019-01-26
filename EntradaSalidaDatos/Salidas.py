v = "otro texto"
n = 10
print("Un texto ", v ," y un número ",n)

s = "Un texto {} y un número {}".format(v,n)
print(s)

s = "Un texto {1} y un número {0}".format(v,n)
print(s)

s = "Un texto {texto} y un número {numero}".format(texto=v,numero=n)
print(s)

s = "{v},{v},{v},{v}".format(v=v)
print(s)

# Alinear a la derecha
print("{:>30}".format("palabra"))

# Alinear a la izquierda
print("{:30}".format("palabra"))

# Alinear al CENTRO
print("{:^30}".format("palabra"))

# Alinear al TRUNCAMIENTO
print("{:.3}".format("palabra"))

# Alineamiento a la derecha en 30 caracteres con truncamiento 3
print("{:>30.3}".format("palabra"))

# Formateo de números enteros, rellenados con espacios
print("{:05d}".format(10))
print("{:05d}".format(100))
print("{:05d}".format(1000))
print("{:05d}".format(10000))

#Formateo de números flotantes
print("{:.2f}".format(3.1415926))

print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.11))

# Alineado por puntos rellenado con 0
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.11))