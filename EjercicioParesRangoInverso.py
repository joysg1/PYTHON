# 1. Cree un script que imprima los numeros pares segun el rango que indique el usuario
# imprima en orden inverso


def numParesR(i,f):
    nump = []
    
    for c in range(i,f+1):
        if c%2 ==0:
            nump.append(c)
    return list(reversed(nump)) 

inicioU = 0

while inicioU <=0:
 inicioU = int(input("Ingrese el inicio: "))


finalU =0

while finalU <=0 or finalU < inicioU:
 finalU = int(input("Ingrese el final: "))  


resultU = numParesR(inicioU, finalU)
print(f"Inicio = {inicioU} -- Final = {finalU} --- Numeros Pares en Reversa = {resultU}")