# INGRESAR NUMERO DEL 0 AL 9, SI EL NUMERO NO ESTA EN EL RANGO
# REPETIR HASTA QUE INGRESE EL NÚMERO VALIDO
# CUANDO EL NÚMERO SEA VALIDO, VALIDAR SI SE ENCUENTRA EN LA LISTA
# SI ES POSITIVO MOSTRAR MENSAJE QUE EL NÚMERO SE ENCUENTRA EN LA LISTA
numeros = [1,3,6,9]

while True:
    num = float(input("Ingrese un número: "))
    if(num < 0 or num > 9):
        print("Número no válido intente de nuevo")
        continue
    break

for numero in numeros:
    if(numero == num):
        print("El número "+str(int(num))+" se encuentra en la lista")

    
