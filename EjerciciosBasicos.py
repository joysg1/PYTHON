# 1. Leer un numero por teclado, comprobar que sea impar
# repetir el proceso hasta que sea par


while True:
    numero = int(input("Por favor ingrese un numero: "))
    if numero %2!=0:
        print(f"El {numero} es impar")
    elif numero %2 ==0:
        print(f"El {numero} es par, fin del programa")
        break
        