import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo 'gender_submission.csv'
gender_submission = pd.read_csv('gender_submission.csv')

# Mostrar las primeras filas para entender la estructura del archivo
print(gender_submission.head())

# Contar la cantidad de sobrevivientes (1) y no sobrevivientes (0)
survived_counts = gender_submission['Survived'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10,6))

# Graficar las barras con colores pasteles
bars = plt.bar(['No sobrevivió', 'Sobrevivió'], survived_counts, color=['#ffcccc', '#c1e7c1'])  # Rojo pastel y verde pastel

# Agregar etiquetas con la cantidad en cada barra
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), 
             ha='center', va='bottom', fontsize=12)

# Agregar etiquetas y título
plt.title('Distribución de Sobrevivientes vs No Sobrevivientes', fontsize=14)
plt.xlabel('Estado de Supervivencia', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)

# Mostrar la gráfica
plt.show()

