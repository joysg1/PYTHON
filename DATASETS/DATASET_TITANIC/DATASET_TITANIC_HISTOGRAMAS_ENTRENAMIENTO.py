import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv') 
submission = pd.read_csv('gender_submission.csv')

# Visualización del conjunto de entrenamiento
print(train_data.head())

# Crear una gráfica para cada característica individualmente
for column in train_data.columns:
    plt.figure(figsize=(10,6))
    
    # Generar el histograma
    n, bins, patches = plt.hist(train_data[column].dropna(), bins=50, color='green', edgecolor='gray')
    
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
    plt.title(f'Distribución de {column}', fontsize=20)
    plt.xlabel(column, fontsize=20)
    plt.ylabel('Frecuencia', fontsize=20)
    
    # Mostrar cada gráfico
    plt.show()




