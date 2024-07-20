def mayor(num1, num2):
    if num1 < num2:
        return num2
    elif num1 > num2:
        return num1
    else:
        return False
    
    
elMayor = mayor(10,10)
if elMayor == False:
    print("Los numeros son iguales")
    
else:
    print(f"El numero mayor es: {elMayor}")        