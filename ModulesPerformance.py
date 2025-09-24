import time
import timeit
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import importlib
import sys
import subprocess
import tempfile
import os

# Configurar estilo para los gráficos
plt.style.use('default')
sns.set_palette("husl")

def crear_modulos_prueba():
    """
    Crea módulos temporales para las pruebas
    """
    # Crear un directorio temporal para nuestros módulos de prueba
    temp_dir = tempfile.mkdtemp()
    sys.path.insert(0, temp_dir)
    
    # Módulo matemático simple
    modulo_math = """
import math

def calcular_factorial(n):
    return math.factorial(n)

def calcular_seno(x):
    return math.sin(x)

def calcular_raiz(x):
    return math.sqrt(x)

def operaciones_complejas(x):
    return math.sin(x) * math.cos(x) + math.sqrt(x) + math.factorial(min(x, 10))
"""

    # Módulo con operaciones de string
    modulo_string = """
import re
import string

def procesar_texto(texto):
    return texto.upper().strip()

def validar_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generar_password(longitud=8):
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(longitud))

def operaciones_string_complejas(texto):
    return re.sub(r'\\s+', ' ', texto.strip().upper())
"""

    # Módulo con operaciones de fecha
    modulo_fecha = """
import datetime
import calendar

def obtener_fecha_actual():
    return datetime.datetime.now()

def calcular_diferencia_dias(fecha1, fecha2):
    return abs((fecha1 - fecha2).days)

def es_bisiesto(año):
    return calendar.isleap(año)

def operaciones_fecha_complejas():
    now = datetime.datetime.now()
    return {
        'año': now.year,
        'mes': now.month,
        'es_bisiesto': calendar.isleap(now.year),
        'dias_mes': calendar.monthrange(now.year, now.month)[1]
    }
"""

    # Escribir los módulos
    modulos = {
        'test_math_module': modulo_math,
        'test_string_module': modulo_string,
        'test_fecha_module': modulo_fecha
    }
    
    for nombre, contenido in modulos.items():
        with open(os.path.join(temp_dir, f"{nombre}.py"), 'w') as f:
            f.write(contenido)
    
    return temp_dir

def metodo_sin_import(operaciones=1000):
    """Método que realiza operaciones sin imports dentro de la función"""
    def operaciones_matematicas():
        import math
        import datetime
        import re
        
        resultados = []
        for i in range(operaciones):
            # Operaciones matemáticas
            x = i + 1
            resultado = math.sin(x) + math.sqrt(x) + (math.factorial(min(x, 10)) if x <= 10 else 1)
            
            # Operaciones de fecha
            fecha = datetime.datetime.now()
            
            # Operación de string
            texto = f"Resultado {resultado}"
            texto_procesado = re.sub(r'\\s+', ' ', texto.strip().upper())
            
            resultados.append((resultado, fecha, texto_procesado))
        
        return len(resultados)
    
    return operaciones_matematicas()

def metodo_import_completo(operaciones=1000):
    """Método que importa módulos completos"""
    import math
    import datetime
    import re
    
    def operaciones_matematicas():
        resultados = []
        for i in range(operaciones):
            # Operaciones matemáticas
            x = i + 1
            resultado = math.sin(x) + math.sqrt(x) + (math.factorial(min(x, 10)) if x <= 10 else 1)
            
            # Operaciones de fecha
            fecha = datetime.datetime.now()
            
            # Operación de string
            texto = f"Resultado {resultado}"
            texto_procesado = re.sub(r'\\s+', ' ', texto.strip().upper())
            
            resultados.append((resultado, fecha, texto_procesado))
        
        return len(resultados)
    
    return operaciones_matematicas()

def metodo_import_especifico(operaciones=1000):
    """Método que importa funciones específicas"""
    from math import sin, sqrt, factorial
    from datetime import datetime
    from re import sub
    
    def operaciones_matematicas():
        resultados = []
        for i in range(operaciones):
            # Operaciones matemáticas
            x = i + 1
            resultado = sin(x) + sqrt(x) + (factorial(min(x, 10)) if x <= 10 else 1)
            
            # Operaciones de fecha
            fecha = datetime.now()
            
            # Operación de string
            texto = f"Resultado {resultado}"
            texto_procesado = sub(r'\\s+', ' ', texto.strip().upper())
            
            resultados.append((resultado, fecha, texto_procesado))
        
        return len(resultados)
    
    return operaciones_matematicas()

