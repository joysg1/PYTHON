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
datos = [[np.nan,200,100],[np.nan,120,101],[np.nan,100,101],[np.nan,101,106]]

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

print(dataframe.drop('total', axis=1))
print(dataframe)
dataframe = dataframe.drop('total', axis=1)
print(dataframe)
condicion = dataframe > 200
print(dataframe[condicion])
condicion = dataframe != 'NaN'
print(dataframe[condicion])
condicion = (dataframe['articulo1'] > 200) | (dataframe['articulo2'] > 100)
print(dataframe[condicion])
nuevaColumna = '1 2 3 4'.split()
dataframe['indices']=nuevaColumna
print(dataframe)
dataframe = dataframe.set_index('indices')
print(dataframe)
dataframe.dropna(inplace=True)
print(dataframe)
dataframe = dataframe.reset_index()
print(dataframe)

datos = [[np.nan,200,100],[np.nan,120,101],[np.nan,100,101],[np.nan,101,106]]

dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)
dataframe.fillna(value=87, inplace=True)
print(dataframe)

#video 97 min 33.24


