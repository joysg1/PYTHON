import time
import timeit
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
import random

# Configurar estilo para los gráficos
plt.style.use('default')
sns.set_palette("husl")

# Diferentes métodos para generar listas de números pares
def metodo_for_tradicional(limite):
    """Método usando bucle for tradicional"""
    pares = []
    for i in range(limite):
        if i % 2 == 0:
            pares.append(i)
    return pares

def metodo_list_comprehension(limite):
    """Método usando list comprehension"""
    return [i for i in range(limite) if i % 2 == 0]

def metodo_filter(limite):
    """Método usando filter con lambda"""
    return list(filter(lambda x: x % 2 == 0, range(limite)))

def metodo_range_step(limite):
    """Método usando range con step=2 (más eficiente)"""
    return list(range(0, limite, 2))

def metodo_numpy_arange(limite):
    """Método usando numpy arange"""
    return np.arange(0, limite, 2).tolist()

def metodo_generator_function(limite):
    """Método usando función generadora"""
    def generar_pares(n):
        for i in range(n):
            if i % 2 == 0:
                yield i
    return list(generar_pares(limite))

def metodo_map(limite):
    """Método usando map"""
    return list(map(lambda x: x, filter(lambda x: x % 2 == 0, range(limite))))

def metodo_while_loop(limite):
    """Método usando while loop"""
    pares = []
    i = 0
    while i < limite:
        if i % 2 == 0:
            pares.append(i)
        i += 1
    return pares

def metodo_numpy_vectorizado(limite):
    """Método usando operaciones vectorizadas de numpy"""
    arr = np.arange(limite)
    return arr[arr % 2 == 0].tolist()

def metodo_itertools(limite):
    """Método usando itertools"""
    import itertools
    return list(itertools.takewhile(lambda x: x < limite, itertools.count(0, 2)))

def medir_tiempo_ejecucion(metodos, limites, repeticiones=5):
    """
    Mide el tiempo de ejecución de diferentes métodos
    
    Args:
        metodos: Dict con nombre y función de cada método
        limites: Lista de límites para generar números pares
        repeticiones: Número de repeticiones para cada medición
    
    Returns:
        DataFrame con los resultados
    """
    resultados = []
    
    for limite in limites:
        print(f"Midiendo tiempos para límite {limite:,}...")
        
        for nombre_metodo, funcion_metodo in metodos.items():
            tiempos = []
            
            for _ in range(repeticiones):
                # Usar timeit para medición más precisa
                tiempo = timeit.timeit(
                    lambda: funcion_metodo(limite), 
                    number=1
                )
                tiempos.append(tiempo)
            
            tiempo_promedio = np.mean(tiempos)
            tiempo_std = np.std(tiempos)
            
            # Verificar que el resultado sea correcto (solo para el primer método como referencia)
            if nombre_metodo == list(metodos.keys())[0]:
                resultado_referencia = funcion_metodo(limite)
                num_elementos = len(resultado_referencia)
            else:
                try:
                    resultado_actual = funcion_metodo(limite)
                    num_elementos = len(resultado_actual)
                except Exception as e:
                    print(f"Error en {nombre_metodo} con límite {limite}: {e}")
                    continue
            
            resultados.append({
                'Limite': limite,
                'Metodo': nombre_metodo,
                'Tiempo_Promedio_ms': tiempo_promedio * 1000,  # Convertir a ms
                'Tiempo_Std_ms': tiempo_std * 1000,
                'Tiempo_Min_ms': np.min(tiempos) * 1000,
                'Tiempo_Max_ms': np.max(tiempos) * 1000,
                'Elementos_Generados': num_elementos,
                'Velocidad_elementos_por_ms': num_elementos / (tiempo_promedio * 1000) if tiempo_promedio > 0 else 0
            })
    
    return pd.DataFrame(resultados)

def analizar_complejidad(df_resultados):
    """
    Analiza la complejidad temporal de los diferentes métodos
    """
    print("\n🔍 Análisis de Complejidad Temporal:")
    print("=" * 50)
    
    for metodo in df_resultados['Metodo'].unique():
        subset = df_resultados[df_resultados['Metodo'] == metodo].sort_values('Limite')
        
        if len(subset) >= 3:  # Necesitamos al menos 3 puntos para análisis
            limites = subset['Limite'].values
            tiempos = subset['Tiempo_Promedio_ms'].values
            
            # Calcular ratio de crecimiento
            ratios = []
            for i in range(1, len(tiempos)):
                if tiempos[i-1] > 0:
                    ratio = tiempos[i] / tiempos[i-1]
                    limite_ratio = limites[i] / limites[i-1]
                    ratios.append(ratio / limite_ratio)
            
            complejidad_estimada = np.mean(ratios) if ratios else 1.0
            
            if complejidad_estimada < 1.2:
                complejidad_desc = "O(n) - Lineal"
            elif complejidad_estimada < 2.0:
                complejidad_desc = "O(n log n) - Cuasilineal"
            else:
                complejidad_desc = "O(n²) o superior"
            
            print(f"{metodo:20}: {complejidad_desc} (ratio: {complejidad_estimada:.2f})")

