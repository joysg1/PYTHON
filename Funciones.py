def esPar(numero):
    if numero%2==0:
        # print(f"El {numero} es par \n")
        return True
    else:
        # print(f"El {numero} es impar \n")  
        return False
        

numero = int(input("Por favor ingrese el numero ha evaluar: \n")) 

resultado = esPar(numero)  
if resultado == True:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")    
  