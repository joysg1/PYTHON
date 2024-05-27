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

serie4 = serie1 - serie2
print("\n")
print(serie4)

filas = ['tienda01','tienda02','tienda03','tienda04']
columnas =['articulo1','articulo2','articulo3']
datos = [[224,200,100],[100,120,101],[50,100,101],[120,101,106]]

dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)

# por fila
print(dataframe.loc['tienda02'])
print(dataframe.loc[['tienda01','tienda02']])

#por columna
print("\n")
print(dataframe['articulo3'])

#volor concreto
print("\n")
print(dataframe.loc['tienda01','articulo1'])

#nueva columna
dataframe['articulo4'] = [100,200,300,400]
print("\n")
print(dataframe)
print("\n")
dataframe['total']=dataframe['articulo1']+dataframe['articulo2']+dataframe['articulo3']+dataframe['articulo4']
print(dataframe)

# Video 97 min 21


