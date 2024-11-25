import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Cargar el dataset
df = pd.read_csv("drug5000.csv")

# Preprocesamiento de datos
# Convertir columnas categóricas a numéricas
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['BP'] = df['BP'].map({'LOW': 0, 'NORMAL': 1, 'HIGH': 2})
df['Cholesterol'] = df['Cholesterol'].map({'NORMAL': 0, 'HIGH': 1})

# Separar las características y el objetivo
X = df.drop('Drug', axis=1)  # Características
y = df['Drug']  # Etiqueta

# Convertir la variable 'Drug' a numérica
y = le.fit_transform(y)

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo RandomForest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones
y_pred = clf.predict(X_test)

# Generar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Configurar el gráfico de la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Greens", cbar=False, annot_kws={"size": 15}, 
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Matriz de Confusión", fontsize=16)
plt.xlabel("Predicción", fontsize=12)
plt.ylabel("Realidad", fontsize=12)
plt.show()

# Generar el reporte de clasificación
report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)

# Convertir el reporte de clasificación a un DataFrame
report_df = pd.DataFrame(report).transpose()

# Mostrar las métricas del modelo
print(report_df)

# Crear un gráfico de barras agrupadas para cada droga con las métricas
metrics = ['precision', 'recall', 'f1-score']
fig, ax = plt.subplots(figsize=(12, 8))

# Convertir el DataFrame en una estructura adecuada para las métricas
metrics_values = report_df.loc[report_df.index != 'accuracy', metrics].values  # Ignorar la fila de accuracy

# Definir el ancho de cada barra y el desplazamiento
bar_width = 0.25
index = np.arange(len(report_df.index[1:]))  # Las clases (drogas)

# Crear las barras agrupadas para cada clase
ax.bar(index, metrics_values[:, 0], bar_width, label='Precision', color='lightgreen')
ax.bar(index + bar_width, metrics_values[:, 1], bar_width, label='Recall', color='lightblue')
ax.bar(index + 2 * bar_width, metrics_values[:, 2], bar_width, label='F1-Score', color='lightcoral')

# Etiquetas y título
ax.set_xlabel('Clase (Droga)', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Métricas del Modelo para Cada Droga (Barras Agrupadas)', fontsize=16)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(report_df.index[1:], rotation=45)

# Agregar leyenda
ax.legend(title='Métricas', loc='upper left')

plt.show()


