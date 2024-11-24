import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
# Reemplaza 'archivo.csv' con la ruta de tu archivo CSV
df = pd.read_csv('drug200.csv')

# Filtrar los datos de personas entre 20 y 30 años con presión y colesterol altos
df_filtered = df[(df['Age'] >= 20) & (df['Age'] <= 30) & (df['BP'] == 'HIGH') & (df['Cholesterol'] == 'HIGH')]

# Contar el número de hombres y mujeres que cumplen con estos criterios
count_gender = df_filtered['Sex'].value_counts()

# Función para mostrar tanto cantidad como porcentaje
def func(pct, allvalues):
    absolute = round(pct/100.*sum(allvalues))
    return f"{absolute} ({pct:.1f}%)"

# Colores pasteles
pastel_colors = ['#B3CDE0', '#FBB0B0']

# Generar el gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(count_gender, labels=count_gender.index, autopct=lambda pct: func(pct, count_gender), 
        startangle=90, colors=pastel_colors, wedgeprops={'edgecolor': 'black'})

# Títulos
plt.title('Distribución de Mujeres y Hombres entre 20 y 30 años con presión y colesterol altos')

# Mostrar el gráfico
plt.axis('equal')  # Para asegurar que el gráfico sea circular
plt.show()

