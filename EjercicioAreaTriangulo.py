# 1. Realice un script que calcule el area de un triangulo


def AreaTr(base, altura):
    r = (base * altura) /2
    return r



baseU = 0

while baseU <=0:
 baseU = float(input("Ingrese la base del triangulo: "))



alturaU = 0

while alturaU <=0:
   alturaU = float(input("Ingrese la altura del triangulo: "))


resultU = AreaTr(baseU, alturaU) 

print("\n")
print("*"*80)
print(f"Base = {baseU:.2f} - Altura = {alturaU:.2f} - Area = {resultU:.2f}")