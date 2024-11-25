import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV
df = pd.read_csv("glass.csv")

# 2. Establecer un estilo bonito para las gráficas
sns.set(style="whitegrid")

# 3. Crear gráficos de tendencias para cada una de las características
features = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
for feature in features:
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Type', y=feature, data=df, marker='o', palette="viridis")
    plt.title(f'Tendencia de {feature} por Tipo de Vidrio', fontsize=18)
    plt.xlabel('Tipo de Vidrio', fontsize=18)
    plt.ylabel(feature, fontsize=18)
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejor visibilidad
    plt.show()
