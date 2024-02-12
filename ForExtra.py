lista_colores = ["Amarillo", "Blanco","Rojo", "Negro","Azul"]
for color in lista_colores:
    print(color)

print("----------------------------------\n")    
    
mi_color=input("Ingrese un color para buscarlo en la lista: ")

lista_colores = ["Amarillo", "Blanco","Rojo", "Negro","Azul"]
for color in lista_colores:
    if color == mi_color:
         print(f'El color {mi_color} esta en la lista')
         break
else:
    print(f'El color {mi_color} no ha sido encontrado')
    
    
print("------------------------- \n")
print("Ejemplo for con lista larga \n")

rango_largo = range(1,100)
numero = int(input('Ingrese por favor el numero ha buscar: '))

for i in rango_largo:
    print(i)
    if i == numero:
        print(f"El {numero} ha sido encontado")
        break
else: 
    print(f'El recorrido ha sido terminado, el {numero} no ha sido encontrado  \n')            
    