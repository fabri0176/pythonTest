#Caputar excepciones
while(True):

    try:
        n = float(input("Introduce un número: "))
        print(5/n)
        break
    except TypeError: # SI es error TypeError
        print("No se puede dividir el número por una cadena")
    except ValueError: # SI es error TypeError
        print("Debes introducir una cadena que sea número")
    except ZeroDivisionError:
        print("No se puede dividir por CERO, prueba otro número")
    except Exception as e: # SI es error generico
        print("Error: " + type(e) .__name__)