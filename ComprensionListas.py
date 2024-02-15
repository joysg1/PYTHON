#lista de los cuadrados de los numeros del 1 al 5

numeros = [1,2,3,4,5]
cuadrados = []

for numero in numeros:
    cuadrados.append(numero**2)
print(f"Lista original {numeros}\n")
print(f"Lista al cuadrado {cuadrados}\n")   


print("*"*40)
print("Usando comprension de listas \n")

#con comprension de listas

cuadrados = [numero **2 for numero in numeros]
print(f"Los cuadrados son : {cuadrados}")