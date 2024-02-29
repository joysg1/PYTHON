lista = [1,2.3,"arbol",[5,6,"voz"],7,"a",0,"casa"]

print(type(lista))

print(lista)

print(lista[2])

print(lista[3][1])

#mostrar los elementos en un intervalo (el ultimo digito no entra)

print(lista[0:2])

#muestra los elementos en un intervalo con un salto de dos 

print(lista[0:4:2])

#imprimir usando un for

print(f"Lista completa: {lista}")

print("\n")
print("*"*80)
contador = 0
for e in lista:
    contador = contador +1 
    print (f"Elemento #{contador} = {e}")
    
#agregar elementos a la lista



lista.append("nuevo_elemento")    
lista.append(23)

#agregamos una lista usando append, agrega una lista dentro de la lista
lista.append([1,67,"asd"])

#agregamos una lista usando extend (esto hace que los elementos de la lista se agregen de forma independiente)
lista.extend([1,2,3])

print(f"Lista actualizada tras agregar: {lista}")

#remover algun elemento de la lista, se debe indicar el elemento no la posicion
lista.remove(0)
print(f"Lista actualizada tras eliminar el 0: {lista}")

"""

#pedir al usuario que ingrese el valor a eliminar

print("\n")

opcion = 'Z'
while opcion != 'c' and opcion != 'C' or opcion !='N' and opcion !='n':
 opcion = str(input ("Desea eliminar una cadena o un numero [C/N]: "))
 if opcion == 'C' or opcion == 'c':
    eliminar = str(input("Por favor ingrese la cadena a eliminar: "))
    break
 elif opcion == 'N' or opcion =='n':
    eliminar = int(input("Por favor ingrese el numero a eliminar: "))
    break
 else:
     print("Opcion fuera de rango favor validar \n")
     

for e in lista:
    if eliminar == e:
        print(f"Elemento {eliminar} encontrado, se ha eliminado de la lista")
        lista.remove[eliminar]
print(f"Elemento {eliminar} no encontrado, por ende no ha sido eliminado")


contador2 = 0

print("\n")

print("Lista actualizada") 

for e in lista:
    contador2 = contador2 +1
    print(f"Elemento #{contador2} = {e}")
    
           
"""

print("\n")
print("*"*80)
#Mostrar el indice de un elemento en la lista

a = lista.index(2.3)

print(f"El elemento cuyo valor es 2.3 tiene como indice: {a}")

#Mostrar cuantas veces se repite un elemento en la lista

b = lista.count(1)

print("\n")
print("*"*80)

print(f"El elemento 1 se repite tantas veces en la lista: {b}")

#Mostrar la lista de forma reversa


print(f"Lista en orden original: {lista}")
lista.reverse()
print(f"Lista en orden reversa: {lista}")

#Mas ejemplos
print("\n")
print("*"*80)

listaCompra = ["pan","patatas","kiwis","fresas"]
print(f"Lista de elementos a comprar: {listaCompra}")
print(type(listaCompra))

#Crear una lista de variables
print("\n")
print("*"*80)
cantidadPan = 5
precioPan = 0.50
totalPago = cantidadPan * precioPan
pedido01 = [cantidadPan, precioPan, totalPago]
print(f"Lista pedido: {pedido01}")
print("\n")
print("*"*80)

#Crear lista dentro de listas
pedido02 = [4,0.4,4*0.4]
pedido03 = [5,0.8,5*0.8]
pedidos04 = [pedido01, pedido02, pedido03]
print(f"Lista total: {pedidos04}")
print("\n")
print("*"*80)

#Crear lista vacia

listaVacia = []
print(f"Lista vacia: {listaVacia}")
print(type(listaVacia))

print("\n")
print("*"*80)

#Agregar mas elementos a la listaCompra, con append se agrega al final
listaCompra.append("platanos")
print(f"Lista actualizada tras agregar el elemento platanos al final: {listaCompra}")

print("\n")
print("*"*80)

#Agregar mas elementos a la listaCompra, con insert se agregan en una posicion en concreto
listaCompra.insert(1,"peras")
print(f"Lista actualizada tras agregar el elemento pera en la posicion 1: {listaCompra}")

print("\n")
print("*"*80)

#Eliminar el ultimo elemento de la lista
listaCompra.pop()
print(f"Lista actualizada tras eliminar el ultimo elemento: {listaCompra}")

print("\n")
print("*"*80)

#Obtener la longitud de una lista
c = len(listaCompra)
print(f"Longitud de la listaCompra: {c}")

print("\n")
print("*"*80)

#Ejemplo anadir mediante un bucle for los cuadrados

cuadrados = []
numeros = [2,4,6,8]

for n in numeros:
    cuadrados.append(n*n)
print(f"Lista original de numeros: {numeros}")
print(f"Lista de los cuadrados {cuadrados}")

print("\n")
print("*"*80)

#Segundo ejemplo cuadrado de numeros mediante ciclo for (numeros del 1 al 10)

cuadrados2 = []

for numero in range(1,11):
    cuadrados2.append(numero*numero)
print(f"Lista de cuadrados de los numeros del 1 al 10: {cuadrados2}")

print("\n")
print("*"*80)

#Mostrar el minimo, maximo y suma de la lista cuadrados2

u1 = min(cuadrados2)
u2 = max(cuadrados2)
u3 = sum(cuadrados2)
print(f"Minimo de la lista cuadrados2: {u1}")
print(f"Maximo de la lista cuadrados2: {u2}")
print(f"Sumatoria de los elementos de cuadrados2: {u3}")

print("\n")
print("*"*80)

#Comprobar si un elemento esta o no en la lista compra

r1 = str(input("Por favor ingrese el elemento que desea buscar en listaCompra: "))

if r1 in listaCompra:
    print(f"El elemento {r1} esta en listaCompra")
if r1 not in listaCompra:
    print(f"El elemento {r1} no esta en listaCompra")       
        
print(f"Listado completo: {listaCompra}")

print("\n")
print("*"*80)
    