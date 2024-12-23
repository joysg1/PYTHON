import numpy as np
import pandas as pd



b = np.empty(10)

print(b)

b[0] = 10

print(b)

b = np.empty(10, dtype = np.int64)

print(b)

b[0] = 10

print(b)

a = np.random.randint(0,100,20)

print(a)


print(np.nan)

print(a[0:10:2])

print(a[5:])

print(a[[0,2,3]])

# Quede en el minito -5:59

# https://codigofacilito.com/videos/arreglos-pt2-61b08130-ac2e-4eea-bb32-b23c3f79cafe