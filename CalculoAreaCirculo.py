import math


def areaCirculo(r):
    area = math.pi * r **2
    return area



radioUsuario = 0

while radioUsuario <=0:
 radioUsuario = float(input("Por favor ingrese el radio del circulo: "))


resultadoUsuario = (areaCirculo(radioUsuario))


print("\n")
print("*"*80)

print(f"El area del circulo es = {resultadoUsuario:.2f}")