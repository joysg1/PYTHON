import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1. Cargar el archivo CSV
df = pd.read_csv("glass.csv")

# 2. Preprocesamiento de datos
# Asegúrate de que las columnas de tipo numérico estén en el formato correcto (convertir a float si es necesario)

# 3. Separar las características (X) y la etiqueta objetivo (y)
X = df.drop(columns=['Type'])  # Las características son todas menos 'Type'
y = df['Type']  # La etiqueta objetivo es 'Type'

# 4. Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Crear y entrenar el modelo de Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 6. Hacer predicciones
y_pred = rf.predict(X_test)

# 7. Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 8. Generar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Graficar la matriz de confusión con colores pastel dorados
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu", cbar=False, linewidths=0.5, linecolor='gray')
plt.title('Matriz de Confusión', fontsize=16)
plt.xlabel('Predicción', fontsize=12)
plt.ylabel('Real', fontsize=12)
plt.show()

# 9. Explicación detallada de la matriz de confusión
print("\nExplicación detallada de la matriz de confusión:")
print("La matriz de confusión muestra cómo el modelo ha clasificado cada tipo de vidrio. Las filas corresponden a las categorías reales (lo que debería ser),")
print("y las columnas corresponden a las predicciones del modelo (lo que el modelo ha clasificado).")
print("\nValores de la matriz:")
for i in range(cm.shape[0]):
    print(f"\nTipo de vidrio {i+1}:")
    print(f"- Verdaderos Positivos (TP): {cm[i, i]} (Estos son los casos que el modelo clasificó correctamente como tipo {i+1})")
    for j in range(cm.shape[1]):
        if i != j:
            print(f"- Falsos Positivos (FP) para tipo {i+1} cuando el modelo predice tipo {j+1}: {cm[j, i]}")
            print(f"- Falsos Negativos (FN) para tipo {i+1} cuando el modelo predice tipo {j+1}: {cm[i, j]}")

# 10. Gráfico de métricas: Precisión, Recall y F1-Score con colores pastel dorados
classification_rep = classification_report(y_test, y_pred, output_dict=True)

# Extrayendo las métricas
precision = classification_rep['macro avg']['precision']
recall = classification_rep['macro avg']['recall']
f1_score = classification_rep['macro avg']['f1-score']

# Graficar las métricas con tonos dorados pastel
metrics = ['Precisión', 'Recall', 'F1-Score']
scores = [precision, recall, f1_score]

plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette=sns.light_palette("gold", reverse=True))  # Usando tonos dorados
plt.title('Métricas de rendimiento del modelo', fontsize=16)
plt.ylabel('Valor', fontsize=12)
plt.show()

# 11. Explicación de las métricas
print("\nExplicación de las métricas:")
print(f"- Precisión: {precision:.2f}")
print(f"- Recall: {recall:.2f}")
print(f"- F1-Score: {f1_score:.2f}")

if precision > 0.8 and recall > 0.8 and f1_score > 0.8:
    print("\nEl modelo es preciso y tiene un buen desempeño general, ya que todas las métricas están por encima de 0.8.")
else:
    print("\nEl modelo no es totalmente preciso. Puede ser necesario ajustar el modelo o preprocesar mejor los datos.")

