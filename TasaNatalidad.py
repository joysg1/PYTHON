import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.animation import FuncAnimation
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Datos de ejemplo de tasa de natalidad (nacimientos por 1000 habitantes)
# Datos reales aproximados del Banco Mundial
data = {
    'País': ['Níger', 'Angola', 'Mali', 'Uganda', 'Chad', 'Somalia', 'República Democrática del Congo',
             'Burkina Faso', 'Zambia', 'Malawi', 'Mozambique', 'Tanzania', 'Guinea', 'Sierra Leona',
             'Nigeria', 'Senegal', 'Gambia', 'Liberia', 'República Centroafricana', 'Guinea-Bisáu',
             'China', 'India', 'Estados Unidos', 'Brasil', 'Rusia', 'Japón', 'Alemania', 'Italia',
             'Reino Unido', 'Francia', 'Canadá', 'Australia', 'Corea del Sur', 'España'],
    'Tasa_Natalidad_2023': [47.28, 42.22, 41.60, 40.70, 40.64, 39.30, 39.24, 38.35, 36.60, 36.30,
                           35.80, 35.40, 35.20, 34.20, 33.80, 33.40, 33.20, 32.90, 32.80, 32.50,
                           7.52, 17.60, 11.00, 13.44, 8.90, 6.90, 8.30, 6.80, 10.90, 10.80,
                           9.80, 11.60, 6.40, 7.10],
    'Región': ['África', 'África', 'África', 'África', 'África', 'África', 'África', 'África',
               'África', 'África', 'África', 'África', 'África', 'África', 'África', 'África',
               'África', 'África', 'África', 'África', 'Asia', 'Asia', 'América del Norte',
               'América del Sur', 'Europa', 'Asia', 'Europa', 'Europa', 'Europa', 'Europa',
               'América del Norte', 'Oceanía', 'Asia', 'Europa'],
    'Continente': ['África', 'África', 'África', 'África', 'África', 'África', 'África', 'África',
                   'África', 'África', 'África', 'África', 'África', 'África', 'África', 'África',
                   'África', 'África', 'África', 'África', 'Asia', 'Asia', 'América', 'América',
                   'Europa', 'Asia', 'Europa', 'Europa', 'Europa', 'Europa', 'América', 'Oceanía',
                   'Asia', 'Europa']
}

# Datos históricos simulados (2000-2023)
years = list(range(2000, 2024))
np.random.seed(42)

# Crear DataFrame principal
df = pd.DataFrame(data)

# Función para crear gráfico de barras horizontales
def crear_grafico_barras():
    plt.figure(figsize=(14, 10))
    
    # Seleccionar top 20 países
    df_top20 = df.nlargest(20, 'Tasa_Natalidad_2023')
    
    # Crear gráfico de barras horizontales con colores por región
    colors = {'África': '#FF6B6B', 'Asia': '#4ECDC4', 'Europa': '#45B7D1', 
              'América': '#96CEB4', 'América del Norte': '#96CEB4', 
              'América del Sur': '#96CEB4', 'Oceanía': '#FECA57'}
    
    bar_colors = [colors[region] for region in df_top20['Región']]
    
    bars = plt.barh(range(len(df_top20)), df_top20['Tasa_Natalidad_2023'], 
                    color=bar_colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    
    plt.yticks(range(len(df_top20)), df_top20['País'])
    plt.xlabel('Tasa de Natalidad (nacimientos por 1000 habitantes)', fontsize=12)
    plt.title('Top 20 Países con Mayor Tasa de Natalidad (2023)', fontsize=16, fontweight='bold')
    
    # Agregar valores en las barras
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                f'{width:.1f}', ha='left', va='center', fontweight='bold')
    
    # Crear leyenda
    legend_elements = [plt.Rectangle((0,0),1,1, facecolor=colors[region], alpha=0.8) 
                      for region in colors.keys() if region in df_top20['Región'].values]
    legend_labels = [region for region in colors.keys() if region in df_top20['Región'].values]
    plt.legend(legend_elements, legend_labels, loc='lower right')
    
    plt.tight_layout()
    plt.grid(axis='x', alpha=0.3)
    plt.show()