def metodo_import_global():
    """Método con imports globales (ya importados al inicio del script)"""
    def operaciones_matematicas(operaciones=1000):
        resultados = []
        for i in range(operaciones):
            # Usar numpy (ya importado globalmente)
            x = i + 1
            resultado = np.sin(x) + np.sqrt(x) + (1 if x > 10 else np.math.factorial(min(x, 10)))
            
            # Usar pandas (ya importado globalmente)
            fecha = pd.Timestamp.now()
            
            # Operación de string simple
            texto = f"Resultado {resultado}"
            texto_procesado = texto.strip().upper()
            
            resultados.append((resultado, fecha, texto_procesado))
        
        return len(resultados)
    
    return operaciones_matematicas

def metodo_import_as(operaciones=1000):
    """Método que usa alias en los imports"""
    import math as m
    import datetime as dt
    import re as regex
    
    def operaciones_matematicas():
        resultados = []
        for i in range(operaciones):
            # Operaciones matemáticas
            x = i + 1
            resultado = m.sin(x) + m.sqrt(x) + (m.factorial(min(x, 10)) if x <= 10 else 1)
            
            # Operaciones de fecha
            fecha = dt.datetime.now()
            
            # Operación de string
            texto = f"Resultado {resultado}"
            texto_procesado = regex.sub(r'\\s+', ' ', texto.strip().upper())
            
            resultados.append((resultado, fecha, texto_procesado))
        
        return len(resultados)
    
    return operaciones_matematicas()

def metodo_import_modulos_personalizados(operaciones=1000):
    """Método que importa módulos personalizados completos"""
    import test_math_module
    import test_string_module
    import test_fecha_module
    
    def operaciones_personalizadas():
        resultados = []
        for i in range(min(operaciones, 100)):  # Reducir para evitar factoriales muy grandes
            x = i + 1
            
            # Usar módulos personalizados
            resultado_math = test_math_module.operaciones_complejas(x)
            info_fecha = test_fecha_module.operaciones_fecha_complejas()
            password = test_string_module.generar_password(8)
            
            resultados.append((resultado_math, info_fecha, password))
        
        return len(resultados)
    
    return operaciones_personalizadas()

def metodo_import_from_personalizados(operaciones=1000):
    """Método que importa funciones específicas de módulos personalizados"""
    from test_math_module import operaciones_complejas
    from test_string_module import generar_password
    from test_fecha_module import operaciones_fecha_complejas
    
    def operaciones_personalizadas():
        resultados = []
        for i in range(min(operaciones, 100)):  # Reducir para evitar factoriales muy grandes
            x = i + 1
            
            # Usar funciones importadas específicamente
            resultado_math = operaciones_complejas(x)
            info_fecha = operaciones_fecha_complejas()
            password = generar_password(8)
            
            resultados.append((resultado_math, info_fecha, password))
        
        return len(resultados)
    
    return operaciones_personalizadas()

def metodo_importlib(operaciones=1000):
    """Método que usa importlib para imports dinámicos"""
    def operaciones_dinamicas():
        # Import dinámico
        math_module = importlib.import_module('math')
        datetime_module = importlib.import_module('datetime')
        re_module = importlib.import_module('re')
        
        resultados = []
        for i in range(operaciones):
            x = i + 1
            resultado = math_module.sin(x) + math_module.sqrt(x)
            fecha = datetime_module.datetime.now()
            texto = f"Resultado {resultado}"
            texto_procesado = re_module.sub(r'\\s+', ' ', texto.strip().upper())
            
            resultados.append((resultado, fecha, texto_procesado))
        
        return len(resultados)
    
    return operaciones_dinamicas()

