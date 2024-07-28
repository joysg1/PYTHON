def solicitar():
    lista = []
    num = None
    while num !=0:
        num = int(input("Ingrese un numero (0 para terminar): "))
    
        if num >0:
            lista.append(num)
        elif num ==0:
            break
        
    return lista


def ordenar(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i %2 ==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares


lista = solicitar()
print("Lista original: ")
print(lista)
pares, impares = ordenar(lista)
print("Lista de numeros pares: ")
print(pares)
print("Lista de numeros impares: ")
print(impares)