import pandas as pd

# Cargar el dataset en un DataFrame
df = pd.read_csv('vehicule.csv')

# Verificar si hay valores nulos en el DataFrame
nulos = df.isnull().sum()

# Mostrar las columnas que contienen valores nulos y cuántos valores nulos hay en cada una
print("Valores nulos por atributo:")
print(nulos)