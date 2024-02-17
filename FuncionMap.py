#Funcion Map, muestra en este caso una lista con los elementos al cuadrado
lista = [2,5,8,6,2,1,9,0,4]
print("Lista original")
print(lista)
print("Lista con los cuadrados")
print(list(map((lambda valor: valor * valor ),lista)))

print("*"*40)
#Funcion Filter, muestra en este caso una lista de los elementos pares

print("Lista original")
print(lista)
print("Lista con los pares")
print(list(filter((lambda valor: valor%2==0),lista)))

print("*"*40)

#Funcion Reduce, muestra en esre caso la suma de todos los valores de la lista
print("Lista original")
print(lista)

import functools
print(str(functools.reduce((lambda x, resultado: x+ resultado),lista)))