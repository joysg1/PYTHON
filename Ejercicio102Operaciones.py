def menu():
    print("Selecciona la operacion (1,2,3,4)")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = int(input())
    return opcion

def dameResultado(seleccion):
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    if seleccion == 1:
        resultado = num1 + num2
    elif seleccion == 2:
        resultado = num1 - num2
    elif seleccion == 3:
        resultado = num1 * num2
    elif seleccion == 4:
        try:
         resultado = num1 / num2
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
            resultado = 0
    else:
        print("Opcion no valida")
        resultado = 0
    return resultado


continua = True
while continua:
    seleccion = menu()
    resultado = dameResultado(seleccion)
    print("El resultado es: ", resultado)
    print("Quieres hacer otra operacion? (s/n)")
    respuesta = input()
    if (respuesta =="s" or respuesta == "S"):
        continua = True
    else:
        continua = False
        print("Fin del calculo")
        
        
#video 106 min 18:15        
        