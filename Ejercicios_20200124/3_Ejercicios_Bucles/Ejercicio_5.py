"""http://aprendeconalf.es/python/ejercicios/bucles.html"""
"""Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
amountInvested = float(input("Enter amount Invested:\t"))
interest = float(input("Enter Interest (0%-100%):\t"))
years = int(input("Enter number years:\t"))
capital = 0
if amountInvested > 0:
    for year in range(years+1):
        capital = amountInvested * (interest /  100)
        amountInvested += capital
        print("Capital first year {} is {}".format(year, round(amountInvested,2)))
else:
    print("Error no valid number")

