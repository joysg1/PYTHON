import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Configurar seaborn y matplotlib
plt.style.use('default')
sns.set_palette("husl")

# Crear datos simulados de indicadores de seguridad
np.random.seed(42)

# Generar fechas para los últimos 12 meses
fechas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')

# Crear DataFrame con indicadores clave de seguridad
datos_seguridad = pd.DataFrame({
    'Mes': fechas,
    'Accidentes_Trabajo': np.random.poisson(3, len(fechas)),  # Promedio 3 por mes
    'Incidentes_Reportados': np.random.poisson(8, len(fechas)),  # Promedio 8 por mes
    'Horas_Capacitacion': np.random.normal(120, 20, len(fechas)),  # Promedio 120h por mes
    'Inspecciones_Realizadas': np.random.poisson(15, len(fechas)),  # Promedio 15 por mes
    'Tasa_Ausentismo': np.random.normal(3.5, 0.8, len(fechas)),  # Promedio 3.5%
    'Cumplimiento_EPP': np.random.normal(85, 5, len(fechas))  # Promedio 85%
})

# Añadir columna de mes como string para mejor visualización
datos_seguridad['Mes_Str'] = datos_seguridad['Mes'].dt.strftime('%b %Y')

# Crear figura con subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Indicadores Clave de Seguridad Empresarial - 2024', 
             fontsize=16, fontweight='bold', y=0.98)

# 1. Accidentes de trabajo por mes (gráfico de barras)
sns.barplot(data=datos_seguridad, x='Mes_Str', y='Accidentes_Trabajo', 
            ax=axes[0,0], color='salmon')
axes[0,0].set_title('Accidentes de Trabajo por Mes', fontweight='bold')
axes[0,0].set_xlabel('Mes')
axes[0,0].set_ylabel('Número de Accidentes')
axes[0,0].tick_params(axis='x', rotation=45)

# 2. Incidentes reportados vs accidentes (gráfico de líneas)
axes[0,1].plot(datos_seguridad['Mes'], datos_seguridad['Incidentes_Reportados'], 
               marker='o', linewidth=2, label='Incidentes Reportados', color='blue')
axes[0,1].plot(datos_seguridad['Mes'], datos_seguridad['Accidentes_Trabajo'], 
               marker='s', linewidth=2, label='Accidentes de Trabajo', color='red')
axes[0,1].set_title('Incidentes vs Accidentes', fontweight='bold')
axes[0,1].set_xlabel('Mes')
axes[0,1].set_ylabel('Cantidad')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

# 3. Horas de capacitación (gráfico de área)
axes[0,2].fill_between(datos_seguridad['Mes'], datos_seguridad['Horas_Capacitacion'], 
                       alpha=0.7, color='lightgreen')
axes[0,2].plot(datos_seguridad['Mes'], datos_seguridad['Horas_Capacitacion'], 
               color='darkgreen', linewidth=2)
axes[0,2].set_title('Horas de Capacitación en Seguridad', fontweight='bold')
axes[0,2].set_xlabel('Mes')
axes[0,2].set_ylabel('Horas')
axes[0,2].grid(True, alpha=0.3)

# 4. Inspecciones realizadas (gráfico de barras horizontales)
sns.barplot(data=datos_seguridad, y='Mes_Str', x='Inspecciones_Realizadas', 
            ax=axes[1,0], color='lightblue', orient='h')
axes[1,0].set_title('Inspecciones de Seguridad Realizadas', fontweight='bold')
axes[1,0].set_xlabel('Número de Inspecciones')
axes[1,0].set_ylabel('Mes')

# 5. Tasa de ausentismo (gráfico de líneas con puntos)
sns.lineplot(data=datos_seguridad, x='Mes', y='Tasa_Ausentismo', 
             ax=axes[1,1], marker='o', linewidth=3, color='orange')
axes[1,1].set_title('Tasa de Ausentismo por Accidentes', fontweight='bold')
axes[1,1].set_xlabel('Mes')
axes[1,1].set_ylabel('Porcentaje (%)')
axes[1,1].grid(True, alpha=0.3)

# 6. Cumplimiento de EPP (gráfico gauge-like)
cumplimiento_promedio = datos_seguridad['Cumplimiento_EPP'].mean()
colors = ['red' if x < 80 else 'yellow' if x < 90 else 'green' 
          for x in datos_seguridad['Cumplimiento_EPP']]
sns.barplot(data=datos_seguridad, x='Mes_Str', y='Cumplimiento_EPP', 
            ax=axes[1,2], palette=colors)
axes[1,2].axhline(y=90, color='red', linestyle='--', alpha=0.7, label='Meta: 90%')
axes[1,2].set_title('Cumplimiento de Uso de EPP', fontweight='bold')
axes[1,2].set_xlabel('Mes')
axes[1,2].set_ylabel('Porcentaje (%)')
axes[1,2].tick_params(axis='x', rotation=45)
axes[1,2].legend()

# Ajustar layout
plt.tight_layout()
plt.subplots_adjust(top=0.94)

# Mostrar estadísticas resumidas
print("=== RESUMEN DE INDICADORES DE SEGURIDAD 2024 ===")
print(f"Total de accidentes: {datos_seguridad['Accidentes_Trabajo'].sum()}")
print(f"Promedio mensual de incidentes: {datos_seguridad['Incidentes_Reportados'].mean():.1f}")
print(f"Total horas de capacitación: {datos_seguridad['Horas_Capacitacion'].sum():.0f}")
print(f"Promedio de inspecciones/mes: {datos_seguridad['Inspecciones_Realizadas'].mean():.1f}")
print(f"Tasa promedio de ausentismo: {datos_seguridad['Tasa_Ausentismo'].mean():.2f}%")
print(f"Cumplimiento promedio EPP: {datos_seguridad['Cumplimiento_EPP'].mean():.1f}%")

plt.show()

# Crear también un heatmap de correlación entre indicadores
plt.figure(figsize=(10, 6))
correlacion = datos_seguridad[['Accidentes_Trabajo', 'Incidentes_Reportados', 
                              'Horas_Capacitacion', 'Inspecciones_Realizadas', 
                              'Tasa_Ausentismo', 'Cumplimiento_EPP']].corr()

sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
plt.title('Matriz de Correlación - Indicadores de Seguridad', fontweight='bold', pad=20)
plt.tight_layout()
plt.show()