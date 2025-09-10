import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Configurar el estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Crear datos de ejemplo para inteligencia emocional
np.random.seed(42)

# Datos de ejemplo: puntuaciones en diferentes competencias de IE
competencias = ['Autoconciencia', 'Autorregulación', 'Motivación', 'Empatía', 'Habilidades Sociales']
puntuaciones_persona1 = [7.5, 6.2, 8.1, 7.8, 6.9]
puntuaciones_persona2 = [6.8, 7.5, 6.3, 8.2, 7.1]
puntuaciones_promedio = [7.0, 7.0, 7.0, 7.5, 7.2]

# Crear figura con múltiples subgráficos
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Análisis de Inteligencia Emocional', fontsize=16, fontweight='bold')

# 1. Gráfico de radar/spider
ax1 = plt.subplot(2, 2, 1, projection='polar')

# Ángulos para cada competencia
angles = np.linspace(0, 2 * np.pi, len(competencias), endpoint=False).tolist()
angles += angles[:1]  # Cerrar el círculo

# Agregar datos para cerrar el círculo
puntuaciones_persona1 += puntuaciones_persona1[:1]
puntuaciones_persona2 += puntuaciones_persona2[:1]
puntuaciones_promedio += puntuaciones_promedio[:1]

# Crear el gráfico de radar
ax1.plot(angles, puntuaciones_persona1, 'o-', linewidth=2, label='Persona 1', alpha=0.8)
ax1.fill(angles, puntuaciones_persona1, alpha=0.25)
ax1.plot(angles, puntuaciones_persona2, 'o-', linewidth=2, label='Persona 2', alpha=0.8)
ax1.fill(angles, puntuaciones_persona2, alpha=0.25)
ax1.plot(angles, puntuaciones_promedio, 'o-', linewidth=2, label='Promedio', alpha=0.8)

# Configurar etiquetas
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(competencias, fontsize=10)
ax1.set_ylim(0, 10)
ax1.set_title('Perfil de Competencias Emocionales', pad=20, fontweight='bold')
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
ax1.grid(True)

# 2. Gráfico de barras comparativo
ax2 = axes[0, 1]
x = np.arange(len(competencias))
width = 0.25

bars1 = ax2.bar(x - width, puntuaciones_persona1[:-1], width, label='Persona 1', alpha=0.8)
bars2 = ax2.bar(x, puntuaciones_persona2[:-1], width, label='Persona 2', alpha=0.8)
bars3 = ax2.bar(x + width, puntuaciones_promedio[:-1], width, label='Promedio', alpha=0.8)

ax2.set_xlabel('Competencias')
ax2.set_ylabel('Puntuación (0-10)')
ax2.set_title('Comparación de Competencias Emocionales')
ax2.set_xticks(x)
ax2.set_xticklabels(competencias, rotation=45, ha='right')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# Agregar valores en las barras
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontsize=8)

# 3. Distribución de puntuaciones por grupos
ax3 = axes[1, 0]

# Generar datos de distribución
np.random.seed(42)
grupo_alto = np.random.normal(8.0, 1.0, 100)
grupo_medio = np.random.normal(6.5, 1.2, 150)
grupo_bajo = np.random.normal(4.5, 1.0, 80)

# Crear histograma
ax3.hist(grupo_alto, bins=15, alpha=0.7, label='Alto (8+ puntos)', density=True)
ax3.hist(grupo_medio, bins=15, alpha=0.7, label='Medio (5-7 puntos)', density=True)
ax3.hist(grupo_bajo, bins=15, alpha=0.7, label='Bajo (<5 puntos)', density=True)

ax3.set_xlabel('Puntuación de Inteligencia Emocional')
ax3.set_ylabel('Densidad')
ax3.set_title('Distribución de Puntuaciones de IE')
ax3.legend()
ax3.grid(alpha=0.3)

# 4. Evolución temporal
ax4 = axes[1, 1]

# Datos de progreso a lo largo del tiempo
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep']
progreso_persona1 = [5.8, 6.1, 6.5, 6.8, 7.0, 7.2, 7.3, 7.5, 7.6]
progreso_persona2 = [6.0, 6.2, 6.3, 6.7, 6.9, 7.0, 7.1, 7.2, 7.3]

ax4.plot(meses, progreso_persona1, marker='o', linewidth=2, label='Persona 1')
ax4.plot(meses, progreso_persona2, marker='s', linewidth=2, label='Persona 2')
ax4.axhline(y=7.0, color='red', linestyle='--', alpha=0.7, label='Meta')

ax4.set_xlabel('Mes')
ax4.set_ylabel('Puntuación Promedio')
ax4.set_title('Evolución de la Inteligencia Emocional')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_ylim(5, 8)

# Ajustar layout
plt.tight_layout()
plt.show()

# Crear un segundo gráfico: Heatmap de correlaciones
plt.figure(figsize=(10, 8))

# Crear datos de correlación entre competencias
np.random.seed(42)
n_personas = 100

# Generar datos correlacionados
data = np.random.multivariate_normal(
    mean=[7, 6.5, 7.2, 7.5, 6.8],
    cov=[[1.2, 0.6, 0.4, 0.5, 0.7],
         [0.6, 1.0, 0.3, 0.4, 0.6],
         [0.4, 0.3, 1.1, 0.6, 0.5],
         [0.5, 0.4, 0.6, 1.0, 0.8],
         [0.7, 0.6, 0.5, 0.8, 1.2]],
    size=n_personas
)

# Crear DataFrame
df = pd.DataFrame(data, columns=competencias)

# Calcular matriz de correlación
correlation_matrix = df.corr()

# Crear heatmap
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', 
            center=0, square=True, fmt='.2f', cbar_kws={'shrink': .8})

plt.title('Correlaciones entre Competencias de Inteligencia Emocional', 
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# Estadísticas descriptivas
print("=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(f"Media general: {df.mean().mean():.2f}")
print(f"Desviación estándar promedio: {df.std().mean():.2f}")
print("\nPor competencia:")
for competencia in competencias:
    print(f"{competencia}: Media = {df[competencia].mean():.2f}, SD = {df[competencia].std():.2f}")

# Identificar fortalezas y áreas de mejora
print("\n=== ANÁLISIS INDIVIDUAL (Persona 1) ===")
puntuaciones_p1 = puntuaciones_persona1[:-1]  # Remover el duplicado del radar
fortalezas = [competencias[i] for i, score in enumerate(puntuaciones_p1) if score > 7.5]
areas_mejora = [competencias[i] for i, score in enumerate(puntuaciones_p1) if score < 6.5]

print(f"Fortalezas: {', '.join(fortalezas) if fortalezas else 'Desarrollo equilibrado'}")
print(f"Áreas de mejora: {', '.join(areas_mejora) if areas_mejora else 'Ninguna crítica'}")
print(f"Puntuación promedio: {np.mean(puntuaciones_p1):.2f}/10")