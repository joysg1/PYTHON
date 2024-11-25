import pandas as pd

# Cargar el archivo CSV original
df = pd.read_csv('vehicule.csv')  # Asegúrate de que la ruta sea correcta

# Generar 100,000 registros aleatorios a partir del dataset original
# Si el número de registros en el dataset original es menor que 100,000, replicamos aleatoriamente filas
n_samples = 100000
df_resampled = df.sample(n=n_samples, replace=True, random_state=42)

# Guardar el nuevo conjunto de datos generado aleatoriamente
df_resampled.to_csv('vehicules_100000.csv', index=False)

# Mostrar las primeras filas del nuevo dataset
print(df_resampled.head())
