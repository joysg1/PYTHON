import pandas as pd
import numpy as np

etiquetas = ['a','b','c','d','e']
datos = np.arange(4,9)
serie = pd.Series(datos,index=etiquetas)
print(serie)
print(serie['a'])
datos = ['Jose',5,'Maria',60]
print("\n")
serie = pd.Series(datos)
print(serie)
print("\n")
serie = pd.Series([100,200,40],index=['Emp01','Emp02','Emp03'])
print(serie)

serie1 = pd.Series([100, 200, 40], index=['Emp01', 'Emp02', 'Emp03'])
serie2 = pd.Series([101, 201, 41], index=['Emp01', 'Emp02', 'Emp03'])
serie3 = serie1 + serie2
print("\n")
print(serie3)

#Video 97 min 10:30