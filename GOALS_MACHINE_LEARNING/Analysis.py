import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas.plotting import scatter_matrix

# Cargar el dataset
df = pd.read_csv('/home/userlm/Documentos/Goals/understat_per_game.csv')

# Mostrar información básica del dataset
print("Información del dataset:")
print(f"Forma del dataset: {df.shape}")
print("\nPrimeras 5 filas:")
print(df.head())

# VERSIÓN OPTIMIZADA: Seleccionar solo las variables más importantes
# Reducido de 15 variables a 6-8 variables clave para mejor rendimiento
variables_clave = [
    'xG',        # Expected Goals - variable principal
    'xGA',       # Expected Goals Against - variable principal  
    'scored',    # Goles anotados - resultado real
    'missed',    # Goles perdidos - resultado real
    'xpts',      # Expected Points - resultado esperado
    'pts'        # Points - resultado real
]

# Verificar que las columnas existen en el dataframe
variables_disponibles = [col for col in variables_clave if col in df.columns]
print(f"\nVariables clave disponibles: {variables_disponibles}")

# Crear el dataset con solo las variables clave
df_optimizado = df[variables_disponibles].copy()

# MÉTODO 1: Scatter matrix básico y rápido
print("\nCreando scatter matrix básico...")
plt.figure(figsize=(12, 10))  # Reducido de 15x15 a 12x10
scatter_matrix(df_optimizado, 
               alpha=0.6, 
               figsize=(12, 10), 
               diagonal='hist',
               s=20)  # Puntos más pequeños para mejor rendimiento
plt.suptitle('Scatter Matrix Optimizado - Variables Clave', fontsize=14, y=0.95)
plt.tight_layout()
plt.show()

# MÉTODO 2: Versión con seaborn (más estético pero sigue siendo rápido)
print("\nCreando scatter matrix con seaborn...")
plt.figure(figsize=(12, 10))
g = sns.pairplot(df_optimizado, 
                 diag_kind='hist',
                 plot_kws={'alpha': 0.7, 's': 25},  # Puntos medianos
                 diag_kws={'bins': 15})  # Menos bins = más rápido

g.fig.suptitle('Scatter Matrix - Variables Clave del Rendimiento', fontsize=14, y=0.98)
plt.show()

# MÉTODO 3: Con colores por resultado (solo si existe la columna)
if 'result' in df.columns:
    print("\nCreando scatter matrix coloreado por resultado...")
    
    # Usar solo las 4 variables más importantes para este gráfico
    variables_minimas = ['xG', 'xGA', 'scored', 'pts']
    variables_minimas = [col for col in variables_minimas if col in df.columns]
    
    df_resultado = df[variables_minimas + ['result']].copy()
    
    plt.figure(figsize=(10, 8))  # Más pequeño para mejor rendimiento
    g = sns.pairplot(df_resultado, 
                     hue='result',
                     diag_kind='hist',
                     plot_kws={'alpha': 0.8, 's': 30},
                     diag_kws={'bins': 12})
    
    g.fig.suptitle('Scatter Matrix por Resultado (Variables Principales)', fontsize=14, y=0.98)
    plt.show()

# MÉTODO 4: Matriz de correlación (complemento rápido)
print("\nCreando matriz de correlación...")
plt.figure(figsize=(8, 6))  # Más compacto
correlation_matrix = df_optimizado.corr()

sns.heatmap(correlation_matrix, 
            annot=True,
            cmap='coolwarm',
            center=0,
            square=True,
            fmt='.2f',
            cbar_kws={'shrink': 0.8})

plt.title('Matriz de Correlación - Variables Clave', fontsize=12, pad=15)
plt.tight_layout()
plt.show()

# FUNCIÓN ULTRA-RÁPIDA: Para casos donde necesites velocidad máxima
def scatter_matrix_rapido(dataframe, n_vars=4):
    """
    Función para crear scatter matrix súper rápido con las variables más correlacionadas
    
    Parámetros:
    - dataframe: DataFrame con los datos
    - n_vars: número de variables a incluir (máximo recomendado: 5)
    """
    
    # Seleccionar automáticamente las variables con mayor varianza
    variables_numericas = dataframe.select_dtypes(include=[np.number]).columns
    
    # Calcular varianza y seleccionar las top N
    varianzas = dataframe[variables_numericas].var().sort_values(ascending=False)
    top_vars = varianzas.head(n_vars).index.tolist()
    
    print(f"Variables seleccionadas automáticamente: {top_vars}")
    
    df_rapido = dataframe[top_vars].copy()
    
    plt.figure(figsize=(8, 8))
    scatter_matrix(df_rapido, 
                   alpha=0.7, 
                   figsize=(8, 8), 
                   diagonal='hist',
                   s=15)  # Puntos pequeños
    
    plt.suptitle('Scatter Matrix Rápido - Top Variables', fontsize=12, y=0.95)
    plt.tight_layout()
    plt.show()

# Ejemplo de uso de función rápida
print("\nCreando scatter matrix ultra-rápido...")
scatter_matrix_rapido(df, n_vars=4)  # Solo 4 variables = muy rápido

# Estadísticas descriptivas de las variables optimizadas
print("\nEstadísticas descriptivas (variables optimizadas):")
print(df_optimizado.describe())

print("\n" + "="*60)
print("CONSEJOS PARA OPTIMIZACIÓN:")
print("="*60)
print("1. Usar máximo 6-8 variables para scatter matrix completo")
print("2. Para análisis rápido, usar solo 4-5 variables clave") 
print("3. Reducir tamaño de puntos (s=15-25)")
print("4. Usar figsize más pequeño (8x8 o 10x10)")
print("5. Menos bins en histogramas (10-15)")
print("6. Si el dataset es muy grande, considera hacer sampling:")
print("   df_sample = df.sample(n=1000)  # Solo 1000 filas aleatorias")

# BONUS: Versión con sampling para datasets muy grandes
if len(df) > 2000:
    print(f"\nDataset grande detectado ({len(df)} filas). Creando versión con sampling...")
    df_sample = df.sample(n=1000, random_state=42)  # Muestra aleatoria de 1000 filas
    
    plt.figure(figsize=(10, 8))
    g = sns.pairplot(df_sample[variables_disponibles], 
                     diag_kind='hist',
                     plot_kws={'alpha': 0.8, 's': 30})
    
    g.fig.suptitle('Scatter Matrix con Sampling (1000 filas)', fontsize=14, y=0.98)
    plt.show()

print("\nAnálisis completado con optimizaciones para mejor rendimiento!")