import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset desde CSV
def cargar_dataset(ruta_csv):
    try:
        data = pd.read_csv(ruta_csv)
        return data
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")

# Preparar datos
def preparar_datos(data):
    # Convertir variables categóricas a numéricas
    le = LabelEncoder()
    data['WindGustDir'] = le.fit_transform(data['WindGustDir'])
    data['WindDir9am'] = le.fit_transform(data['WindDir9am'])
    data['WindDir3pm'] = le.fit_transform(data['WindDir3pm'])
    data['RainToday'] = le.fit_transform(data['RainToday'])
    data['RainTomorrow'] = le.fit_transform(data['RainTomorrow'])
    
    # Definir características (X) y objetivo (y)
    X = data.drop('RainTomorrow', axis=1)
    y = data['RainTomorrow']
    
    return X, y

# Entrenar modelo
def entrenar_modelo(X, y):
    # Dividir datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Crear modelo de Random Forest
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Entrenar modelo
    modelo.fit(X_train, y_train)
    
    # Realizar predicciones
    y_pred = modelo.predict(X_test)
    
    # Evaluar modelo
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    
    return modelo, accuracy, report, matrix

# Main
def main():
    ruta_csv = "/home/userlm/Documentos/WEATHER_MACHINE_LEARNING/weather.csv"
    data = cargar_dataset(ruta_csv)
    
    if data is not None:
        X, y = preparar_datos(data)
        modelo, accuracy, report, matrix = entrenar_modelo(X, y)
        
        print(f"Precisión del modelo: {accuracy:.3f}")
        print("Informe de clasificación:")
        print(report)
        
        # Imprimir matriz de confusión con seaborn
        plt.figure(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, cmap='Blues', fmt='d')
        plt.xlabel('Predicciones')
        plt.ylabel('Valores reales')
        plt.title('Matriz de confusión')
        plt.show()

if __name__ == "__main__":
    main()