# Función para crear gráfico de dispersión por región
def crear_scatter_plot():
    plt.figure(figsize=(12, 8))
    
    # Crear scatter plot
    for region in df['Región'].unique():
        df_region = df[df['Región'] == region]
        plt.scatter(df_region.index, df_region['Tasa_Natalidad_2023'], 
                   label=region, alpha=0.7, s=100)
    
    plt.xlabel('Índice de País', fontsize=12)
    plt.ylabel('Tasa de Natalidad (por 1000 habitantes)', fontsize=12)
    plt.title('Tasa de Natalidad por Región (2023)', fontsize=16, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Función para crear boxplot por continente
def crear_boxplot():
    plt.figure(figsize=(12, 8))
    
    sns.boxplot(data=df, x='Continente', y='Tasa_Natalidad_2023', palette='Set2')
    plt.xticks(rotation=45)
    plt.xlabel('Continente', fontsize=12)
    plt.ylabel('Tasa de Natalidad (por 1000 habitantes)', fontsize=12)
    plt.title('Distribución de Tasa de Natalidad por Continente (2023)', 
              fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Función para crear mapa de calor (simulado)
def crear_heatmap():
    # Crear datos simulados de tendencia histórica para algunos países
    paises_muestra = ['Níger', 'China', 'India', 'Estados Unidos', 'Alemania', 'Japón']
    df_muestra = df[df['País'].isin(paises_muestra)]
    
    # Simular datos históricos
    np.random.seed(42)
    data_historica = []
    
    for _, pais in df_muestra.iterrows():
        tasa_actual = pais['Tasa_Natalidad_2023']
        # Simular tendencia histórica
        tendencia = np.linspace(tasa_actual * 1.5, tasa_actual, len(years))
        ruido = np.random.normal(0, tasa_actual * 0.05, len(years))
        tasas_historicas = tendencia + ruido
        
        for i, year in enumerate(years):
            data_historica.append({
                'País': pais['País'],
                'Año': year,
                'Tasa_Natalidad': max(0, tasas_historicas[i])
            })
    
    df_historico = pd.DataFrame(data_historica)
    df_pivot = df_historico.pivot(index='País', columns='Año', values='Tasa_Natalidad')
    
    plt.figure(figsize=(16, 8))
    sns.heatmap(df_pivot, annot=False, cmap='YlOrRd', fmt='.1f', cbar_kws={'label': 'Tasa de Natalidad'})
    plt.title('Evolución de la Tasa de Natalidad (2000-2023)', fontsize=16, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('País', fontsize=12)
    plt.tight_layout()
    plt.show()

# Función para crear gráfico interactivo con Plotly
def crear_grafico_interactivo():
    # Gráfico de barras interactivo
    fig1 = px.bar(df.nlargest(15, 'Tasa_Natalidad_2023'), 
                  x='País', y='Tasa_Natalidad_2023',
                  color='Región',
                  title='Top 15 Países con Mayor Tasa de Natalidad (2023)',
                  labels={'Tasa_Natalidad_2023': 'Tasa de Natalidad'})
    fig1.update_xaxes(tickangle=45)
    fig1.show()
    
    # Gráfico de dispersión interactivo
    fig2 = px.scatter(df, x='País', y='Tasa_Natalidad_2023', 
                      color='Continente', size='Tasa_Natalidad_2023',
                      hover_data=['Región'],
                      title='Tasa de Natalidad Mundial por País y Continente')
    fig2.update_xaxes(tickangle=45)
    fig2.show()

# Función principal para ejecutar todas las visualizaciones
def visualizar_tasa_natalidad():
    print("🌍 VISUALIZACIÓN DE TASA DE NATALIDAD MUNDIAL 🌍\n")
    
    print("📊 Estadísticas Generales:")
    print(f"Promedio mundial: {df['Tasa_Natalidad_2023'].mean():.2f}")
    print(f"País con mayor tasa: {df.loc[df['Tasa_Natalidad_2023'].idxmax(), 'País']} ({df['Tasa_Natalidad_2023'].max():.2f})")
    print(f"País con menor tasa: {df.loc[df['Tasa_Natalidad_2023'].idxmin(), 'País']} ({df['Tasa_Natalidad_2023'].min():.2f})")
    print("\n" + "="*50 + "\n")
    
    # Crear todas las visualizaciones
    print("1. Gráfico de Barras Horizontales (Top 20)")
    crear_grafico_barras()
    
    print("2. Gráfico de Dispersión por Región")
    crear_scatter_plot()
    
    print("3. Boxplot por Continente")
    crear_boxplot()
    
    print("4. Mapa de Calor Histórico")
    crear_heatmap()
    
    print("5. Gráficos Interactivos (Plotly)")
    crear_grafico_interactivo()

# Ejecutar las visualizaciones
if __name__ == "__main__":
    visualizar_tasa_natalidad()

# INSTRUCCIONES PARA USAR DATOS REALES:
"""
Para usar datos reales del Banco Mundial, instala wbdata:
pip install wbdata

Y reemplaza los datos simulados con:

import wbdata

# Obtener datos reales de tasa de natalidad
indicator = 'SP.DYN.CBRT.IN'  # Birth rate, crude (per 1,000 people)
data_real = wbdata.get_dataframe({indicator: 'birth_rate'}, 
                                 date=(2020, 2023))

# El resto del código se mantiene igual
"""