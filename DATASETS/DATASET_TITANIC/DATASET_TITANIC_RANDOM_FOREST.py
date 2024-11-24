import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Convertir la variable 'Sex' en una variable numérica
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})
test_data['Sex'] = test_data['Sex'].map({'male': 0, 'female': 1})

# Seleccionar las variables predictores y la variable objetivo
X = train_data[['Sex', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
y = train_data['Survived']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de clasificación
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Imprimir la matriz de confusión
print("Matriz de Confusión:")
print(cm)

# Explicación detallada de los resultados
TN, FP, FN, VP = cm.ravel()  # Extraer los valores de la matriz de confusión

# Imprimir explicación
print("\nExplicación de la Matriz de Confusión:")
print(f"Verdaderos Negativos (TN): {TN}")
print(f"Falsos Positivos (FP): {FP}")
print(f"Falsos Negativos (FN): {FN}")
print(f"Verdaderos Positivos (VP): {VP}")

# Explicación de cada componente
print("\nInterpretación:")
print("1. Verdaderos Negativos (TN): Son los casos en los que el modelo predijo correctamente que un pasajero no sobrevivió y realmente no sobrevivió.")
print("2. Verdaderos Positivos (VP): Son los casos en los que el modelo predijo correctamente que un pasajero sobrevivió y realmente sobrevivió.")
print("3. Falsos Positivos (FP): Son los casos en los que el modelo predijo que un pasajero sobrevivió, pero realmente no sobrevivió.")
print("4. Falsos Negativos (FN): Son los casos en los que el modelo predijo que un pasajero no sobrevivió, pero realmente sobrevivió.")

# Gráfico de la matriz de confusión
plt.figure(figsize=(12,8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Matriz de Confusión del Modelo', fontsize=22, weight='bold')  # Título más grande y en negrita
plt.xlabel('Clase Predicha', fontsize=18, weight='bold')  # Etiqueta de eje X en negrita y más grande
plt.ylabel('Clase Real', fontsize=18, weight='bold')  # Etiqueta de eje Y en negrita y más grande
plt.xticks([0, 1], ['No sobrevivió', 'Sobrevivió'], fontsize=16, weight='bold')  # Etiquetas en los ejes X en negrita
plt.yticks([0, 1], ['No sobrevivió', 'Sobrevivió'], rotation=0, fontsize=16, weight='bold')  # Etiquetas en los ejes Y en negrita
plt.show()

# Métricas de precisión
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Mostrar las métricas de precisión
print("\nMétricas de Precisión:")
print(f"Precisión del modelo: {accuracy:.2f}")
print(f"Precisión (Sobrevivientes): {report['1']['precision']:.2f}")
print(f"Recall (Sobrevivientes): {report['1']['recall']:.2f}")
print(f"F1-Score (Sobrevivientes): {report['1']['f1-score']:.2f}")

# Gráfico de métricas de precisión, recall y F1-Score
metrics = ['Precisión', 'Recall', 'F1-Score']
metrics_values = [report['1']['precision'], report['1']['recall'], report['1']['f1-score']]

plt.figure(figsize=(12,8))
sns.barplot(x=metrics, y=metrics_values, palette='Pastel1')
plt.title('Métricas de Precisión para la Clase Sobreviviente (1)', fontsize=22, weight='bold')  # Título más grande y en negrita
plt.xlabel('Métrica', fontsize=18, weight='bold')  # Etiqueta de eje X en negrita y más grande
plt.ylabel('Valor', fontsize=18, weight='bold')  # Etiqueta de eje Y en negrita y más grande
plt.ylim(0, 1)
plt.xticks(fontsize=16, weight='bold')  # Etiquetas de las barras en negrita
plt.yticks(fontsize=16, weight='bold')  # Etiquetas del eje Y en negrita
plt.show()

# Validación del modelo según las métricas
print("\nValidación del Modelo:")

# Umbrales para considerar un modelo como preciso
precision_threshold = 0.75
recall_threshold = 0.75
f1_threshold = 0.75

# Evaluar precisión, recall y F1-Score
if report['1']['precision'] >= precision_threshold and report['1']['recall'] >= recall_threshold and report['1']['f1-score'] >= f1_threshold:
    print("El modelo es preciso en función de las métricas.")
else:
    print("El modelo no es lo suficientemente preciso. Se recomienda mejorar el modelo.")







