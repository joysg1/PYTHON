import pandas as pd
from scipy.io import arff

# Cargar archivo ARFF
data, meta = arff.loadarff('vehicle.arff')

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Guardar el DataFrame como archivo CSV
df.to_csv('vehicule.csv', index=False)
