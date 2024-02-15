# Calculadora_Basica_v_2.0

def menu():
    print("-------------------\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("0. Salir")
    print("-------------------\n")
    opcion = int(input("Por favor ingresa la opcion: "))
    
    return opcion 

def solDatos():
    num1 = int(input("Por favor ingrese el primer numero \n"))
    num2 = int(input("Por favor ingrese el segundo numero \n"))
    if num2 ==0:
        print("El segundo numero no puede ser 0 \n")
        num2 = int(input("Ingrese el segundo numero: \n"))
    return num1, num2

def operacion(operador, num1, num2):
    if operador == "suma":
        result = num1 + num2
    elif operador == "resta":
        result = num1 - num2
    elif operador == "multiplicacion":
        result = num1 * num2  
    elif operador == "division":
        result = num1 / num2  
    return result


while True:
    opcion = menu()
    if opcion ==1:
        num1, num2 = solDatos()
        print(f"{num1} + {num2} = ")
        print(operacion("suma",num1,num2))
    elif opcion ==2:
        num1, num2 = solDatos()
        print(f"{num1} - {num2} = ")
        print(operacion("resta",num1,num2))  
    elif opcion ==3:
        num1, num2 = solDatos()
        print(f"{num1} * {num2} = ")
        print(operacion("multiplicacion",num1,num2))  
    elif opcion ==4:
        num1, num2 = solDatos()
        print(f"{num1} / {num2} = ")
        print(operacion("division",num1,num2))  
    elif opcion ==0:
        break
    else:
        print("Opcion ivalida por favor verifique \n")
                  
                