def medir_tiempo_imports(metodos, tamaños_operaciones, repeticiones=3):
    """
    Mide el tiempo de diferentes métodos de import
    
    Args:
        metodos: Dict con nombre y función de cada método
        tamaños_operaciones: Lista de números de operaciones a realizar
        repeticiones: Número de repeticiones para cada medición
    
    Returns:
        DataFrame con los resultados
    """
    resultados = []
    
    for num_operaciones in tamaños_operaciones:
        print(f"Midiendo tiempos para {num_operaciones:,} operaciones...")
        
        for nombre_metodo, funcion_metodo in metodos.items():
            tiempos = []
            
            for rep in range(repeticiones):
                try:
                    if nombre_metodo == 'Import global':
                        # Caso especial para el método global
                        func = funcion_metodo()
                        tiempo = timeit.timeit(
                            lambda: func(num_operaciones), 
                            number=1
                        )
                    else:
                        tiempo = timeit.timeit(
                            lambda: funcion_metodo(num_operaciones), 
                            number=1
                        )
                    tiempos.append(tiempo)
                except Exception as e:
                    print(f"Error en {nombre_metodo} con {num_operaciones} operaciones: {e}")
                    tiempos.append(float('inf'))  # Tiempo infinito para errores
            
            tiempos = [t for t in tiempos if t != float('inf')]  # Remover errores
            if tiempos:  # Solo si tenemos mediciones válidas
                tiempo_promedio = np.mean(tiempos)
                tiempo_std = np.std(tiempos)
                
                resultados.append({
                    'Num_Operaciones': num_operaciones,
                    'Metodo': nombre_metodo,
                    'Tiempo_Promedio_ms': tiempo_promedio * 1000,
                    'Tiempo_Std_ms': tiempo_std * 1000,
                    'Tiempo_Min_ms': np.min(tiempos) * 1000,
                    'Tiempo_Max_ms': np.max(tiempos) * 1000,
                    'Tiempo_por_operacion_us': (tiempo_promedio * 1000000) / num_operaciones,
                    'Operaciones_por_segundo': num_operaciones / tiempo_promedio if tiempo_promedio > 0 else 0
                })
    
    return pd.DataFrame(resultados)

def analizar_overhead_imports(df_resultados):
    """
    Analiza el overhead específico de los diferentes tipos de import
    """
    print("\n🔍 Análisis de Overhead de Imports:")
    print("=" * 60)
    
    # Calcular overhead promedio por método
    overhead_por_metodo = df_resultados.groupby('Metodo').agg({
        'Tiempo_por_operacion_us': 'mean',
        'Operaciones_por_segundo': 'mean'
    }).round(4)
    
    print("Tiempo promedio por operación (microsegundos):")
    print(overhead_por_metodo['Tiempo_por_operacion_us'].sort_values())
    
    print("\nOperaciones promedio por segundo:")
    print(overhead_por_metodo['Operaciones_por_segundo'].sort_values(ascending=False))
    
    # Análisis de escalabilidad
    print("\n📈 Análisis de Escalabilidad:")
    for metodo in df_resultados['Metodo'].unique():
        subset = df_resultados[df_resultados['Metodo'] == metodo].sort_values('Num_Operaciones')
        
        if len(subset) >= 2:
            primer_tiempo = subset.iloc[0]['Tiempo_por_operacion_us']
            ultimo_tiempo = subset.iloc[-1]['Tiempo_por_operacion_us']
            
            if primer_tiempo > 0:
                factor_escalabilidad = ultimo_tiempo / primer_tiempo
                if factor_escalabilidad < 1.1:
                    escalabilidad = "Excelente (O(1))"
                elif factor_escalabilidad < 2.0:
                    escalabilidad = "Buena (casi O(1))"
                else:
                    escalabilidad = "Regular (overhead creciente)"
                
                print(f"{metodo:25}: {escalabilidad} (factor: {factor_escalabilidad:.2f})")

