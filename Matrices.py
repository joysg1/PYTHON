# Crea un arreglo de 20 elementos
import random
import numpy as np
import pandas as pd

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



# A partir del arreglo crea una matriz de 4x5

matriz = np.array(arreglo).reshape(5, 4)

print(matriz)

print(matriz.shape)

print(matriz.size)

# Obtener el ultimo elemento de la prima fila de la matriz
print(matriz[0, -1])

# Obtener el ultimo elemento de la ultima fila de la matriz
print(matriz[-1, -1])

# Obtener la suma de los elementos de la prima fila de la matriz
print(np.sum(matriz[0, :]))

# Obtener la cuenta de los elementos de la prima fila de la matriz
print(np.count_nonzero(matriz[0, :]))

# Obtener el elemento minimo de la primera fila de la matriz
print(np.min(matriz[0, :]))

# Obtener el elemento maximo de la primera fila de la matriz
print(np.max(matriz[0, :]))

# Obtener el promedio de la primera fila de la matriz
print(np.mean(matriz[0, :]))

# Obtener la desviacion estandar de la primera fila de la matriz
print(np.std(matriz[0, :]))

# Obtener la traspuesta de la matriz
print(matriz.T)

# Obtener el tamano de la traspuesta de la matriz
print(matriz.T.shape)

# Que en el minito - 5:18

