# http://aprendeconalf.es/python/ejercicios/condicionales.html
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 €
# mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
# usuario tiene que tributar o no.

age = int(input("Enter your age:\t"))
if age >= 16:
    income = int(input("Enter your income:\t"))
    if(income > 1000):
        print("you are to pay")
    else:
        print("dont you are to pay")
else:
    print("No tiene edad para tributar")


