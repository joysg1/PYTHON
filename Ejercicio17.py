"""


Pedir al usuario una lista de colores 
(separados por comas), guardarlos en una lista. 
No se deben guardar colores repetidos. 
Mostrar por consola la lista de colores ordenados alfabeticamente.


"""

# Se inicializan las variables 

colores = []
opcion = ""
color = ""
numColores = 0

# Se proceden a pedir los datos para llenar la lista colores

while opcion !="s" and opcion !="S" and opcion !="n" and opcion !="N":
 opcion = str(input("Desea agregar elementos a la lista colores (s/n): "))
 if opcion == "s" or opcion =="S":
     while numColores <=0:
      numColores = int(input("Ingrese el numero de colores a agregar: "))
     for i in range(1,numColores + 1):
      color = str(input(f"Ingrese el color #{i}: "))   
      if color in colores:
         print(f"El color = {color} ya esta en la lista")
      elif color not in colores:
         colores.append(color)    
 if opcion =="n" or opcion =="N":
     print("--- GRACIAS POR USAR EL PROGRAMA --- ")
     break

# Se ordena la lista colores

colores.sort()
print("\n")
print("*"*80)

# Se imprime la lista colores

print(f"Lista de colores: {colores} ")
print("\n")
print("*"*80)