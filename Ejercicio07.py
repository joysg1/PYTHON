inicio = int(input("Por favor ingrese el inicio: "))
fin = int(input("Por favor ingrese el final: "))
print("*"*80)
print("\n")

impares = []

for i in range(inicio, fin +1 ):
    if i%2 !=0:
        impares.append(i)
print(f"Inicio indicado = {inicio} - Fin indicado = {fin}") 
print(f"Lista de numeros impares en el rango: {impares}")   
