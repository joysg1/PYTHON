# 1. Guarde una contrasena en una variable 
# valide que la contrasena ingresada sea correcta

'''
passw = "secure"

while True:
    passU = str(input("Por favor ingrese su password: "))
    if passw == passU:
        print("Password correcto \n")
        break
    else:
        print("Password incorrecto \n")
        
'''       
        
# 2. Solicitar dos numeros al usuario para dividir, tener en cuenta
# que no se puede dividir por 0

'''

def dividir(num1, num2):
    result = num1 /num2
    return result

print("--- DIVISION DE DOS NUMEROS ---\n")
num1U = float(input("Ingrese el primer numero: "))

num2U = 0
while num2U ==0:
 num2U = float(input("Ingrese el segundo numero: "))
 print("Valide el divisor, la division entre 0 no es posible")


resultadoU = dividir(num1U, num2U)

print(f"{num1U} / {num2U} = {resultadoU:.2f}")

        
'''


# 3. Solicitar la edad del usuario e indicar si es mayor de edad o no

'''

def mayorEdad(e):
    if e >=18:
        mensaje = "Usted si es mayor de edad"
    else:
        mensaje = "Usted no es mayor de edad"
        
    return mensaje             



edad = 0

while edad <=0:
 edad = int(input("Por favor ingrese su edad: "))

resulU = mayorEdad(edad)

print(resulU)

'''


# 4. Pedir un numero al usuario e indicar si es par o no

'''

def esPar(n):
    if n %2 ==0:
        mensaje = "Si es par"
    elif n%2 !=0:
        mensaje = "No es par"
    return mensaje



numU =0

while numU <=0:
    
 numU = int(input("Por favor ingrese un numero: "))


resultU = esPar(numU)

print(resultU)        

'''