import pandas as pd
import numpy as np


# Crea un arreglo int de 5 elementos
a = np.array([1, 2, 3, 4, 5])

# Imprime usando true los valores 0, 2 y 4
print(a[[True, False, True, False, True]])


print (a>10)

print(a<-1)

print(a>2)

b = np.random.randint(0, 100, 200)

print(b)

# Imprime los valores mayores a 50 y menores a 80
print(b[(b>50) & (b<80)])

