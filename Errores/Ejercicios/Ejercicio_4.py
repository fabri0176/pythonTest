try:
    resultado = 15+"20"
except TypeError:
    print("Error: La suma debe realizar con valores tipo [enter|flotante], no se permite cadenas")
else:
    print("Suma Correcta")
finally:
    print("Ejecutando")