import time
import timeit
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
import string
import random

# Configurar estilo para los gráficos
plt.style.use('default')
sns.set_palette("husl")

def generar_cadenas_aleatorias(longitudes, num_cadenas=1000):
    """
    Genera cadenas aleatorias de diferentes longitudes
    
    Args:
        longitudes: Lista de longitudes de cadenas a generar
        num_cadenas: Número de cadenas por longitud
    
    Returns:
        Dict con cadenas organizadas por longitud
    """
    cadenas_por_longitud = {}
    caracteres = string.ascii_letters + string.digits + " "
    
    for longitud in longitudes:
        cadenas = []
        for _ in range(num_cadenas):
            cadena = ''.join(random.choice(caracteres) for _ in range(longitud))
            cadenas.append(cadena)
        cadenas_por_longitud[longitud] = cadenas
    
    return cadenas_por_longitud

# Diferentes métodos para calcular la longitud de cadenas
def metodo_len_builtin(cadenas):
    """Método usando len() built-in"""
    return [len(cadena) for cadena in cadenas]

def metodo_contador_manual(cadenas):
    """Método contando caracteres manualmente"""
    resultados = []
    for cadena in cadenas:
        contador = 0
        for _ in cadena:
            contador += 1
        resultados.append(contador)
    return resultados

def metodo_sum_generator(cadenas):
    """Método usando sum() con generator expression"""
    return [sum(1 for _ in cadena) for cadena in cadenas]

def metodo_numpy(cadenas):
    """Método usando numpy (convertir a array y usar size)"""
    return [len(np.array(list(cadena))) for cadena in cadenas]

def metodo_reduce(cadenas):
    """Método usando functools.reduce"""
    from functools import reduce
    return [reduce(lambda x, y: x + 1, cadena, 0) for cadena in cadenas]

def medir_tiempo_ejecucion(metodos, cadenas_por_longitud, repeticiones=5):
    """
    Mide el tiempo de ejecución de diferentes métodos
    
    Args:
        metodos: Dict con nombre y función de cada método
        cadenas_por_longitud: Dict con cadenas organizadas por longitud
        repeticiones: Número de repeticiones para cada medición
    
    Returns:
        DataFrame con los resultados
    """
    resultados = []
    
    for longitud, cadenas in cadenas_por_longitud.items():
        print(f"Midiendo tiempos para cadenas de longitud {longitud}...")
        
        for nombre_metodo, funcion_metodo in metodos.items():
            tiempos = []
            
            for _ in range(repeticiones):
                # Usar timeit para medición más precisa
                tiempo = timeit.timeit(
                    lambda: funcion_metodo(cadenas), 
                    number=1
                )
                tiempos.append(tiempo)
            
            tiempo_promedio = np.mean(tiempos)
            tiempo_std = np.std(tiempos)
            
            resultados.append({
                'Longitud_Cadena': longitud,
                'Metodo': nombre_metodo,
                'Tiempo_Promedio_ms': tiempo_promedio * 1000,  # Convertir a ms
                'Tiempo_Std_ms': tiempo_std * 1000,
                'Tiempo_Min_ms': np.min(tiempos) * 1000,
                'Tiempo_Max_ms': np.max(tiempos) * 1000
            })
    
    return pd.DataFrame(resultados)

