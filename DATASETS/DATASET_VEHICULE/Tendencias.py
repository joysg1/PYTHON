import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# Cargar el archivo CSV con 100,000 registros generados aleatoriamente
df = pd.read_csv('vehicules_100000.csv')  # Asegúrate de que la ruta sea correcta

# Separar las características (X) y la variable objetivo (y)
X = df.drop('Class', axis=1)
y = df['Class']

# Dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear el modelo de regresión logística
model = LogisticRegression(max_iter=5000, random_state=42, solver='lbfgs')

# Entrenar el modelo
model.fit(X_train_scaled, y_train)

# Realizar las predicciones en el conjunto de prueba
y_pred = model.predict(X_test_scaled)

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred, labels=y_test.unique())

# Crear un DataFrame de la matriz de confusión para facilitar la manipulación
cm_df = pd.DataFrame(cm, index=y_test.unique(), columns=y_test.unique())

# Crear un DataFrame para los aciertos y errores
accuracy_df = pd.DataFrame(index=cm_df.index)

# Usar numpy para obtener la diagonal (aciertos)
accuracy_df['Correct'] = np.diag(cm_df.values)
accuracy_df['Incorrect'] = cm_df.sum(axis=1) - np.diag(cm_df.values)

# Normalizar a proporciones (por cada clase)
accuracy_df['Correct Prop'] = accuracy_df['Correct'] / accuracy_df.sum(axis=1)
accuracy_df['Incorrect Prop'] = accuracy_df['Incorrect'] / accuracy_df.sum(axis=1)

# Crear un gráfico de barras apiladas
ax = accuracy_df[['Correct Prop', 'Incorrect Prop']].plot(kind='bar', stacked=True, figsize=(10, 7), color=['#7bc043', '#e74c3c'])

# Añadir los textos dentro de las barras
for p in ax.patches:
    # El valor de la barra
    height = p.get_height()
    width = p.get_width()
    x = p.get_x() + width / 2
    y = p.get_y() + height / 2
    
    # Calcular el porcentaje
    percentage = round(height * 100, 2)
    
    # Colocar el texto en el centro de la barra (en negrita y en color negro)
    ax.text(x, y, f'{percentage}%', ha='center', va='center', color='black', fontsize=10, fontweight='bold')

# Personalizar el gráfico
plt.title('Proporción de Aciertos y Errores por Clase de Vehículo', fontsize=16)
plt.xlabel('Clase de Vehículo', fontsize=12)
plt.ylabel('Proporción', fontsize=12)
plt.xticks(rotation=45)
plt.legend(['Aciertos', 'Errores'], loc='upper left')
plt.tight_layout()

# Mostrar el gráfico
plt.show()

