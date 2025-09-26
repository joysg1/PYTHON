import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. CARGAR Y EXPLORAR LOS DATOS
# ==========================================

# Cargar los datos con el nombre correcto
df_co2 = pd.read_csv('/home/userlm/Documentos/CO2_EMISSIONS_MACHINE_LEARNING/co2_emmissions_by_state_2025.csv')

print("Información básica del dataset:")
print(df_co2.head())
print("\nInfo del dataset:")
print(df_co2.info())
print("\nEstadísticas descriptivas:")
print(df_co2.describe())

# Usar df_co2 en lugar de df para el resto del análisis
df = df_co2.copy()

# ==========================================
# 2. CONFIGURACIÓN Y ANÁLISIS VISUAL
# ==========================================

# Configurar el estilo (corrigiendo el nombre del estilo)
plt.style.use('default')  # Cambio: usar 'default' en lugar de 'seaborn-v0_8'
sns.set_palette("husl")

# Crear figura con múltiples subplots
fig, axes = plt.subplots(2, 2, figsize=(20, 16))
fig.suptitle('Análisis de Distribución de Emisiones CO2 por País', fontsize=20, fontweight='bold')

# 1. Box plot de todos los países (solo top 20 por legibilidad)
ax1 = axes[0, 0]
top_20_countries = df.groupby('STATE_NAME')['CO2_QTY_TONNES'].sum().nlargest(20).index
df_top20 = df[df['STATE_NAME'].isin(top_20_countries)]

box_plot = sns.boxplot(data=df_top20, y='STATE_NAME', x='CO2_QTY_TONNES', 
                       ax=ax1, orient='h')
ax1.set_title('Top 20 Países - Distribución Mensual de Emisiones CO2', fontsize=14, fontweight='bold')
ax1.set_xlabel('Emisiones CO2 (Toneladas)', fontsize=12)
ax1.set_ylabel('País', fontsize=12)
ax1.tick_params(axis='both', labelsize=8)  # Cambio: reducir tamaño de fuente

# Añadir líneas de referencia
median_all = df_top20['CO2_QTY_TONNES'].median()
ax1.axvline(median_all, color='red', linestyle='--', alpha=0.7, 
            label=f'Mediana General: {median_all:,.0f}')
ax1.legend()

# 2. Box plot comparativo por grupos de países (basado en emisiones totales)
ax2 = axes[0, 1]
total_emissions = df.groupby('STATE_NAME')['CO2_QTY_TONNES'].sum()

# Crear grupos basados en cuartiles
q1, q2, q3 = total_emissions.quantile([0.25, 0.5, 0.75])

def classify_country(country):
    total = total_emissions[country]
    if total <= q1:
        return 'Bajas Emisiones'
    elif total <= q2:
        return 'Emisiones Medias-Bajas'
    elif total <= q3:
        return 'Emisiones Medias-Altas'
    else:
        return 'Altas Emisiones'

df['emission_group'] = df['STATE_NAME'].apply(classify_country)

sns.boxplot(data=df, x='emission_group', y='CO2_QTY_TONNES', ax=ax2)
ax2.set_title('Distribución por Grupos de Emisión', fontsize=14, fontweight='bold')
ax2.set_xlabel('Grupo de Emisión', fontsize=12)
ax2.set_ylabel('Emisiones CO2 (Toneladas)', fontsize=12)
ax2.tick_params(axis='x', rotation=45, labelsize=10)

# 3. Box plot por mes (análisis estacional)
ax3 = axes[1, 0]
# Cambio: obtener el rango correcto de meses basado en los datos reales
unique_months = sorted(df['MONTH'].unique())
month_names = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
month_mapping = {i+1: month_names[i] for i in range(len(unique_months))}
df['month_name'] = df['MONTH'].map(month_mapping)

sns.boxplot(data=df, x='month_name', y='CO2_QTY_TONNES', ax=ax3)
ax3.set_title('Distribución Mensual de Emisiones (Todos los Países)', fontsize=14, fontweight='bold')
ax3.set_xlabel('Mes', fontsize=12)
ax3.set_ylabel('Emisiones CO2 (Toneladas)', fontsize=12)
ax3.tick_params(axis='x', rotation=45, labelsize=10)

# 4. Box plot de eficiencia (CO2 por vuelo)
ax4 = axes[1, 1]
# Cambio: añadir verificación para evitar división por cero
df['co2_per_flight'] = np.where(df['TF'] > 0, df['CO2_QTY_TONNES'] / df['TF'], 0)
df_efficiency = df[df['co2_per_flight'] < df['co2_per_flight'].quantile(0.95)]

# Top 15 países por número total de vuelos para el análisis de eficiencia
top_15_flights = df.groupby('STATE_NAME')['TF'].sum().nlargest(15).index
df_efficiency_top15 = df_efficiency[df_efficiency['STATE_NAME'].isin(top_15_flights)]

