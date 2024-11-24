import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv') 
submission = pd.read_csv('gender_submission.csv')

# Visualización del conjunto de prueba
print(test_data.head())

# Crear una gráfica para cada característica individualmente en el conjunto de prueba
for column in test_data.columns:
    plt.figure(figsize=(10,6))
    
    # Generar el histograma para los datos de prueba
    n, bins, patches = plt.hist(test_data[column].dropna(), bins=50, color='orange', edgecolor='gray')
    
    # Mostrar los valores de cada barra
    for i in range(len(patches)):
        height = n[i]
        if height > 0:  # Solo mostrar si la barra tiene algún valor
            plt.text(
                patches[i].get_x() + patches[i].get_width() / 2,  # Posición X del texto
                height,  # Posición Y del texto
                str(int(height)),  # El valor de la barra como texto
                ha='center',  # Alineación horizontal
                va='bottom',  # Alineación vertical
                fontsize=14
            )
    
    # Agregar etiquetas y título a cada gráfico
    plt.title(f'Distribución de {column} (Conjunto de Prueba)', fontsize=20)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Frecuencia', fontsize=14)
    
    # Mostrar cada gráfico
    plt.show()
