import math
# print(math.pi)

def area_circulo(radio):
    return math.pi * radio**2

radio = 65
area = area_circulo(65)

print("Area circulo con radio "+str(radio)+" es igual a "+str(area))