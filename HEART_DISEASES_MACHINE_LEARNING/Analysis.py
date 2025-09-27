import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.svm import SVR, SVC
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import warnings
warnings.filterwarnings('ignore')

class PredictiveAnalysis:
    def __init__(self, file_path, target_column, predictor_column=None):
        """
        Inicializa el análisis predictivo
        
        Args:
            file_path (str): Ruta del archivo CSV
            target_column (str): Nombre de la columna objetivo
            predictor_column (str): Nombre de la columna predictora (opcional)
        """
        self.file_path = file_path
        self.target_column = target_column
        self.predictor_column = predictor_column
        self.df = None
        self.X = None
        self.y = None
        self.is_classification = False
        self.scaler = StandardScaler()
        self.results = {}
        
    def load_data(self):
        """Carga los datos desde el archivo CSV"""
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"Datos cargados exitosamente: {self.df.shape}")
            print("\nPrimeras 5 filas:")
            print(self.df.head())
            print("\nInformación del dataset:")
            print(self.df.info())
            return True
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return False
    
    def prepare_data(self):
        """Prepara los datos para el análisis"""
        if self.df is None:
            print("Primero debe cargar los datos")
            return False
            
        # Si no se especifica columna predictora, usar todas excepto la objetivo
        if self.predictor_column is None:
            self.X = self.df.drop(columns=[self.target_column])
        else:
            self.X = self.df[[self.predictor_column]]
            
        self.y = self.df[self.target_column]
        
        # Manejar valores faltantes
        self.X = self.X.fillna(self.X.mean() if self.X.select_dtypes(include=[np.number]).shape[1] > 0 else self.X.mode().iloc[0])
        self.y = self.y.fillna(self.y.mean() if pd.api.types.is_numeric_dtype(self.y) else self.y.mode()[0])
        
        # Codificar variables categóricas
        for col in self.X.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            self.X[col] = le.fit_transform(self.X[col].astype(str))
            
        # Determinar si es clasificación o regresión
        if pd.api.types.is_numeric_dtype(self.y) and len(self.y.unique()) > 10:
            self.is_classification = False
            print("Detectado como problema de REGRESIÓN")
        else:
            self.is_classification = True
            if not pd.api.types.is_numeric_dtype(self.y):
                le_target = LabelEncoder()
                self.y = le_target.fit_transform(self.y)
            print("Detectado como problema de CLASIFICACIÓN")
            
        print(f"Variables predictoras: {list(self.X.columns)}")
        print(f"Variable objetivo: {self.target_column}")
        print(f"Forma de X: {self.X.shape}, Forma de y: {self.y.shape}")
        
        return True
    
    def get_algorithms(self):
        """Retorna los algoritmos según el tipo de problema"""
        if self.is_classification:
            return {
                'Logistic Regression': LogisticRegression(random_state=42),
                'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
                'SVM': SVC(random_state=42),
                'KNN': KNeighborsClassifier(),
                'Decision Tree': DecisionTreeClassifier(random_state=42),
                'Gradient Boosting': GradientBoostingClassifier(random_state=42),
                'Naive Bayes': GaussianNB()
            }
        else:
            return {
                'Linear Regression': LinearRegression(),
                'Ridge Regression': Ridge(random_state=42),
                'Lasso Regression': Lasso(random_state=42),
                'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
                'SVM': SVR(),
                'KNN': KNeighborsRegressor(),
                'Decision Tree': DecisionTreeRegressor(random_state=42),
                'Gradient Boosting': GradientBoostingRegressor(random_state=42)
            }
    
    def evaluate_algorithms(self, test_size=0.2):
        """Evalúa múltiples algoritmos y compara su rendimiento"""
        # Dividir los datos
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=42
        )
        
        # Escalar los datos
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        algorithms = self.get_algorithms()
        results = []
        
        print("\nEvaluando algoritmos...")
        print("="*60)
        
        for name, algorithm in algorithms.items():
            try:
                # Entrenar el modelo
                if name in ['SVM', 'KNN', 'Logistic Regression']:
                    algorithm.fit(X_train_scaled, y_train)
                    y_pred = algorithm.predict(X_test_scaled)
                    # Cross-validation con datos escalados
                    cv_scores = cross_val_score(algorithm, X_train_scaled, y_train, cv=5)
                else:
                    algorithm.fit(X_train, y_train)
                    y_pred = algorithm.predict(X_test)
                    # Cross-validation con datos originales
                    cv_scores = cross_val_score(algorithm, X_train, y_train, cv=5)
                
                if self.is_classification:
                    accuracy = accuracy_score(y_test, y_pred)
                    cv_mean = cv_scores.mean()
                    cv_std = cv_scores.std()
                    
                    results.append({
                        'Algoritmo': name,
                        'Accuracy': accuracy,
                        'CV Mean': cv_mean,
                        'CV Std': cv_std
                    })
                    
                    print(f"{name:20} | Accuracy: {accuracy:.4f} | CV: {cv_mean:.4f} ± {cv_std:.4f}")
                    
                else:
                    mse = mean_squared_error(y_test, y_pred)
                    rmse = np.sqrt(mse)
                    mae = mean_absolute_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)
                    cv_mean = cv_scores.mean()
                    cv_std = cv_scores.std()
                    
                    results.append({
                        'Algoritmo': name,
                        'RMSE': rmse,
                        'MAE': mae,
                        'R²': r2,
                        'CV Mean': cv_mean,
                        'CV Std': cv_std
                    })
                    
                    print(f"{name:20} | R²: {r2:.4f} | RMSE: {rmse:.4f} | CV: {cv_mean:.4f} ± {cv_std:.4f}")
                
                # Guardar el modelo entrenado
                self.results[name] = {
                    'model': algorithm,
                    'predictions': y_pred,
                    'y_test': y_test
                }
                    
            except Exception as e:
                print(f"Error con {name}: {e}")
                continue
        
        self.results_df = pd.DataFrame(results)
        return self.results_df
    
    def plot_results(self):
        """Visualiza los resultados de la comparación"""
        if not hasattr(self, 'results_df'):
            print("Primero debe ejecutar evaluate_algorithms()")
            return
            
        plt.figure(figsize=(15, 10))
        
        if self.is_classification:
            # Gráfico de accuracy
            plt.subplot(2, 2, 1)
            bars = plt.bar(self.results_df['Algoritmo'], self.results_df['Accuracy'])
            plt.title('Comparación de Accuracy por Algoritmo')
            plt.xticks(rotation=45)
            plt.ylabel('Accuracy')
            
            # Añadir valores en las barras
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.3f}', ha='center', va='bottom')
            
            # Gráfico de CV scores
            plt.subplot(2, 2, 2)
            plt.errorbar(range(len(self.results_df)), self.results_df['CV Mean'], 
                        yerr=self.results_df['CV Std'], fmt='o-', capsize=5)
            plt.title('Cross-Validation Scores')
            plt.xticks(range(len(self.results_df)), self.results_df['Algoritmo'], rotation=45)
            plt.ylabel('CV Score')
            
        else:
            # Gráfico de R²
            plt.subplot(2, 2, 1)
            bars = plt.bar(self.results_df['Algoritmo'], self.results_df['R²'])
            plt.title('Comparación de R² por Algoritmo')
            plt.xticks(rotation=45)
            plt.ylabel('R² Score')
            
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.3f}', ha='center', va='bottom')
            
            # Gráfico de RMSE
            plt.subplot(2, 2, 2)
            bars = plt.bar(self.results_df['Algoritmo'], self.results_df['RMSE'])
            plt.title('Comparación de RMSE por Algoritmo')
            plt.xticks(rotation=45)
            plt.ylabel('RMSE')
            
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.3f}', ha='center', va='bottom')
        
        # Matriz de correlación de las variables predictoras
        plt.subplot(2, 2, 3)
        correlation_matrix = self.X.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Matriz de Correlación de Variables Predictoras')
        
        # Distribución de la variable objetivo
        plt.subplot(2, 2, 4)
        if self.is_classification:
            self.y.value_counts().plot(kind='bar')
            plt.title('Distribución de la Variable Objetivo')
            plt.xticks(rotation=0)
        else:
            plt.hist(self.y, bins=30, alpha=0.7)
            plt.title('Distribución de la Variable Objetivo')
            plt.xlabel(self.target_column)
            plt.ylabel('Frecuencia')
        
        plt.tight_layout()
        plt.show()
    
    def get_best_algorithm(self):
        """Retorna el mejor algoritmo según la métrica principal"""
        if not hasattr(self, 'results_df'):
            print("Primero debe ejecutar evaluate_algorithms()")
            return None
            
        if self.is_classification:
            best_idx = self.results_df['Accuracy'].idxmax()
            metric = 'Accuracy'
        else:
            best_idx = self.results_df['R²'].idxmax()
            metric = 'R²'
            
        best_algorithm = self.results_df.iloc[best_idx]
        
        print(f"\n🏆 MEJOR ALGORITMO: {best_algorithm['Algoritmo']}")
        print(f"   {metric}: {best_algorithm[metric]:.4f}")
        
        return best_algorithm
    
    def detailed_analysis(self, algorithm_name):
        """Análisis detallado de un algoritmo específico"""
        if algorithm_name not in self.results:
            print(f"Algoritmo '{algorithm_name}' no encontrado")
            return
            
        model_info = self.results[algorithm_name]
        y_pred = model_info['predictions']
        y_test = model_info['y_test']
        
        print(f"\n📊 ANÁLISIS DETALLADO: {algorithm_name}")
        print("="*50)
        
        if self.is_classification:
            accuracy = accuracy_score(y_test, y_pred)
            print(f"Accuracy: {accuracy:.4f}")
            print("\nReporte de Clasificación:")
            print(classification_report(y_test, y_pred))
            
            # Matriz de confusión
            plt.figure(figsize=(8, 6))
            cm = confusion_matrix(y_test, y_pred)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title(f'Matriz de Confusión - {algorithm_name}')
            plt.ylabel('Valor Real')
            plt.xlabel('Predicción')
            plt.show()
            
        else:
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print(f"R² Score: {r2:.4f}")
            print(f"RMSE: {rmse:.4f}")
            print(f"MAE: {mae:.4f}")
            print(f"MSE: {mse:.4f}")
            
            # Gráfico de predicciones vs valores reales
            plt.figure(figsize=(10, 6))
            
            plt.subplot(1, 2, 1)
            plt.scatter(y_test, y_pred, alpha=0.7)
            plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
            plt.xlabel('Valores Reales')
            plt.ylabel('Predicciones')
            plt.title(f'Predicciones vs Valores Reales\n{algorithm_name}')
            
            plt.subplot(1, 2, 2)
            residuals = y_test - y_pred
            plt.scatter(y_pred, residuals, alpha=0.7)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.xlabel('Predicciones')
            plt.ylabel('Residuos')
            plt.title(f'Gráfico de Residuos\n{algorithm_name}')
            
            plt.tight_layout()
            plt.show()

