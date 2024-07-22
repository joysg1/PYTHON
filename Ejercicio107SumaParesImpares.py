contador = 1
pares = 0
impares =0
SumaPares = 0
SumaImpares = 0

while contador <= 50:
    print(contador)
    if contador % 2 == 0:
        SumaPares  += contador
        pares += 1
    else:
        SumaImpares += contador
        impares += 1
    contador += 1
print(f"La suma de los pares es: {SumaPares}")
print(f"La cantidad de pares es: {pares}")
print(f"La suma de los impares es: {SumaImpares}")
print(f"La cantidad de impares es: {impares}")