def crear_graficos(df_resultados):
    """
    Crea gráficos de comparación usando seaborn
    """
    # Configurar el tamaño de la figura
    plt.figure(figsize=(15, 12))
    
    # Gráfico 1: Tiempo promedio por método y longitud
    plt.subplot(2, 2, 1)
    sns.lineplot(data=df_resultados, x='Longitud_Cadena', y='Tiempo_Promedio_ms', 
                hue='Metodo', marker='o', linewidth=2, markersize=8)
    plt.title('Tiempo de Ejecución por Método vs Longitud de Cadena', fontsize=14, fontweight='bold')
    plt.xlabel('Longitud de la Cadena', fontsize=12)
    plt.ylabel('Tiempo Promedio (ms)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    # Gráfico 2: Comparación con barras para una longitud específica
    plt.subplot(2, 2, 2)
    longitud_media = df_resultados['Longitud_Cadena'].median()
    df_subset = df_resultados[df_resultados['Longitud_Cadena'] == longitud_media]
    
    sns.barplot(data=df_subset, x='Metodo', y='Tiempo_Promedio_ms', 
               palette='viridis', errorbar=('sd'))
    plt.title(f'Comparación de Métodos (Cadenas de {int(longitud_media)} caracteres)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Método', fontsize=12)
    plt.ylabel('Tiempo Promedio (ms)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 3: Boxplot para mostrar variabilidad
    plt.subplot(2, 2, 3)
    # Crear datos expandidos para boxplot
    datos_expandidos = []
    for _, row in df_resultados.iterrows():
        # Simular distribución normal basada en promedio y std
        valores = np.random.normal(row['Tiempo_Promedio_ms'], row['Tiempo_Std_ms'], 100)
        for valor in valores:
            datos_expandidos.append({
                'Metodo': row['Metodo'],
                'Tiempo_ms': max(0, valor)  # Evitar valores negativos
            })
    
    df_expandido = pd.DataFrame(datos_expandidos)
    sns.boxplot(data=df_expandido, x='Metodo', y='Tiempo_ms', palette='Set2')
    plt.title('Distribución de Tiempos por Método', fontsize=14, fontweight='bold')
    plt.xlabel('Método', fontsize=12)
    plt.ylabel('Tiempo (ms)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 4: Heatmap de rendimiento
    plt.subplot(2, 2, 4)
    df_pivot = df_resultados.pivot(index='Metodo', columns='Longitud_Cadena', 
                                  values='Tiempo_Promedio_ms')
    sns.heatmap(df_pivot, annot=True, cmap='YlOrRd', fmt='.2f', cbar_kws={'label': 'Tiempo (ms)'})
    plt.title('Mapa de Calor: Tiempo por Método y Longitud', fontsize=14, fontweight='bold')
    plt.xlabel('Longitud de la Cadena', fontsize=12)
    plt.ylabel('Método', fontsize=12)
    
    plt.tight_layout()
    plt.show()
    
    # Gráfico adicional: Escalabilidad
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df_resultados, x='Longitud_Cadena', y='Tiempo_Promedio_ms', 
                   hue='Metodo', s=100, alpha=0.7)
    plt.title('Escalabilidad de los Métodos', fontsize=14, fontweight='bold')
    plt.xlabel('Longitud de la Cadena', fontsize=12)
    plt.ylabel('Tiempo Promedio (ms)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    # Eficiencia relativa (comparado con len())
    plt.subplot(1, 2, 2)
    df_len = df_resultados[df_resultados['Metodo'] == 'len() built-in']
    df_ratio = df_resultados.copy()
    
    for longitud in df_resultados['Longitud_Cadena'].unique():
        tiempo_len = df_len[df_len['Longitud_Cadena'] == longitud]['Tiempo_Promedio_ms'].iloc[0]
        mask = df_ratio['Longitud_Cadena'] == longitud
        df_ratio.loc[mask, 'Ratio_vs_len'] = df_ratio.loc[mask, 'Tiempo_Promedio_ms'] / tiempo_len
    
    sns.lineplot(data=df_ratio, x='Longitud_Cadena', y='Ratio_vs_len', 
                hue='Metodo', marker='o', linewidth=2)
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Referencia len()')
    plt.title('Eficiencia Relativa vs len()', fontsize=14, fontweight='bold')
    plt.xlabel('Longitud de la Cadena', fontsize=12)
    plt.ylabel('Ratio de Tiempo (vs len())', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    """Función principal que ejecuta toda la comparación"""
    print("🔍 Iniciando comparación de métodos para calcular longitud de cadenas...")
    
    # Definir los métodos a comparar
    metodos = {
        'len() built-in': metodo_len_builtin,
        'Contador manual': metodo_contador_manual,
        'sum() + generator': metodo_sum_generator,
        'numpy array': metodo_numpy,
        'functools.reduce': metodo_reduce
    }
    
    # Definir diferentes longitudes de cadenas para probar
    longitudes = [10, 50, 100, 500, 1000, 2000]
    
    print("📝 Generando cadenas de prueba...")
    cadenas_por_longitud = generar_cadenas_aleatorias(longitudes, num_cadenas=500)
    
    print("⏱️ Midiendo tiempos de ejecución...")
    df_resultados = medir_tiempo_ejecucion(metodos, cadenas_por_longitud, repeticiones=3)
    
    print("\n📊 Resultados de la comparación:")
    print(df_resultados.groupby('Metodo')['Tiempo_Promedio_ms'].agg(['mean', 'min', 'max']).round(4))
    
    print("\n🏆 Método más rápido por longitud de cadena:")
    for longitud in longitudes:
        subset = df_resultados[df_resultados['Longitud_Cadena'] == longitud]
        mas_rapido = subset.loc[subset['Tiempo_Promedio_ms'].idxmin()]
        print(f"  Longitud {longitud}: {mas_rapido['Metodo']} "
              f"({mas_rapido['Tiempo_Promedio_ms']:.4f} ms)")
    
    print("\n📈 Generando gráficos...")
    crear_graficos(df_resultados)
    
    print("\n✅ Análisis completado!")
    
    return df_resultados

if __name__ == "__main__":
    # Fijar semilla para reproducibilidad
    random.seed(42)
    np.random.seed(42)
    
    # Ejecutar el análisis completo
    resultados = main()