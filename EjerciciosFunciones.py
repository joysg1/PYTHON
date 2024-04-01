# 1. Cree una funcion que salude al usuario, recibiendo el 
# nombre por parametro

'''

def saludo(nombre):
    mensaje = f"Hola {nombre}"
    return mensaje


nombreU = str(input("Por favor ingrese su nombre: "))


resultadoU = saludo(nombreU)

print(resultadoU)

'''



'''

# 2. Funcion que solicite al usuario su nombre y edad para mostrarlos


def nombreEdad(nombre, edad):
    mensaje = f"Hola {nombre} tu edad es {edad}"
    return mensaje


nombreU = str(input("Por favor ingrese su nombre: "))

edadU = 0
while edadU <=0:
 edadU = int(input("Por favor ingrese su edad: "))
 
 
resultadoU = nombreEdad(nombreU,edadU) 

print(resultadoU)

'''

'''

# 3. Funcion que reciba dos numeros y los reste

def resta(num1, num2):
    result = num1 - num2
    return result


print("--- RESTA DE DOS NUMEROS ---")
num1U = float(input("Por favor ingrese el primer numero: "))
num2U = float(input("Por favor ingrese el segundo numero: "))

resultU = resta(num1U, num2U)

print(f"{num1U:.2f} - {num2U:.2f} = {resultU:.2f}")


'''