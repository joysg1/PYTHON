import statistics

import random


# 1. Leer un numero por teclado, comprobar que sea impar
# repetir el proceso hasta que sea par

'''

while True:
    numero = int(input("Por favor ingrese un numero: "))
    if numero %2!=0:
        print(f"El {numero} es impar")
    elif numero %2 ==0:
        print(f"El {numero} es par, fin del programa")
        break
    
'''    
 # 2. Realiza la media de los numeros que ingrese el usuario
 
''' 

listaNumeros = []

numUsuario = 0

cantidad = 0

media = 0

while cantidad <=0:
 cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
 
 
for i in range(0,cantidad):
    numUsuario = int(input(f"Ingrese el numero {i+1}: "))
    listaNumeros.append(numUsuario)
    
print("\n")
print("*"*80)
print(f"Listado de numeros = {listaNumeros}")
print("\n")
print("*"*80)
print(f"Media del listado = {statistics.mean(listaNumeros)}") 

''' 


# 3. Generar una lista con los numeros impares del 11 al 31


'''

listaImpar = []

for i in range(11,32):
    if i%2 !=0:
     listaImpar.append(i)

print(f"Listado de numeros impares [11-31]: {listaImpar}")    

'''


# 4. Genera una lista con los multiplos del 7 del 10 al 80

'''

listaI = []


for i in range(10,81):
    if i%7==0:
        listaI.append(i)
print(f"Multiplos del 7 [10-80]: {listaI}")        

'''


# 5. Sumar todos los numeros enteros pares del 50 al 100

'''

suma = 0
listaP = []


for i in range(50,101):
    if i%2 ==0:
        listaP.append(i)
        suma = suma + i
print(f"Listado de pares [50-100]: {listaP}") 
print("\n")
print("*"*80) 
print(f"Sumatoria = {suma}")      


'''


# 6. Genera una lista con numeros al azar e indicar cuantas veces aparece 
# un numero en la lista


listaR = []

cR = 0


while cR <=0:
 cR = int(input("Ingrese la cantidad de numeros al azar que desea: "))

print("\n")
print("*"*80)

for i in range(0,cR):
    listaR.append(random.randint(0,cR))
print(f"Listado de numeros aleatorios = {listaR}")

print("\n")
print("*"*80)
r = int(input("Ingrese el numero que desea verificar si se repite: "))
print(f"El numero = {r} se repite = {listaR.count(r)} veces")

