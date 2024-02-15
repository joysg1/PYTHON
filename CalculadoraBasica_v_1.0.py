#Calculadora basica version 1.0


opcion = 1

def suma (num1, num2):
    result = num1 + num2
    return result

def resta (num1, num2):
    result = num1 - num2
    return result

def multi (num1, num2):
    result = num1 * num2
    return result

def divi (num1, num2):
    result = num1 / num2
    return result

def menu():
    print("----------------------\n")
    print("1. Suma \n")
    print("2. Resta \n")
    print("3. Multiplicacion \n")
    print("4. Division \n")
    print("0. Salir \n")
    print("---------------------\n")
    

while opcion != 0:
    menu()
    opcion = int(input("Ingrese la operacion deseada: \n"))
    if opcion == 0:
        print("Gracias por utilizar el programa \n")
        break
        
    num1 = int(input("Por favor ingrese el primer numero \n"))
    num2 = int(input("Por favor ingrese el segundo numero \n"))
    
    if opcion == 1:
        resultado = suma(num1, num2)
        print(f"{num1} + {num2} = {resultado}\n")
    elif opcion == 2:
        resultado = resta(num1, num2)
        print(f"{num1} - {num2} = {resultado}\n")
    elif opcion ==3:
        resultado = multi(num1, num2)
        print(f"{num1} * {num2} = {resultado}\n")  
    elif opcion ==4:
        resultado = divi(num1, num2)
        print(f"{num1} / {num2} = {resultado} \n")
    else:
        print("Por favor verifique la opcion ingresada \n")    
    
            
                  
    
    
