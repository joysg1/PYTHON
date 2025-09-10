import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configurar el estilo de seaborn
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Crear datos simulados sobre el impacto de la luz azul
np.random.seed(42)

# Datos de exposición a luz azul vs diferentes métricas mentales
horas_exposicion = np.repeat([1, 2, 3, 4, 5, 6, 7, 8], 30)
ruido = np.random.normal(0, 0.5, len(horas_exposicion))

# Métricas que se ven afectadas por la luz azul
concentracion = 100 - (horas_exposicion * 8) + ruido
calidad_sueno = 100 - (horas_exposicion * 12) + ruido
fatiga_visual = (horas_exposicion * 15) + ruido
nivel_estres = (horas_exposicion * 10) + ruido

# Crear DataFrame
data = pd.DataFrame({
    'Horas_Exposicion': horas_exposicion,
    'Concentracion': np.clip(concentracion, 0, 100),
    'Calidad_Sueño': np.clip(calidad_sueno, 0, 100),
    'Fatiga_Visual': np.clip(fatiga_visual, 0, 100),
    'Nivel_Estres': np.clip(nivel_estres, 0, 100)
})

# Crear subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Impacto de la Luz Azul en Funciones Mentales', fontsize=16, fontweight='bold')

# Gráfico 1: Concentración vs Horas de exposición
sns.regplot(data=data, x='Horas_Exposicion', y='Concentracion', 
           ax=axes[0,0], color='skyblue', scatter_kws={'alpha':0.6})
axes[0,0].set_title('Concentración vs Exposición a Luz Azul')
axes[0,0].set_xlabel('Horas de Exposición Diaria')
axes[0,0].set_ylabel('Nivel de Concentración (%)')

# Gráfico 2: Calidad del sueño vs Horas de exposición
sns.regplot(data=data, x='Horas_Exposicion', y='Calidad_Sueño', 
           ax=axes[0,1], color='lightcoral', scatter_kws={'alpha':0.6})
axes[0,1].set_title('Calidad del Sueño vs Exposición a Luz Azul')
axes[0,1].set_xlabel('Horas de Exposición Diaria')
axes[0,1].set_ylabel('Calidad del Sueño (%)')

# Gráfico 3: Fatiga visual vs Horas de exposición
sns.regplot(data=data, x='Horas_Exposicion', y='Fatiga_Visual', 
           ax=axes[1,0], color='orange', scatter_kws={'alpha':0.6})
axes[1,0].set_title('Fatiga Visual vs Exposición a Luz Azul')
axes[1,0].set_xlabel('Horas de Exposición Diaria')
axes[1,0].set_ylabel('Nivel de Fatiga Visual (%)')

# Gráfico 4: Nivel de estrés vs Horas de exposición
sns.regplot(data=data, x='Horas_Exposicion', y='Nivel_Estres', 
           ax=axes[1,1], color='mediumpurple', scatter_kws={'alpha':0.6})
axes[1,1].set_title('Nivel de Estrés vs Exposición a Luz Azul')
axes[1,1].set_xlabel('Horas de Exposición Diaria')
axes[1,1].set_ylabel('Nivel de Estrés (%)')

plt.tight_layout()
plt.show()

# Crear un mapa de calor de correlaciones
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0,
           square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
plt.title('Correlaciones entre Exposición a Luz Azul y Efectos Mentales', 
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Crear un gráfico de violín para mostrar la distribución
data_melted = pd.melt(data, id_vars=['Horas_Exposicion'], 
                     value_vars=['Concentracion', 'Calidad_Sueño', 'Fatiga_Visual', 'Nivel_Estres'],
                     var_name='Metrica', value_name='Valor')

plt.figure(figsize=(12, 6))
sns.violinplot(data=data_melted, x='Metrica', y='Valor', hue='Horas_Exposicion', 
               palette='viridis', split=False)
plt.title('Distribución de Efectos Mentales por Horas de Exposición a Luz Azul')
plt.xlabel('Métrica Mental')
plt.ylabel('Valor (%)')
plt.legend(title='Horas de Exposición', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Mostrar estadísticas descriptivas
print("Estadísticas Descriptivas:")
print(data.describe())

# Mostrar correlaciones específicas
print("\nCorrelaciones con Horas de Exposición:")
correlations = data.corr()['Horas_Exposicion'].sort_values(ascending=False)
for metric, corr in correlations.items():
    if metric != 'Horas_Exposicion':
        print(f"{metric}: {corr:.3f}")