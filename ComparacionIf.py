numero1 = int(input("Por favor ingrese el primer numero: "))
numero2 = int(input("Por favor ingrese el segundo numero: "))

if(numero1>numero2):
    print(f"El {numero1} es mayor que el {numero2}")
elif(numero1<numero2):
    print(f"El {numero2} es mayor que el {numero1}")
elif(numero1==numero2):
    print(f"El {numero1} es igual al {numero2}")  
    
    
print("Hemos terminado de comparar")

print("----------------------------------")      
    
#segundo ejemplo, edades para tarifa

edad = int(input("Por favor ingresa la edad: "))  

if edad<5:
    precio = 0  
elif edad<15:
    precio = 15
elif edad<65:
    precio = 20
else:
    precio = 15    

print(f"Edad ingresada: {edad} por tanto la tarifa es: {precio}") 
print("-------------------------------------")   
    