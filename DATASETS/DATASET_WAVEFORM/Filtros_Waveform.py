import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset desde un archivo CSV 
df = pd.read_csv('data_filtrada.csv')  

# Verificar las primeras filas para asegurarnos de que los datos se cargaron correctamente
print("Primeras filas del dataset:")
print(df.head())

# Asegurarse de que 'Atributo_V' está presente en el dataset
if 'Atributo_V' in df.columns:
    print("\nEl atributo 'Atributo_V' está presente en el dataset.")
else:
    print("\nEl atributo 'Atributo_V' NO está presente en el dataset.")

# Estadísticas para el atributo de clasificación 'Atributo_V'
atributo_v = df['Atributo_V']

# Frecuencia de cada clase (0, 1, 2)
frecuencia = atributo_v.value_counts()

# Proporción de cada clase
proporciones = atributo_v.value_counts(normalize=True)

# Moda (valor más frecuente)
moda = atributo_v.mode()[0]



# Imprimir las estadísticas
print("\nFrecuencia de cada clase:")
print(frecuencia)
print("\nProporción de cada clase:")
print(proporciones)
print("\nModa del atributo:")
print(moda)


# Graficar las frecuencias de las clases
plt.figure(figsize=(8, 6))

# Crear un gráfico de barras para la frecuencia de cada clase
ax = sns.countplot(x=atributo_v, palette="Set2")

# Personalizar el gráfico
plt.title('Frecuencia de las clases para Atributo_V')
plt.xlabel('Valor del Atributo_V')
plt.ylabel('Frecuencia')
plt.xticks(ticks=[0, 1, 2], labels=['Clase 0', 'Clase 1', 'Clase 2'])

# Mostrar las cantidades en las barras
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', fontweight='bold')

plt.tight_layout()
plt.show()

# Graficar las proporciones de cada clase
plt.figure(figsize=(8, 6))

# Crear un gráfico de barras para las proporciones de cada clase
ax2 = proporciones.plot(kind='bar', color=sns.color_palette("Set2", len(proporciones)))

# Personalizar el gráfico
plt.title('Proporciones de las clases para Atributo_V')
plt.xlabel('Valor del Atributo_V')
plt.ylabel('Proporción')
plt.xticks(ticks=[0, 1, 2], labels=['Clase 0', 'Clase 1', 'Clase 2'])

# Mostrar las proporciones en las barras
for p in ax2.patches:
    ax2.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=12, color='black', fontweight='bold')

plt.tight_layout()
plt.show()



