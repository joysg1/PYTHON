import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

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
cm = confusion_matrix(y_test, y_pred)

# Mostrar la matriz de confusión en formato gráfico
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=model.classes_, yticklabels=model.classes_)
plt.title('Matriz de Confusión (Regresión Logística)', fontsize=16)
plt.xlabel('Predicción', fontsize=12)
plt.ylabel('Realidad', fontsize=12)
plt.show()

# Calcular las métricas de desempeño
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Extraer las métricas relevantes para cada clase
# En este caso, las clases son los tipos de vehículos
class_names = model.classes_  # Usar las clases predichas por el modelo

# Imprimir las métricas para cada tipo de vehículo
print("Métricas del Modelo (Regresión Logística):")
for vehicle_class in class_names:
    precision = report[str(vehicle_class)]['precision']
    recall = report[str(vehicle_class)]['recall']
    f1_score = report[str(vehicle_class)]['f1-score']
    print(f"\nClase: {vehicle_class}")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  F1-Score: {f1_score:.4f}")

# Evaluación simple de si el modelo es competente
print("\nEvaluación del modelo:")
competente = True
for vehicle_class in class_names:
    precision = report[str(vehicle_class)]['precision']
    f1_score = report[str(vehicle_class)]['f1-score']
    if precision < 0.6 or f1_score < 0.6:
        competente = False
        print(f"El modelo no es competente para la clase {vehicle_class}.")
        break

if competente:
    print("El modelo es competente para todas las clases.")



