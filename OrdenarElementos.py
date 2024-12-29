
import random

# Crea un arreglo de 20 elementos
arreglo = [0] * 20

# Llena el arreglo con números aleatorios entre 1 y 100
for i in range(20):
    arreglo[i] = random.randint(1, 100)

# Imprime el arreglo original
print("Arreglo original:")
print(arreglo)

# Ordena el arreglo de menor a mayor
arreglo.sort()

# Imprime el arreglo ordenado
print("Arreglo ordenado:")
print(arreglo)


# Imprime el arreglo ordenado de mayor a menor
print("Arreglo ordenado de mayor a menor:")
print(arreglo[::-1])


