def dame_cuadrado(numero):
   miLista = []
   for i in range(numero):
       miLista.append(i**2)
   return miLista

print(dame_cuadrado(5))


def genera_cuadrados(numero):
    num = 1
    miLiista = []
    while num <numero:
        yield num**2
        num = num +1

for elemento in genera_cuadrados(5):
    print(elemento)
    
    
numeros =[2,3,4,6,23,67]
i = map(lambda x: x**2,numeros)
print(list(i))