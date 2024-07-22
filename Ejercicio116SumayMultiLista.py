def suma(lista):
    suma =0
    for i in lista:
        suma+=i
    return suma

def multiplica(lista):
    multi = 1
    for i in lista:
        multi*=i
    return multi


lista = [1,2,3,4,5,6,7,8,9,10]

print(suma(lista))
print(multiplica(lista))