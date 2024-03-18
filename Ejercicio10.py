def esprimo(num):
    
    for n in range(2, num):
        if num % n == 0:
            print(f"El {num} no es primo", n, "es divisor")
            return False
    print(f"El {num} es primo")
    return True
       
 
numero = 0
    
while numero <=0:      
 numero = int(input("Por favor ingrese un numero: "))


esprimo(numero)

 