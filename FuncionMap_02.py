#elevar al cuadrado los elementos de la lista utilizando la funcion map

numeros = [2,7,3,8,12,6,5]
cuadrados = list(map(lambda x: x**2,numeros))

print(f"Lista original {numeros}")
print(f"Cuadrados de la lista con map {cuadrados}")

print("-"*80)

# elevar al cuadrado los elementos de la lista sin map
cuadrados = []
for numero in numeros:
    cuadrados.append(numero**2)
print(f"Cuadrados de la lista sin map {cuadrados}")