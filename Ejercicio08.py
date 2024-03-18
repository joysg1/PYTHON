inicio = int(input("Por favor ingrese el inicio: "))
fin = int(input("Por favor ingrese el final: "))

pares = []

print("\n")
print("*"*80)

for i in range (inicio, fin +1):
    if i%2 ==0:
        pares.append(i)
print(f"Lista de numeros pares: {pares}")  
pares.reverse()
print(f"Lista de numeros pares en reversa: {pares}")

      