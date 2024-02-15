numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

print("Metodo tradicional\n")

for numero in numeros:
    if numero%2 ==0:
        pares.append(numero)
print(f"Lista de numeros original {numeros}\n")
print(f"Lista de numeros pares {pares}\n")    

print("*"*40)


print("Usando comprension de listas \n")

pares = [numero for numero in numeros if numero%2==0]
print(f"Lista de numeros pares {pares}")