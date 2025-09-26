import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_dogs = pd.read_csv('/home/userlm/Documentos/DOGS_MACHINE_LEARNING/dogs_cleaned.csv')

# Mapea los tamaños de perro a valores numéricos
size_map = {"Small": 1, "Medium": 2, "Large": 3, "Very Large": 4}
df_dogs['Dog Size Num'] = df_dogs['Dog Size'].map(size_map)

# Crea el gráfico de dispersión
plt.figure(figsize=(10,6))
sns.scatterplot(x="Avg. Height, cm", y="Avg. Weight, kg", hue="Dog Size", data=df_dogs)

# Configura el gráfico
plt.title('Breed vs Dog Size')
plt.xlabel('Altura promedio (cm)')
plt.ylabel('Peso promedio (kg)')

# Muestra el gráfico
plt.show()
