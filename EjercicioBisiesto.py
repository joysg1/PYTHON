def bisiesto(a):
    if a%4 !=0:
        mensaje = "No es bisiesto"
    elif a%4 ==0 and a%100 !=0:
        mensaje ="Si es bisiesto"
    elif a%4 ==0 and a %100 ==0 and a %400 !=0:
        mensaje = "No es bisiesto"
    elif a%4 ==0 and a %100 ==0 and a %400 ==0:
        mensaje ="Si es bisiesto"
    return mensaje

aU =0

while aU <=0:
 aU = int(input("Por favor ingrese un año: "))  

resultU = bisiesto(aU)

print(f"Año ingresado = {aU} -- {resultU}")

