import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
datos = [
    [3, 'Femenino', 18, 'Ingeniería'],
    [2, 'Masculino', 21, 'Economía'],
    [4, 'Femenino', 19, 'Derecho'],
    [1, 'Masculino', 20, 'Ingeniería'],
    [3, 'Femenino', 18, 'Economía'],
    [4, 'Masculino', 19, 'Derecho'],
    [5, 'Masculino', 18, 'Derecho'],
    [3, 'Masculino', 19, 'Ingeniería'],
    [3, 'Masculino', 20, 'Ingeniería'],
    [4, 'Femenino', 19, 'Economía'],
    [3, 'Femenino', 21, 'Derecho'],
    [2, 'Masculino', 18, 'Derecho'],
    [3, 'Femenino', 19, 'Economía'],
    [3, 'Femenino', 18, 'Economía'],
    [4, 'Masculino', 19, 'Derecho'],
    [5, 'Masculino', 18, 'Derecho'],
    [3, 'Femenino', 18, 'Ingeniería'],
    [2, 'Masculino', 21, 'Economía'],
    [4, 'Femenino', 19, 'Derecho'],
    [1, 'Masculino', 20, 'Ingeniería'],
    [4, 'Masculino', 19, 'Derecho'],
    [5, 'Masculino', 18, 'Derecho'],
    [3, 'Masculino', 19, 'Ingeniería'],
    [3, 'Masculino', 20, 'Ingeniería'],
    [4, 'Femenino', 19, 'Economía'],
    [3, 'Femenino', 21, 'Derecho'],
    [2, 'Masculino', 18, 'Derecho'],
    [3, 'Femenino', 19, 'Economía'],
    [3, 'Femenino', 19, 'Economía'],
    [3, 'Femenino', 18, 'Economía'],
    [4, 'Masculino', 19, 'Derecho'],
    [5, 'Masculino', 18, 'Derecho'],
    [3, 'Femenino', 18, 'Ingeniería'],
    [3, 'Femenino', 18, 'Ingeniería'],
    [2, 'Masculino', 21, 'Economía'],
    [4, 'Femenino', 19, 'Derecho'],
    [1, 'Masculino', 20, 'Ingeniería'],
    [3, 'Femenino', 18, 'Economía'],
    [4, 'Masculino', 19, 'Derecho'],
    [5, 'Masculino', 18, 'Derecho'],
    [3, 'Masculino', 19, 'Ingeniería'],
    [3, 'Masculino', 20, 'Ingeniería'],
    [4, 'Femenino', 19, 'Economía']
]

# Crear un DataFrame
df = pd.DataFrame(datos, columns=['Estrato', 'Género', 'Edad', 'Carrera'])

# Contar la frecuencia de cada carrera por género y estrato
carrera_genero_estrato = df.groupby(['Género', 'Estrato', 'Carrera']).size().reset_index(name='Frecuencia')

# Gráfico de barras
plt.figure(figsize=(12, 6))
colores = plt.cm.rainbow(np.linspace(0, 1, len(carrera_genero_estrato)))
for i, (genero, estrato) in enumerate(carrera_genero_estrato.groupby(['Género', 'Estrato']).groups.keys()):
    datos_genero_estrato = carrera_genero_estrato[(carrera_genero_estrato['Género'] == genero) & (carrera_genero_estrato['Estrato'] == estrato)]
    plt.bar(datos_genero_estrato['Carrera'], datos_genero_estrato['Frecuencia'], label=f'{genero} - Estrato {estrato}', color=colores[i])

plt.xlabel('Carrera')
plt.ylabel('Frecuencia')
plt.title('Distribución de carreras universitarias por género y estrato')
plt.legend()
plt.show()

# Tabla con la información de las leyendas
print("Tabla de frecuencias:")
for i, (genero, estrato) in enumerate(carrera_genero_estrato.groupby(['Género', 'Estrato']).groups.keys()):
    datos_genero_estrato = carrera_genero_estrato[(carrera_genero_estrato['Género'] == genero) & (carrera_genero_estrato['Estrato'] == estrato)]
    print(f"{genero} - Estrato {estrato}:")
    for j, carrera in enumerate(datos_genero_estrato['Carrera']):
        frecuencia = datos_genero_estrato['Frecuencia'].iloc[j]
        print(f"  {carrera}: {frecuencia} estudiantes")
    print()

