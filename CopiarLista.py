lista_original = [1,2,3,4]
id_or = id(lista_original)


lista_copia = lista_original
id_cop = id(lista_copia)


print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n")
print(f"Lista copia: {lista_copia}")
print(f"Referencia lista copia: {id_cop}")
print(f"Tipo lista copia: {type(lista_copia)}")

print("*"*80)
print("\n")

print("Son los id de ambas listas iguales ?")
if id_or == id_cop:
    print("Si son iguales")
elif id_or != id_cop:
    print("No son iguales")  
    
print("*"*80)
print("\n") 

print("Agregamos en ambas listas valores y comprobamos la relacion") 

lista_original.append(5)
lista_copia.append(6) 

print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n")
print(f"Lista copia: {lista_copia}")
print(f"Referencia lista copia: {id_cop}")
print(f"Tipo lista copia: {type(lista_copia)}")

print("*"*80)
print("\n")

print("Son los id de ambas listas iguales ?")
if id_or == id_cop:
    print("Si son iguales")
elif id_or != id_cop:
    print("No son iguales")
      
    
print("*"*80)
print("\n") 


print("Ahora realizaremos el proceso con copy")

listacopy = lista_original.copy()
id_cop2 = id(listacopy)

print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n") 
print(f"Lista copia mediante la funcion copy: {listacopy}")
print(f"Referencia lista copy: {id_cop2}")
print(f"Tipo lista mediante la funcion copy: {type(listacopy)}")


print("Son los id de ambas listas iguales ?")
if id_or == id_cop2:
    print("Si son iguales")
elif id_or != id_cop2:
    print("No son iguales") 
    
comp = lista_original is lista_copia
print(f"Son la lista original y la lista copia iguales?: {comp}")     
    
print("*"*80)
print("\n") 


print("Prueba de modificacion entre la lista original y la lista generada con copy")
lista_original.append(7)
listacopy.append(8)

print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n") 
print(f"Lista copia mediante la funcion copy: {listacopy}")
print(f"Referencia lista copy: {id_cop2}")
print(f"Tipo lista mediante la funcion copy: {type(listacopy)}")


print("Son los id de ambas listas iguales ?")
if id_or == id_cop2:
    print("Si son iguales")
elif id_or != id_cop2:
    print("No son iguales")  
    
comp2 = lista_original is listacopy

print(f"Son la lista original y la lista generada con copy iguales: {comp2}") 
    
print("*"*80)
print("\n")


print("Prueba usando slicing [copiado total]")

lista_slice = lista_original[:]
id_ls = id(lista_slice)

print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n") 
print(f"Lista copia mediante la funcion slice: {lista_slice}")
print(f"Referencia lista copy: {id_ls}")
print(f"Tipo lista mediante la funcion slice: {type(lista_slice)}")


print("Son los id de ambas listas iguales ?")
if id_or == id_ls:
    print("Si son iguales")
elif id_or != id_ls:
    print("No son iguales") 
    
comp3 = lista_original is lista_copia
print(f"Son la lista original y la lista slice iguales?: {comp3}")     
    
print("*"*80)
print("\n") 


print("Prueba usando slicing [copiado parcial]")

lista_slice = lista_original[1:4]
id_ls = id(lista_slice)

print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n") 
print(f"Lista copia mediante la funcion slice: {lista_slice}")
print(f"Referencia lista copy: {id_ls}")
print(f"Tipo lista mediante la funcion slice: {type(lista_slice)}")


print("Son los id de ambas listas iguales ?")
if id_or == id_ls:
    print("Si son iguales")
elif id_or != id_ls:
    print("No son iguales") 
    
comp3 = lista_original is lista_copia
print(f"Son la lista original y la lista slice iguales?: {comp3}")     
    
print("*"*80)
print("\n") 



print("Prueba usando deep copy")

import copy

lista_deepC = copy.deepcopy(lista_original)
id_deC = id(lista_deepC)

print(f"Lista original: {lista_original}")
print(f"Referencia lista original: {id_or}")
print(f"Tipo lista original: {type(lista_original)}")
print("*"*80)
print("\n") 
print(f"Lista copia mediante la funcion deepCopy: {lista_deepC}")
print(f"Referencia lista deep copy: {id_deC}")
print(f"Tipo lista mediante la funcion deepCopy: {type(lista_deepC)}")


print("Son los id de ambas listas iguales ?")
if id_or == id_deC:
    print("Si son iguales")
elif id_or != id_deC:
    print("No son iguales") 
    
comp4 = lista_original is lista_deepC
print(f"Son la lista original y la lista deepCopy iguales?: {comp4}")     
    
print("*"*80)
print("\n") 


# Ejemplos varios

# Asignacion directa, los cambios se reflejan en ambas

listaOriginal = [0,1,2,3,4]
listaCopia = listaOriginal
listaCopia[0] = 100
print(f"Lista original: {listaOriginal}")
print(f"Lista copia: {listaCopia}")
print("*"*80)
print("\n") 

# Con la funcion copy, los cambios se reflejan en la lista donde se haga el cambio

listaCopia2 = listaOriginal.copy()
listaCopia2[1] = -1
print(f"Lista original: {listaOriginal}")
print(f"Lista alterada usando la funcion Copy: {listaCopia2}")

print("*"*80)
print("\n") 

# Con slice, los cambios se reflejan en la lista donde se haga el cambio

listaCopia3 = listaOriginal[:]
listaCopia3[2] = -5
print(f"Lista original: {listaOriginal}")
print(f"Lista alterada usando slice: {listaCopia3}")

print("*"*80)
print("\n") 

# Con el modulo Copy, los cambios se reflejan en la lista donde se haga el cambio
listaA = [[1,2],[3,4],[5,6]]
listaCopia4 = copy.deepcopy(listaA)
listaCopia4[0][1] = -8
print(f"Lista original: {listaA}")
print(f"Lista alterada usando el modulo Copy: {listaCopia4}")

print("*"*80)
print("\n") 





    
      