sns.boxplot(data=df_efficiency_top15, y='STATE_NAME', x='co2_per_flight', 
            ax=ax4, orient='h')
ax4.set_title('Eficiencia: CO2 por Vuelo (Top 15 países por vuelos)', fontsize=14, fontweight='bold')
ax4.set_xlabel('CO2 por Vuelo (Toneladas)', fontsize=12)
ax4.set_ylabel('País', fontsize=12)
ax4.tick_params(axis='both', labelsize=8)

plt.tight_layout()
plt.show()

# ==========================================
# ANÁLISIS DETALLADO DE OUTLIERS
# ==========================================

print("="*80)
print("ANÁLISIS DETALLADO DE OUTLIERS")
print("="*80)

# Función para detectar outliers usando IQR
def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

# Análisis de outliers para emisiones CO2
outliers, lower, upper = detect_outliers(df, 'CO2_QTY_TONNES')

print(f"\n1. OUTLIERS EN EMISIONES CO2:")
print(f"   Límite inferior: {lower:,.0f} toneladas")
print(f"   Límite superior: {upper:,.0f} toneladas")
print(f"   Número de outliers detectados: {len(outliers)}")

if len(outliers) > 0:
    print(f"\n   Top 10 outliers más altos:")
    top_outliers = outliers.nlargest(10, 'CO2_QTY_TONNES')[['STATE_NAME', 'MONTH', 'CO2_QTY_TONNES', 'TF']]
    for idx, row in top_outliers.iterrows():
        print(f"   - {row['STATE_NAME']}, Mes {int(row['MONTH'])}: {row['CO2_QTY_TONNES']:,.0f} toneladas ({int(row['TF'])} vuelos)")

# Análisis por país de los outliers
print(f"\n2. PAÍSES CON MÁS OUTLIERS:")
outlier_counts = outliers['STATE_NAME'].value_counts().head(10)
for country, count in outlier_counts.items():
    total_months = df[df['STATE_NAME'] == country].shape[0]
    percentage = (count / total_months) * 100
    print(f"   - {country}: {count}/{total_months} meses ({percentage:.1f}%)")

# Estadísticas descriptivas por grupo
print(f"\n3. ESTADÍSTICAS POR GRUPO DE EMISIÓN:")
stats = df.groupby('emission_group')['CO2_QTY_TONNES'].agg(['count', 'mean', 'std', 'min', 'max']).round(0)
print(stats)

# Análisis de eficiencia
print(f"\n4. ANÁLISIS DE EFICIENCIA (CO2 por vuelo):")
# Cambio: filtrar países con datos válidos de eficiencia
valid_efficiency = df[df['co2_per_flight'] > 0]
efficiency_stats = valid_efficiency.groupby('STATE_NAME')['co2_per_flight'].agg(['mean', 'std']).round(2)
efficiency_stats = efficiency_stats.sort_values('mean', ascending=False)

print(f"\n   Países MENOS eficientes (más CO2 por vuelo):")
print(efficiency_stats.head(10).to_string())
print(f"\n   Países MÁS eficientes (menos CO2 por vuelo):")
print(efficiency_stats.tail(10).to_string())

print(f"\n5. ANÁLISIS ESTACIONAL:")
seasonal_stats = df.groupby('MONTH')['CO2_QTY_TONNES'].agg(['mean', 'std', 'min', 'max']).round(0)
# Cambio: mapear correctamente los nombres de los meses
seasonal_stats.index = [month_mapping.get(month, f'Mes {month}') for month in seasonal_stats.index]
print(seasonal_stats.to_string())

print("\n" + "="*80)
print("INTERPRETACIÓN DE RESULTADOS:")
print("="*80)
print("• Los outliers indican meses con actividad aérea inusualmente alta")
print("• Países con más outliers suelen ser hubs aéreos importantes")
print("• La eficiencia varía significativamente entre países")
print("• Los patrones estacionales muestran picos en meses de verano")
print("="*80)

# ==========================================
# 3. INFORMACIÓN ADICIONAL DEL DATASET
# ==========================================
print("\n" + "="*80)
print("INFORMACIÓN ADICIONAL DEL DATASET:")
print("="*80)
print(f"• Total de registros: {len(df):,}")
print(f"• Total de países: {df['STATE_NAME'].nunique()}")
print(f"• Meses incluidos: {sorted(df['MONTH'].unique())}")
print(f"• Rango de fechas: {df['FLIGHT_MONTH'].min()} a {df['FLIGHT_MONTH'].max()}")
print(f"• Total emisiones CO2: {df['CO2_QTY_TONNES'].sum():,.0f} toneladas")
print(f"• Total vuelos: {df['TF'].sum():,}")
print("="*80)
