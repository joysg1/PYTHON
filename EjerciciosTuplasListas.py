# 1. Almacena en una lista diferentes asignaturas y muestralas

'''
asignaturas = ["matematicas","fisica","biologia","ingles"]
print(asignaturas)

'''


# 2. Almacena nombres en una lista, muestra un mensaje saludando a cada persona


'''

listaP = {"Luis","Maria","Pedro"}


for i in listaP:
    print(f"Hola {i}")
    
    
'''


# 3. Cree un diccionario en donde la clave este es espanol y el valor en ingles

'''

colores = {'rojo':'red','amarillo':'yellow','verde':'green','negro':'black'} 
opcion_u = str(input("Por favor ingrese un color: ")) 

if opcion_u not in colores:
    print(f"El color {opcion_u} no esta en memoria")
else:
    print(f"El color {opcion_u} esta en memoria su valor en ingles es: {colores[opcion_u]}")      
    
    
'''


# 4. En una tupla muestre decimales, cadenas y lista. Luego muestre la tupla


tupla = (0.24, "arbol",[2,34,5])

print(tupla)
print(type(tupla))
