# Un conjunto en python es una coleccion desordenada de elementos unicos

# Creacion de un conjunto vacio
conjunto_vacio = set()

# Creacion de un conjunto con elementos

numeros = {1,2,3,4,5}
letras = set(['a','b','c'])

# Impresion de los conjuntos

print(f"Contenido del conjunto_vacio: {conjunto_vacio}")
print(f"Tipo de dato: {type(conjunto_vacio)}")
print(f"Contenido del conjunto numeros: {numeros}")
print(f"Tipo de dato {type(numeros)}")
print(f"Contenido del conjunto letras: {letras}")
print(f"Tipo de datos: {type(letras)}")

print("*"*80)
print("\n")


# Creacion de un conjunto nuevo para agregarle elementos

frutas = {'banana','pera','uva'}
print(f"Contenido del conjunto frutas: {frutas}")
frutas.add("coco")
frutas.add("manzana")
print(f"Contenido del conjunto frutas tras agregado de nuevos elementos {frutas}")
print("*"*80)
print("\n")


# Eliminar un elemento del conjunto frutas

# frutas.remove('coco')
# print(f"Contenido del conjunto frutas tras eliminar el elemento coco: {frutas}")

print(f"Elementos del conjunto frutas {frutas}")
eliminar = str(input('Por favor ingrese un elemento a eliminar: '))

if eliminar in frutas:
    frutas.remove(eliminar)
    print(f"Elemento {eliminar} quitado del conjunto frutas")
    print(f"Conjunto actualizado {frutas}")
elif eliminar not in frutas:
    print(f'Lo sentimos el elemento {eliminar} no esta en el conjunto frutas') 
    print(f"Elementos del conjunto frutas: {frutas}")   
    

print("*"*80)
print("\n")
   
agregar = str(input('Por favor ingrese un elemento para agregar: '))

frutas.add(agregar)

print(f"Contenido del conjunto frutas tras agregar elemento: {frutas}")


print("*"*80)
print("\n")

# Union de conjuntos, une los elementos de ambos conjuntos, usa el operador |

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
union = conjunto1 | conjunto2
print(f"Union de conjuntos, conjunto1: {conjunto1} y conjunto2: {conjunto2}")
print(f"Union: {union}")

print("*"*80)
print("\n")


# Interseccion de conjuntos, muestra el elemento comun entre ambos conjuntos, usa el operador &

interseccion = conjunto1 & conjunto2
print(f"Interseccion entre conjunto1: {conjunto1} y el conjunto2: {conjunto2}")
print(f"Interseccion: {interseccion}")

print("*"*80)
print("\n")


# Diferencia entre conjuntos, muestra los elementos que solo estan en un solo conjunto, usa el operador -

diferencia = conjunto1 - conjunto2
print(f"Diferencia entre el conjunto1: {conjunto1} y el conjunto2: {conjunto2}")
print(f"Diferencia: {diferencia}")

print("*"*80)
print("\n")

# Diferencia simetrica, muestra los elementos distintos entre ambos conjuntos, usa el operador ^

diferencia_simetrica = conjunto1 ^ conjunto2
print(f"Diferencia simetrica entre el conjunto1: {conjunto1} y el conjunto2: {conjunto2}")
print(f"Diferencia simetrica: {diferencia_simetrica}")  

print("*"*80)
print("\n")

# Comprobacion de pertenencia de un elemento a un conjunto

numerosP = {1,2,3,4,5,6,7,8,9,10}
print(f"Elementos del conjunto numerosP: {numerosP}")
p = int(input("Por favor ingrese un numero para comprobar la pertenencia: "))

if p in numerosP:
    print(f"El elemento {p} si esta en el conjunto")
elif p not in numerosP:
    print(f"El elemento {p} no esta en el conjunto") 
    
print("*"*80)
print("\n")

# Longitud de los conjuntos

longitud = len(numerosP)
print(f"La longitud del conjunto numerosP es: {longitud}")       

# Conversion lista a conjunto, con la finalidad de eliminar elementos repetidos

lista = [1,1,3,4,4,6,6,77,77,10]

conjuntol = set(lista)

lista_nueva = list(conjuntol)

print(f"Lista original: {lista}")
print(f"Lista original convertida a conjunto: {conjuntol}")
print(f"Lista sin elementos repetidos: {lista_nueva}")

print("*"*80)
print("\n")
               