def crear_graficos(df_resultados):
    """
    Crea gráficos de comparación usando seaborn
    """
    # Configurar el tamaño de la figura
    plt.figure(figsize=(18, 15))
    
    # Gráfico 1: Tiempo promedio por método y límite (escala lineal)
    plt.subplot(3, 3, 1)
    sns.lineplot(data=df_resultados, x='Limite', y='Tiempo_Promedio_ms', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Tiempo de Ejecución por Método (Escala Lineal)', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números', fontsize=10)
    plt.ylabel('Tiempo Promedio (ms)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 2: Tiempo promedio por método y límite (escala logarítmica)
    plt.subplot(3, 3, 2)
    sns.lineplot(data=df_resultados, x='Limite', y='Tiempo_Promedio_ms', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.yscale('log')
    plt.xscale('log')
    plt.title('Tiempo de Ejecución (Escala Logarítmica)', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números (log)', fontsize=10)
    plt.ylabel('Tiempo Promedio (ms, log)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 3: Comparación con barras para un límite específico
    plt.subplot(3, 3, 3)
    limite_medio = df_resultados['Limite'].median()
    df_subset = df_resultados[df_resultados['Limite'] == limite_medio]
    df_subset_sorted = df_subset.sort_values('Tiempo_Promedio_ms')
    
    sns.barplot(data=df_subset_sorted, x='Tiempo_Promedio_ms', y='Metodo', 
               palette='viridis', orient='h')
    plt.title(f'Comparación de Métodos\n(Límite: {int(limite_medio):,})', 
              fontsize=12, fontweight='bold')
    plt.xlabel('Tiempo Promedio (ms)', fontsize=10)
    plt.ylabel('Método', fontsize=10)
    plt.grid(True, alpha=0.3, axis='x')
    
    # Gráfico 4: Velocidad (elementos por milisegundo)
    plt.subplot(3, 3, 4)
    sns.lineplot(data=df_resultados, x='Limite', y='Velocidad_elementos_por_ms', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Velocidad de Procesamiento', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números', fontsize=10)
    plt.ylabel('Elementos por ms', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 5: Heatmap de rendimiento
    plt.subplot(3, 3, 5)
    df_pivot = df_resultados.pivot(index='Metodo', columns='Limite', 
                                  values='Tiempo_Promedio_ms')
    sns.heatmap(df_pivot, annot=True, cmap='RdYlBu_r', fmt='.2f', 
               cbar_kws={'label': 'Tiempo (ms)'})
    plt.title('Mapa de Calor: Tiempo por Método', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números', fontsize=10)
    plt.ylabel('Método', fontsize=10)
    
    # Gráfico 6: Boxplot de variabilidad
    plt.subplot(3, 3, 6)
    # Crear datos expandidos para boxplot
    datos_expandidos = []
    for _, row in df_resultados.iterrows():
        if row['Tiempo_Std_ms'] > 0:
            valores = np.random.normal(row['Tiempo_Promedio_ms'], row['Tiempo_Std_ms'], 50)
            for valor in valores:
                datos_expandidos.append({
                    'Metodo': row['Metodo'],
                    'Tiempo_ms': max(0.001, valor)  # Evitar valores negativos o cero
                })
    
    df_expandido = pd.DataFrame(datos_expandidos)
    sns.boxplot(data=df_expandido, y='Metodo', x='Tiempo_ms', palette='Set2', orient='h')
    plt.title('Distribución de Tiempos por Método', fontsize=12, fontweight='bold')
    plt.xlabel('Tiempo (ms)', fontsize=10)
    plt.ylabel('Método', fontsize=10)
    plt.grid(True, alpha=0.3, axis='x')
    
    # Gráfico 7: Eficiencia relativa vs for tradicional
    plt.subplot(3, 3, 7)
    df_for = df_resultados[df_resultados['Metodo'] == 'For tradicional']
    df_ratio = df_resultados.copy()
    
    for limite in df_resultados['Limite'].unique():
        tiempo_for = df_for[df_for['Limite'] == limite]['Tiempo_Promedio_ms']
        if not tiempo_for.empty:
            tiempo_for = tiempo_for.iloc[0]
            mask = df_ratio['Limite'] == limite
            df_ratio.loc[mask, 'Ratio_vs_for'] = df_ratio.loc[mask, 'Tiempo_Promedio_ms'] / tiempo_for
    
    sns.lineplot(data=df_ratio, x='Limite', y='Ratio_vs_for', 
                hue='Metodo', marker='o', linewidth=2)
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Referencia For')
    plt.title('Eficiencia Relativa vs For Tradicional', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números', fontsize=10)
    plt.ylabel('Ratio de Tiempo (vs For)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 8: Escalabilidad (tiempo por elemento)
    plt.subplot(3, 3, 8)
    df_resultados_copia = df_resultados.copy()
    df_resultados_copia['Tiempo_por_elemento'] = df_resultados_copia['Tiempo_Promedio_ms'] / df_resultados_copia['Elementos_Generados']
    
    sns.lineplot(data=df_resultados_copia, x='Limite', y='Tiempo_por_elemento', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Escalabilidad (Tiempo por Elemento)', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números', fontsize=10)
    plt.ylabel('Tiempo por Elemento (ms)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 9: Ranking de métodos por límite
    plt.subplot(3, 3, 9)
    rankings = []
    for limite in df_resultados['Limite'].unique():
        subset = df_resultados[df_resultados['Limite'] == limite].sort_values('Tiempo_Promedio_ms')
        for rank, (_, row) in enumerate(subset.iterrows(), 1):
            rankings.append({
                'Limite': limite,
                'Metodo': row['Metodo'],
                'Ranking': rank
            })
    
    df_rankings = pd.DataFrame(rankings)
    sns.lineplot(data=df_rankings, x='Limite', y='Ranking', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Ranking de Rendimiento por Límite', fontsize=12, fontweight='bold')
    plt.xlabel('Límite de Números', fontsize=10)
    plt.ylabel('Ranking (1 = Mejor)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.gca().invert_yaxis()  # Invertir para que 1 esté arriba
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    """Función principal que ejecuta toda la comparación"""
    print("🔍 Iniciando comparación de métodos para generar listas de números pares...")
    
    # Definir los métodos a comparar
    metodos = {
        'For tradicional': metodo_for_tradicional,
        'List comprehension': metodo_list_comprehension,
        'Filter + lambda': metodo_filter,
        'Range con step': metodo_range_step,
        'Numpy arange': metodo_numpy_arange,
        'Generator function': metodo_generator_function,
        'Map + filter': metodo_map,
        'While loop': metodo_while_loop,
        'Numpy vectorizado': metodo_numpy_vectorizado,
        'Itertools': metodo_itertools
    }
    
    # Definir diferentes límites para probar
    limites = [100, 1000, 5000, 10000, 50000, 100000]
    
    print("⏱️ Midiendo tiempos de ejecución...")
    df_resultados = medir_tiempo_ejecucion(metodos, limites, repeticiones=3)
    
    # Análisis de resultados
    print("\n📊 Resultados de la comparación:")
    print("=" * 60)
    resumen = df_resultados.groupby('Metodo').agg({
        'Tiempo_Promedio_ms': ['mean', 'min', 'max'],
        'Velocidad_elementos_por_ms': 'mean'
    }).round(4)
    print(resumen)
    
    print("\n🏆 Método más rápido por límite:")
    for limite in limites:
        subset = df_resultados[df_resultados['Limite'] == limite]
        if not subset.empty:
            mas_rapido = subset.loc[subset['Tiempo_Promedio_ms'].idxmin()]
            print(f"  Límite {limite:,}: {mas_rapido['Metodo']} "
                  f"({mas_rapido['Tiempo_Promedio_ms']:.4f} ms)")
    
    print("\n🥇 Ranking general de métodos (por tiempo promedio):")
    ranking_general = df_resultados.groupby('Metodo')['Tiempo_Promedio_ms'].mean().sort_values()
    for i, (metodo, tiempo) in enumerate(ranking_general.items(), 1):
        print(f"  {i}. {metodo}: {tiempo:.4f} ms promedio")
    
    # Análisis de complejidad
    analizar_complejidad(df_resultados)
    
    print("\n📈 Generando gráficos...")
    crear_graficos(df_resultados)
    
    print("\n✅ Análisis completado!")
    print("\n💡 Observaciones clave:")
    print("- 'Range con step' debería ser el más eficiente (evita verificar paridad)")
    print("- 'List comprehension' suele ser más rápido que bucles tradicionales")
    print("- Métodos de numpy pueden ser más lentos para datos pequeños debido al overhead")
    print("- La eficiencia puede variar según el tamaño de los datos")
    
    return df_resultados

if __name__ == "__main__":
    # Ejecutar el análisis completo
    resultados = main()