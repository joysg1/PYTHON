import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('data_filtrada.csv')

# Verificar los tipos de datos de cada columna
print(df.dtypes)

# Comprobar si alguna columna tiene valores no numéricos
for column in df.columns:
    non_numeric_values = df[column][~df[column].apply(pd.to_numeric, errors='coerce').notnull()]
    if not non_numeric_values.empty:
        print(f"Columna '{column}' contiene valores no numéricos:")
        print(non_numeric_values)

# Si la columna 'Atributo_V' tiene valores no numéricos o NaN, imputamos con la media o mediana
df['Atributo_V'] = df['Atributo_V'].fillna(df['Atributo_V'].median())

# Asegurarse de que todas las columnas sean numéricas antes de continuar
X = df.drop('Atributo_V', axis=1)  # Variables independientes
X = X.apply(pd.to_numeric, errors='coerce')  # Convertir a numérico

# Seleccionar la variable objetivo (Atributo_V)
y = df['Atributo_V']

# Escalar las características (solo las columnas numéricas)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Entrenar el modelo con Random Forest
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Realizar predicciones
y_pred = rf_classifier.predict(X_test)

# Evaluar el rendimiento del modelo
print("Reporte de clasificación:")
report = classification_report(y_test, y_pred, output_dict=True)
print(report)

# Mostrar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=['Clase 0', 'Clase 1', 'Clase 2'], yticklabels=['Clase 0', 'Clase 1', 'Clase 2'])
plt.title('Matriz de Confusión')
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.tight_layout()
plt.show()

# Extraer las métricas de clasificación (considerando que las clases son 0.0, 1.0 y 2.0)
metrics = {
    'Precisión': [report['0.0']['precision'], report['1.0']['precision'], report['2.0']['precision']],
    'Recall': [report['0.0']['recall'], report['1.0']['recall'], report['2.0']['recall']],
    'F1-Score': [report['0.0']['f1-score'], report['1.0']['f1-score'], report['2.0']['f1-score']]
}

# Crear un DataFrame para las métricas
metrics_df = pd.DataFrame(metrics, index=['Clase 0', 'Clase 1', 'Clase 2'])

# Crear el gráfico de barras con colores pastel rojos
ax = metrics_df.plot(kind='bar', figsize=(10, 6), color=['#FFCCCC', '#FF6666', '#FF3333'], width=0.8)

# Añadir valores en cada barra
for p in ax.patches:
    ax.annotate(f'{p.get_height():.3f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', fontweight='bold', xytext=(0, 5),
                textcoords='offset points')

# Personalizar el gráfico
plt.title('Métricas de Clasificación por Clase', fontsize=16)
plt.ylabel('Valor', fontsize=14)
plt.xlabel('Clase', fontsize=14)
plt.xticks(rotation=0)
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Explicar la matriz de confusión
print("\nExplicación de la matriz de confusión:")
total_samples = cm.sum()
correct_predictions = cm.diagonal().sum()
accuracy = correct_predictions / total_samples

print(f"\nEl total de muestras es: {total_samples}")
print(f"El total de predicciones correctas es: {correct_predictions}")
print(f"Precisión del modelo: {accuracy:.4f}")

if accuracy > 0.85:
    print("\nEl modelo tiene una buena precisión.")
else:
    print("\nEl modelo tiene una precisión baja, podría requerir ajustes.")

