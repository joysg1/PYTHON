import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configuración para gráficos en español
plt.rcParams['font.size'] = 10
plt.style.use('seaborn-v0_8')

# Datos de los principales APTs según la investigación actualizada
apt_data = {
    'Grupo APT': [
        'Salt Typhoon', 'Lazarus Group', 'APT31', 'APT41', 'Kimsuky',
        'APT29 (Cozy Bear)', 'Star Blizzard', 'APT28 (Fancy Bear)', 
        'Flax Typhoon', 'Volt Typhoon'
    ],
    'País de Origen': [
        'China', 'Corea del Norte', 'China', 'China', 'Corea del Norte',
        'Rusia', 'Rusia', 'Rusia', 'China', 'China'
    ],
    'Nivel de Amenaza': [10, 10, 8, 9, 7, 9, 8, 9, 8, 9],
    'Sector Principal': [
        'Telecomunicaciones', 'Financiero/Cripto', 'Gobierno', 'Dual (Espionaje/Financiero)', 
        'Gobierno/Militar', 'Gobierno/Diplomático', 'Gobierno/NATO', 'Infraestructura Crítica',
        'Gobierno/Academia', 'Infraestructura Crítica'
    ],
    'Actividad 2024': [
        'Infiltración ISPs de EE.UU.', 'Robos de $500M+ en cripto', 'Campaña 14 años vs EE.UU.',
        'Malware DodgeBox/MoonWalk', 'Ataques sin malware', 'Explotación WinRAR/Teams',
        'Phishing con QR WhatsApp', 'Exploit GooseEgg', 'Botnet 260K dispositivos',
        'Exploit FortiOS SSL VPN'
    ],
    'Técnicas TTPs': [
        'Zero-day/Persistencia', 'Social Engineering/Heists', 'Spear-phishing/Tracking',
        'DLL Sideloading/Evasion', 'Credential Harvesting', 'Watering Hole/Phishing',
        'Session Hijacking/QR', 'Print Spooler/Backdoors', 'IoT Botnet/Mirai',
        'Living off the Land'
    ]
}

df = pd.DataFrame(apt_data)

# Crear figura con múltiples subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Principales Advanced Persistent Threats (APTs) - 2024/2025\nAnálisis de Amenazas Cibernéticas Globales', 
             fontsize=16, fontweight='bold', y=0.98)

# 1. Gráfico de barras - Nivel de amenaza por APT
colors = ['#ff4444', '#ff6b6b', '#ffa500', '#ffcc00', '#4ecdc4']
color_map = []
for nivel in df['Nivel de Amenaza']:
    if nivel == 10:
        color_map.append('#ff0000')  # Rojo crítico
    elif nivel == 9:
        color_map.append('#ff4444')  # Rojo alto
    elif nivel == 8:
        color_map.append('#ff8800')  # Naranja
    else:
        color_map.append('#ffaa00')  # Amarillo

sns.barplot(data=df, y='Grupo APT', x='Nivel de Amenaza', ax=ax1, palette=color_map)
ax1.set_title('Nivel de Amenaza por Grupo APT', fontweight='bold', pad=20)
ax1.set_xlabel('Nivel de Amenaza (1-10)')
ax1.set_ylabel('Grupo APT')
ax1.grid(axis='x', alpha=0.3)

# Añadir valores en las barras
for i, v in enumerate(df['Nivel de Amenaza']):
    ax1.text(v + 0.1, i, str(v), va='center', fontweight='bold')

# 2. Distribución por país de origen
country_counts = df['País de Origen'].value_counts()
colors_pie = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4']
wedges, texts, autotexts = ax2.pie(country_counts.values, labels=country_counts.index, 
                                  autopct='%1.0f%%', colors=colors_pie, startangle=90)
ax2.set_title('Distribución por País de Origen', fontweight='bold', pad=20)

# 3. Heatmap de actividad por sector
sector_data = df.groupby(['País de Origen', 'Sector Principal']).size().unstack(fill_value=0)
sns.heatmap(sector_data, annot=True, cmap='Reds', ax=ax3, fmt='d', cbar_kws={'label': 'Número de Grupos'})
ax3.set_title('Matriz de Amenazas: País vs Sector Objetivo', fontweight='bold', pad=20)
ax3.set_xlabel('Sector Principal Objetivo')
ax3.set_ylabel('País de Origen')

