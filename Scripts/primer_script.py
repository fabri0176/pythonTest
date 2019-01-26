import sys
print("Hola, bienvenido a tu primer script")
print(sys.argv)

if(len(sys.argv) > 0): # valida si hay argumentos
    i = 1
    for argumento in sys.argv:
        print('#'+str(i) + " Argumento = "+ argumento)
        i += 1