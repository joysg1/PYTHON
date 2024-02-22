# importamos toda las funciones

# import Paquetes.funcion

# print(Paquetes.funcion.esPar(23))
# print(Paquetes.funcion.esPar(10))
# print("*"*10)
# print(Paquetes.funcion.suma(23,10))

# importamos las funciones de forma individual usando alias

from Paquetes.funcion import suma as s
from Paquetes.funcion import esPar as eP

print(s(2,4))
print("*"*10)
print(eP(34))
