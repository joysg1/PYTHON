from math import sqrt

def ecuacionSegundoGrado(a,b,c):
 a = int(input("Ingrese el valor de a: "))
 b = int(input("Ingrese el valor de b: "))
 c = int(input("Ingrese el valor de c: "))

 x1 =0
 x2 =0
 parcial = (b**2)-(4*a*c)
 if parcial < 0:
    print("No existen soluciones reales")
 if parcial >0:
    x1 = (-b+sqrt(parcial))/(2*a)
    x2 = (-b-sqrt(parcial))/(2*a)
    print("Las soluciones son: ")
    print("x1 = ", x1)
    print("x2 = ", x2)
    

ecuacionSegundoGrado(0,0,0)

