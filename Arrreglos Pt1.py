import pandas as pd

import numpy as np


a = np.array ([1,2,3,4,5])

print(a)

a = np.array ([1,2,3,4,5],dtype = np.int64)

print(a)

a = np.array ([1,2,3,4,5,'6'],dtype = np.str_)

print(a)

a = np.array ([1,2,3,4,5,'6'],dtype = np.float64)

print(a)

a = np.array ([1,2,3,4,5,'6'],dtype = np.bool)

print(a)

a = np.array ([1,2,3,4,5,'6',0],dtype = np.bool)

print(a)

a = np.array ([1,2,3,4,5],dtype = np.uint64) # uint enteros sin signo

print(a)

a = np.array (([1,2,3,4,5,6]),dtype = np.complex128) # complex permite trabajar con numeros muy grandes

print(a)

a = np.ones(10) # crea un arreglo de 10 elementos con 1

print(a)

a = np.zeros(10) # crea un arreglo de 10 elementos con 0

print(a)

a = np.arange(0,10) # crea un arreglo del 0 al 9

print(a)

a = np.random.randint(0,255,10) # crea un arreglo de 10 elementos con  numeros aleatorios entre 0 y 255

print(a)

a.size

print(a.size)

print(a.shape) #imprime la forma del arreglo

print(a.ndim) #imprime la dimension del arreglo

b= np.array ([[1,2,3], [4,5,6]])

print(b)

print(b.ndim)

print(b.shape)







