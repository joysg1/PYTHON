# Realiza un programa que calcule la raiz cuadrada usando la libreria cmath
import cmath
def squareroot(num):
    result = cmath.sqrt(num)
    return result


num1 = float(input("Introduce un numero: "))

squareroot(num1)

a = round(squareroot(num1).real, 2)
print("La raiz cuadrada de " + str(num1) + " es " + str(a))