# 4. Gráfico de dispersión - Comparación de amenazas
# Crear un índice de sofisticación basado en las técnicas
sophistication_scores = {
    'Zero-day/Persistencia': 10, 'Social Engineering/Heists': 8, 'Spear-phishing/Tracking': 7,
    'DLL Sideloading/Evasion': 9, 'Credential Harvesting': 6, 'Watering Hole/Phishing': 8,
    'Session Hijacking/QR': 9, 'Print Spooler/Backdoors': 8, 'IoT Botnet/Mirai': 7,
    'Living off the Land': 9
}

df['Sofisticación'] = df['Técnicas TTPs'].map(sophistication_scores)

# Colores por país
country_colors = {'China': '#ff4444', 'Rusia': '#4444ff', 'Corea del Norte': '#44ff44'}
point_colors = [country_colors[country] for country in df['País de Origen']]

scatter = ax4.scatter(df['Sofisticación'], df['Nivel de Amenaza'], 
                     c=point_colors, s=150, alpha=0.7, edgecolors='black')

# Añadir etiquetas
for i, txt in enumerate(df['Grupo APT']):
    ax4.annotate(txt, (df['Sofisticación'].iloc[i], df['Nivel de Amenaza'].iloc[i]), 
                xytext=(5, 5), textcoords='offset points', fontsize=8, ha='left')

ax4.set_xlabel('Nivel de Sofisticación Técnica')
ax4.set_ylabel('Nivel de Amenaza')
ax4.set_title('Sofisticación vs Nivel de Amenaza', fontweight='bold', pad=20)
ax4.grid(True, alpha=0.3)

# Leyenda para el scatter
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, 
                             markersize=10, label=country) 
                  for country, color in country_colors.items()]
ax4.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
plt.subplots_adjust(top=0.93)

# Tabla resumen en la parte inferior
fig2, ax5 = plt.subplots(1, 1, figsize=(16, 8))
ax5.axis('tight')
ax5.axis('off')

# Crear tabla con información clave
table_data = []
for i, row in df.iterrows():
    table_data.append([
        row['Grupo APT'],
        row['País de Origen'], 
        f"{row['Nivel de Amenaza']}/10",
        row['Sector Principal'],
        row['Actividad 2024'][:50] + "..." if len(row['Actividad 2024']) > 50 else row['Actividad 2024']
    ])

table = ax5.table(cellText=table_data,
                 colLabels=['Grupo APT', 'País', 'Nivel', 'Sector Objetivo', 'Actividad Principal 2024'],
                 cellLoc='left',
                 loc='center',
                 colWidths=[0.15, 0.12, 0.08, 0.20, 0.45])

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)

# Colorear las filas por nivel de amenaza
for i in range(1, len(table_data) + 1):
    nivel = int(table_data[i-1][2].split('/')[0])
    if nivel == 10:
        color = '#ffcccc'
    elif nivel == 9:
        color = '#ffe6cc'
    elif nivel == 8:
        color = '#fff2cc'
    else:
        color = '#f0f0f0'
    
    for j in range(5):
        table[(i, j)].set_facecolor(color)

# Header styling
for j in range(5):
    table[(0, j)].set_facecolor('#2c3e50')
    table[(0, j)].set_text_props(weight='bold', color='white')

ax5.set_title('Resumen Detallado de Principales APTs - Actualizado 2024/2025', 
              fontsize=14, fontweight='bold', pad=20)

# Agregar nota informativa
note_text = """
Fuente: SOCRadar Cyber Intelligence, ESET Research, CISA, FBI
Nota: Los niveles de amenaza se basan en impacto demostrado, sofisticación técnica y alcance geográfico.
Datos actualizados a septiembre 2025 con información de incidentes confirmados en 2024.
"""
plt.figtext(0.02, 0.02, note_text, fontsize=9, style='italic')

plt.tight_layout()
plt.show()

# Estadísticas adicionales
print("\n=== ESTADÍSTICAS DE APTS 2024-2025 ===")
print(f"Total de APTs analizados: {len(df)}")
print(f"Nivel promedio de amenaza: {df['Nivel de Amenaza'].mean():.1f}/10")
print(f"País con más grupos APT: {df['País de Origen'].value_counts().index[0]} ({df['País de Origen'].value_counts().iloc[0]} grupos)")
print("\nDistribución por nivel de amenaza:")
for nivel in sorted(df['Nivel de Amenaza'].unique(), reverse=True):
    count = (df['Nivel de Amenaza'] == nivel).sum()
    grupos = df[df['Nivel de Amenaza'] == nivel]['Grupo APT'].tolist()
    print(f"  Nivel {nivel}: {count} grupo(s) - {', '.join(grupos)}")