def crear_graficos_imports(df_resultados):
    """
    Crea gráficos específicos para analizar imports
    """
    plt.figure(figsize=(20, 16))
    
    # Gráfico 1: Tiempo total por método
    plt.subplot(3, 3, 1)
    sns.lineplot(data=df_resultados, x='Num_Operaciones', y='Tiempo_Promedio_ms', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Tiempo Total de Ejecución', fontsize=12, fontweight='bold')
    plt.xlabel('Número de Operaciones', fontsize=10)
    plt.ylabel('Tiempo Promedio (ms)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 2: Tiempo por operación (overhead)
    plt.subplot(3, 3, 2)
    sns.lineplot(data=df_resultados, x='Num_Operaciones', y='Tiempo_por_operacion_us', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Overhead por Operación', fontsize=12, fontweight='bold')
    plt.xlabel('Número de Operaciones', fontsize=10)
    plt.ylabel('Tiempo por Operación (μs)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 3: Operaciones por segundo
    plt.subplot(3, 3, 3)
    sns.lineplot(data=df_resultados, x='Num_Operaciones', y='Operaciones_por_segundo', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Throughput (Operaciones por Segundo)', fontsize=12, fontweight='bold')
    plt.xlabel('Número de Operaciones', fontsize=10)
    plt.ylabel('Operaciones por Segundo', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 4: Comparación de overhead promedio
    plt.subplot(3, 3, 4)
    overhead_promedio = df_resultados.groupby('Metodo')['Tiempo_por_operacion_us'].mean().reset_index()
    overhead_promedio = overhead_promedio.sort_values('Tiempo_por_operacion_us')
    
    sns.barplot(data=overhead_promedio, y='Metodo', x='Tiempo_por_operacion_us', 
               palette='viridis', orient='h')
    plt.title('Overhead Promedio por Método', fontsize=12, fontweight='bold')
    plt.xlabel('Tiempo por Operación (μs)', fontsize=10)
    plt.ylabel('Método', fontsize=10)
    plt.grid(True, alpha=0.3, axis='x')
    
    # Gráfico 5: Heatmap de rendimiento
    plt.subplot(3, 3, 5)
    df_pivot = df_resultados.pivot(index='Metodo', columns='Num_Operaciones', 
                                  values='Tiempo_por_operacion_us')
    sns.heatmap(df_pivot, annot=True, cmap='RdYlBu_r', fmt='.2f', 
               cbar_kws={'label': 'Tiempo por op (μs)'})
    plt.title('Heatmap: Overhead por Método', fontsize=12, fontweight='bold')
    plt.xlabel('Número de Operaciones', fontsize=10)
    plt.ylabel('Método', fontsize=10)
    
    # Gráfico 6: Escalabilidad
    plt.subplot(3, 3, 6)
    sns.scatterplot(data=df_resultados, x='Num_Operaciones', y='Tiempo_por_operacion_us', 
                   hue='Metodo', s=80, alpha=0.7)
    plt.title('Escalabilidad del Overhead', fontsize=12, fontweight='bold')
    plt.xlabel('Número de Operaciones', fontsize=10)
    plt.ylabel('Tiempo por Operación (μs)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 7: Eficiencia relativa vs import específico
    plt.subplot(3, 3, 7)
    metodo_referencia = 'Import específico'
    if metodo_referencia in df_resultados['Metodo'].values:
        df_ref = df_resultados[df_resultados['Metodo'] == metodo_referencia]
        df_ratio = df_resultados.copy()
        
        for num_ops in df_resultados['Num_Operaciones'].unique():
            tiempo_ref = df_ref[df_ref['Num_Operaciones'] == num_ops]['Tiempo_por_operacion_us']
            if not tiempo_ref.empty:
                tiempo_ref = tiempo_ref.iloc[0]
                mask = df_ratio['Num_Operaciones'] == num_ops
                df_ratio.loc[mask, 'Ratio_vs_ref'] = df_ratio.loc[mask, 'Tiempo_por_operacion_us'] / tiempo_ref
        
        sns.lineplot(data=df_ratio, x='Num_Operaciones', y='Ratio_vs_ref', 
                    hue='Metodo', marker='o', linewidth=2)
        plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label=f'Referencia {metodo_referencia}')
        plt.title(f'Eficiencia Relativa vs {metodo_referencia}', fontsize=12, fontweight='bold')
        plt.xlabel('Número de Operaciones', fontsize=10)
        plt.ylabel('Ratio de Overhead', fontsize=10)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
        plt.grid(True, alpha=0.3)
    
    # Gráfico 8: Distribución de tiempos
    plt.subplot(3, 3, 8)
    # Crear boxplot con datos simulados basados en std
    datos_expandidos = []
    for _, row in df_resultados.iterrows():
        if row['Tiempo_Std_ms'] > 0:
            valores = np.random.normal(row['Tiempo_por_operacion_us'], 
                                     row['Tiempo_Std_ms'] * 1000, 30)  # convertir ms a μs
            for valor in valores:
                datos_expandidos.append({
                    'Metodo': row['Metodo'],
                    'Tiempo_us': max(0.1, valor)
                })
    
    if datos_expandidos:
        df_expandido = pd.DataFrame(datos_expandidos)
        sns.violinplot(data=df_expandido, y='Metodo', x='Tiempo_us', 
                      palette='Set3', orient='h')
        plt.title('Distribución de Overhead por Método', fontsize=12, fontweight='bold')
        plt.xlabel('Tiempo por Operación (μs)', fontsize=10)
        plt.ylabel('Método', fontsize=10)
        plt.grid(True, alpha=0.3, axis='x')
    
    # Gráfico 9: Ranking dinámico
    plt.subplot(3, 3, 9)
    rankings = []
    for num_ops in df_resultados['Num_Operaciones'].unique():
        subset = df_resultados[df_resultados['Num_Operaciones'] == num_ops].sort_values('Tiempo_por_operacion_us')
        for rank, (_, row) in enumerate(subset.iterrows(), 1):
            rankings.append({
                'Num_Operaciones': num_ops,
                'Metodo': row['Metodo'],
                'Ranking': rank
            })
    
    df_rankings = pd.DataFrame(rankings)
    sns.lineplot(data=df_rankings, x='Num_Operaciones', y='Ranking', 
                hue='Metodo', marker='o', linewidth=2, markersize=6)
    plt.title('Ranking de Eficiencia por Tamaño', fontsize=12, fontweight='bold')
    plt.xlabel('Número de Operaciones', fontsize=10)
    plt.ylabel('Ranking (1 = Mejor)', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.gca().invert_yaxis()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    """Función principal que ejecuta toda la comparación de imports"""
    print("🔍 Iniciando comparación de métodos de import...")
    
    # Crear módulos de prueba
    print("📦 Creando módulos de prueba...")
    temp_dir = crear_modulos_prueba()
    
    try:
        # Definir los métodos a comparar
        metodos = {
            'Sin import (local)': metodo_sin_import,
            'Import completo': metodo_import_completo,
            'Import específico': metodo_import_especifico,
            'Import global': metodo_import_global,
            'Import con alias': metodo_import_as,
            'Import módulos custom': metodo_import_modulos_personalizados,
            'From módulos custom': metodo_import_from_personalizados,
            'Import dinámico': metodo_importlib
        }
        
        # Diferentes números de operaciones para probar
        tamaños_operaciones = [100, 500, 1000, 2000, 5000]
        
        print("⏱️ Midiendo tiempos de ejecución...")
        df_resultados = medir_tiempo_imports(metodos, tamaños_operaciones, repeticiones=3)
        
        if df_resultados.empty:
            print("❌ No se pudieron obtener resultados de las mediciones.")
            return None
        
        # Análisis de resultados
        print("\n📊 Resultados de la comparación de imports:")
        print("=" * 70)
        resumen = df_resultados.groupby('Metodo').agg({
            'Tiempo_Promedio_ms': ['mean', 'min', 'max'],
            'Tiempo_por_operacion_us': 'mean',
            'Operaciones_por_segundo': 'mean'
        }).round(4)
        print(resumen)
        
        print("\n🏆 Método más eficiente por número de operaciones:")
        for num_ops in tamaños_operaciones:
            subset = df_resultados[df_resultados['Num_Operaciones'] == num_ops]
            if not subset.empty:
                mas_eficiente = subset.loc[subset['Tiempo_por_operacion_us'].idxmin()]
                print(f"  {num_ops:,} ops: {mas_eficiente['Metodo']} "
                      f"({mas_eficiente['Tiempo_por_operacion_us']:.2f} μs/op)")
        
        print("\n🥇 Ranking general de métodos (por overhead promedio):")
        ranking_overhead = df_resultados.groupby('Metodo')['Tiempo_por_operacion_us'].mean().sort_values()
        for i, (metodo, overhead) in enumerate(ranking_overhead.items(), 1):
            print(f"  {i}. {metodo}: {overhead:.2f} μs por operación")
        
        # Análisis específico de imports
        analizar_overhead_imports(df_resultados)
        
        print("\n📈 Generando gráficos...")
        crear_graficos_imports(df_resultados)
        
        print("\n✅ Análisis de imports completado!")
        print("\n💡 Observaciones clave:")
        print("- Imports específicos (from module import function) suelen ser más rápidos")
        print("- Imports globales eliminan overhead pero aumentan uso de memoria")
        print("- Imports dentro de funciones añaden overhead por llamada")
        print("- Módulos personalizados pueden tener overhead de carga inicial")
        print("- Import dinámico con importlib es útil pero más lento")
        
        return df_resultados
        
    finally:
        # Limpiar módulos temporales
        if temp_dir in sys.path:
            sys.path.remove(temp_dir)
        
        # Limpiar cache de módulos importados
        modulos_a_limpiar = [mod for mod in sys.modules.keys() 
                           if mod.startswith('test_') and 'module' in mod]
        for mod in modulos_a_limpiar:
            if mod in sys.modules:
                del sys.modules[mod]

if __name__ == "__main__":
    # Ejecutar el análisis completo
    resultados = main()