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


# En numpy la dimension de los arreglos es inmutable

# En numpy la dimension de las listas es mutable

c = np.append(a,100)

print(c)

print(id(a))

print(id(c))

if(id(a) != id(c)):
    print("Son diferentes")

print(a is b)

b = np.delete(a,0)

print(b)
