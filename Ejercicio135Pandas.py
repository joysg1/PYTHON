import pandas as pd
print("Version de pandas: ",pd.__version__)

import numpy as np


#Estructura de datos en pandas 

# 1. Series: elementos del mismo tipo de una dimension, cada elemento tiene una etiqueta

s = pd.Series([1, 2, 3, 4, 5])
print(s)

# 2. Dataframe: estructura de datos bidimensional, cada columna es una serie. 
# Puede contener diferentes tipos de datos, cada columna tiene una etiqueta

df = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Sofía'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
})

# 3. Carga y guardado de datos

# Cargar datos desde un archivo CSV
df2 = pd.read_csv('DataPersonasPandas.csv')
print(df2)

#4 Inspeccion y limpieza de datos


print(df2.head()) # Primeros 5 registros
print(df2.tail()) # Ultimos 5 registros
print(df2.shape) # Total de registros y columnas
print(df2.dtypes) # Tipo de datos de cada columna
print(df2.describe()) # Proporciona estadisticas descriptivas de las columnas numericas
print(df2.count()) #Cuenta el numero de valores no nulos en cada columna
print(df2.info()) # Informacion general sobre el dataframe
a = df2['Nombre'].unique() # Valores unicos de una columna
print(a)
df2.dropna() # Elimina filas con valores nulos
df2.drop_duplicates(inplace=True) # Elimina filas duplicadas
df2.fillna(value=0) # Rellena los valores nulos con 0
df2['Edad'] = df2['Edad'].astype('int') # Cambia el tipo de dato de una columna
# df2.rename(columns={'columna1': 'nuevo_nombre'}, inplace=True) # Cambia el nombre de una columna



# 5 Manipulacion de datos

# Seleccion y filtrado

print(df2['Nombre']) # Selecciona una columna
print("*"*80)
print(df2[df2['Edad'] > 30]) # Filtra por una condicion
print("*"*80)
print(df2[(df2['Edad'] > 30) & (df2['Ciudad'] == 'Madrid')]) # Filtra por multiples condiciones
print("*"*80)
print(df2.groupby('Ciudad').agg({'Edad': 'sum'})) # Agrupa por una columna y aplica una funcion
print("*"*80)
print(df2.sort_values('Edad', ascending=False)) # Ordena por una columna
print("*"*80)

# Determinar la moda de la edad
moda = df2['Edad'].mode()[0]
print("La moda de la edad es:", moda)
print("*"*80)
# Determinar la moda de la ciudad
moda_ciudad = df2['Ciudad'].mode()[0]
print("La moda de la ciudad es:", moda_ciudad)
print("*"*80)
# Determinar la media de la edad
media = df2['Edad'].mean()
print("La media de la edad es:", media)
print("*"*80)
# Determinar la mediana de la edad
mediana = df2['Edad'].median()
print("La mediana de la edad es:", mediana)
print("*"*80)
# Determinar la desviacion estandar de la edad
desviacion = df2['Edad'].std()
print("La desviacion estandar de la edad es:", desviacion)
print("*"*80)
# Determinar la varianza de la edad
varianza = df2['Edad'].var()
print("La varianza de la edad es:", varianza)
print("*"*80)
# Determinar el rango de la edad
rango = df2['Edad'].max() - df2['Edad'].min()
print("El rango de la edad es:", rango)
print("*"*80)

# Determinar la moda en nombre
moda_nombre = df2['Nombre'].mode()[0]
print("La moda de los nombres es:", moda_nombre)
print("*"*80)

# Determinar las personas en edad de 20 a 30 
print(df2[(df2['Edad'] >= 20) & (df2['Edad'] <= 30)])

print("*"*80)
# Agrupacion por ciudad y media de edad
print(df2.groupby('Ciudad')['Edad'].mean())

print("*"*80)
# Agrupacion por ciudad y edad minima
print(df2.groupby('Ciudad')['Edad'].min())
print("*"*80)


# Retorna el valor en la posicion de fila y columna indice
print(df2.at[4, 'Ciudad'])
fila_idx = 1
columna_idx = 2
print("*"*80)
print(df2.iat[fila_idx, columna_idx])
print("*"*80)

# Determinar las personas que no viven en Madrid
print(df2[~(df2['Ciudad'] == 'Madrid')])
print("*"*80)

# Determinar la moda de la edad de las personas que no viven en Madrid
print(df2[~(df2['Ciudad'] == 'Madrid')]['Edad'].mode()[0])
print("*"*80)


# 6. Fusion y union de datos

# Ejemplo de merge (fusion)
df3 = pd.DataFrame({'key':['A','B','C'], 'value': [1,2,3]})
df4 = pd.DataFrame({'key':['A','B','D'], 'value': [4,5,6]})
merge_df = pd.merge(df3, df4, on='key', how= 'inner') 
print(merge_df)

print("*"*80)

# Ejemplo de join (union)
df5 = pd.DataFrame({'value':[1, 2, 3]}, index=['A', 'B', 'C']) 
df6 = pd.DataFrame({'value':[4, 5, 6]}, index=['A', 'B', 'D'])
joined_df = df5.join(df6, lsuffix='_df1', rsuffix='_df2', how='outer')
joined_df2 = df5.join(df6, lsuffix='_df1', rsuffix='_df2', how='inner')
print(joined_df2)

print("*"*80)

# 7. Visualizacion de datos con pandas

import matplotlib.pyplot as plt

# Genera un grafico de la distribucion de personas por ciudad coloca el titulo en los ejes 
df2.groupby('Ciudad')['Edad'].count().plot(kind='bar', title='Distribucion de personas por ciudad')


plt.show()






 # https://codigofacilito.com/videos/clase-completa-pyhton-para-ciencias-de-datos-pandas