# Función principal de uso
def run_predictive_analysis(file_path, target_column, predictor_column=None):
    """
    Ejecuta el análisis predictivo completo
    
    Args:
        file_path (str): Ruta del archivo CSV
        target_column (str): Nombre de la columna objetivo
        predictor_column (str): Nombre de la columna predictora (opcional)
    
    Returns:
        PredictiveAnalysis: Objeto con todos los resultados
    """
    # Crear instancia del análisis
    analysis = PredictiveAnalysis(file_path, target_column, predictor_column)
    
    # Cargar y preparar datos
    if not analysis.load_data():
        return None
        
    if not analysis.prepare_data():
        return None
    
    # Evaluar algoritmos
    results_df = analysis.evaluate_algorithms()
    
    # Mostrar resultados
    print("\n📈 RESUMEN DE RESULTADOS:")
    print("="*60)
    print(results_df.to_string(index=False))
    
    # Identificar mejor algoritmo
    best = analysis.get_best_algorithm()
    
    # Visualizar resultados
    analysis.plot_results()
    
    # Análisis detallado del mejor algoritmo
    if best is not None:
        analysis.detailed_analysis(best['Algoritmo'])
    
    return analysis

# EJEMPLO DE USO:
if __name__ == "__main__":
    # Reemplaza estos valores con tu información
    FILE_PATH = "/home/userlm/Documentos/HEART_MACHINE_LEARNING/heart.csv"  # Ruta de tu archivo CSV
    TARGET_COLUMN = "chol"      # Nombre de tu columna objetivo
    PREDICTOR_COLUMN = None       # None para usar todas las columnas, o especifica una columna
    
    # Ejecutar análisis
    analysis = run_predictive_analysis(FILE_PATH, TARGET_COLUMN, PREDICTOR_COLUMN)
    
    # Para análisis adicional de un algoritmo específico:
    # analysis.detailed_analysis('Random Forest')