# http://aprendeconalf.es/python/ejercicios/condicionales.html
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 200000€ y 35000€	20%
# Entre 350000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

annualRent = int(input("Enter your annual rent: "))


if 60000 < annualRent < 350000:
    print("Your anual rent is 30%")
elif 35000 < annualRent < 200000:
    print("Your anual rent is 20%")
elif 10000 < annualRent < 20000:
    print("Your anual rent is 15%")
elif annualRent > 60000:
    print("Your anual rent is 45%")
elif annualRent < 10000:
    print("Your anual rent is 5%")