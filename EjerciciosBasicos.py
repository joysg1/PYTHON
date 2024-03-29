import statistics


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
    
        