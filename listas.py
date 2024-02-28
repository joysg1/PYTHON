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
    
           
    