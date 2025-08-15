import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Definir categorías de resiliencia para comparar
categorias = [
    'Journaling',
    'Metadata Checksums', 
    'Corruption Recovery',
    'Power Failure Protection',
    'Bad Sector Handling',
    'Redundancy Features',
    'Self-Healing',
    'Error Detection',
    'Filesystem Check Speed',
    'Data Integrity'
]

# Puntuaciones basadas en características técnicas (1-10)
# Basado en investigación de características de ambos sistemas de archivos

# NTFS scores (Microsoft NTFS features)
ntfs_scores = [
    9,  # Journaling - NTFS tiene journaling completo ($LogFile)
    6,  # Metadata Checksums - Limitado comparado con ext4
    8,  # Corruption Recovery - CHKDSK es robusto
    8,  # Power Failure Protection - Buen manejo con journaling
    9,  # Bad Sector Handling - Excelente con cluster remapping
    7,  # Redundancy Features - MFT backup, etc.
    5,  # Self-Healing - Limitado
    7,  # Error Detection - Bueno pero no extensivo
    6,  # Filesystem Check Speed - CHKDSK puede ser lento
    7   # Data Integrity - Buena pero no checksums completos
]

# EXT4 scores (Linux ext4 features) 
ext4_scores = [
    9,  # Journaling - Journaling completo (metadata y data opcional)
    9,  # Metadata Checksums - Checksums CRC32C extensivos
    7,  # Corruption Recovery - fsck robusto pero manual
    8,  # Power Failure Protection - Muy bueno con barriers
    6,  # Bad Sector Handling - Básico, depende de hardware
    8,  # Redundancy Features - Múltiples copias de metadata crítica
    6,  # Self-Healing - Limitado, principalmente detección
    9,  # Error Detection - Checksums extensivos
    8,  # Filesystem Check Speed - fsck generalmente más rápido
    8   # Data Integrity - Checksums comprensivos
]

# Crear el DataFrame
df = pd.DataFrame({
    'Categoría': categorias,
    'NTFS': ntfs_scores,
    'EXT4': ext4_scores
})

# Crear el gráfico radar
fig = go.Figure()

# Añadir NTFS
fig.add_trace(go.Scatterpolar(
    r=ntfs_scores + [ntfs_scores[0]],  # Cerrar el polígono
    theta=categorias + [categorias[0]],
    fill='tonext',
    fillcolor='rgba(255, 99, 71, 0.3)',
    line=dict(color='#FF6347', width=3),
    marker=dict(size=8, color='#FF6347'),
    name='NTFS (Windows)',
    hovertemplate='<b>NTFS</b><br>%{theta}: %{r}/10<extra></extra>'
))

# Añadir EXT4
fig.add_trace(go.Scatterpolar(
    r=ext4_scores + [ext4_scores[0]],  # Cerrar el polígono
    theta=categorias + [categorias[0]],
    fill='tonext',
    fillcolor='rgba(50, 205, 50, 0.3)',
    line=dict(color='#32CD32', width=3),
    marker=dict(size=8, color='#32CD32'),
    name='EXT4 (Linux)',
    hovertemplate='<b>EXT4</b><br>%{theta}: %{r}/10<extra></extra>'
))

# Personalizar el diseño
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10],
            tickmode='linear',
            tick0=0,
            dtick=2,
            tickfont=dict(size=12),
            gridcolor='lightgray',
            gridwidth=1
        ),
        angularaxis=dict(
            tickfont=dict(size=11),
            rotation=90,
            direction="clockwise"
        ),
        bgcolor='white'
    ),
    title={
        'text': 'Comparación de Resiliencia: NTFS vs EXT4<br><sub>Puntuación por categoría de resistencia del sistema de archivos (1-10)</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18}
    },
    width=900,
    height=700,
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.1,
        xanchor="center",
        x=0.5,
        font=dict(size=14)
    ),
    font=dict(family="Arial, sans-serif", size=12),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Mostrar el gráfico
fig.show()

# Crear gráfico de barras comparativo
fig2 = go.Figure()

# Calcular diferencias
diferencias = [ext4 - ntfs for ext4, ntfs in zip(ext4_scores, ntfs_scores)]
colores = ['green' if diff > 0 else 'red' if diff < 0 else 'gray' for diff in diferencias]

fig2.add_trace(go.Bar(
    x=categorias,
    y=diferencias,
    marker_color=colores,
    text=[f'+{diff}' if diff > 0 else f'{diff}' if diff < 0 else '0' for diff in diferencias],
    textposition='outside',
    name='Ventaja EXT4 vs NTFS'
))

fig2.update_layout(
    title='Diferencias de Puntuación: EXT4 vs NTFS<br><sub>Valores positivos = ventaja EXT4, negativos = ventaja NTFS</sub>',
    xaxis_title='Características de Resiliencia',
    yaxis_title='Diferencia de Puntuación',
    template='plotly_white',
    width=1100,
    height=600,
    xaxis_tickangle=-45,
    yaxis=dict(range=[-4, 4])
)

# Añadir línea de referencia en y=0
fig2.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.7)

fig2.show()

# Análisis detallado
print("=" * 80)
print("ANÁLISIS COMPARATIVO DE RESILIENCIA: NTFS vs EXT4")
print("=" * 80)
print(f"{'Característica':<25} {'NTFS':<6} {'EXT4':<6} {'Ventaja':<15} {'Observaciones'}")
print("-" * 80)

observaciones = [
    "Ambos excelentes",
    "EXT4 superior con CRC32C",
    "NTFS ligeramente mejor",
    "Muy similares",
    "NTFS superior con remapping",
    "EXT4 mejor redundancia",
    "Ambos limitados",
    "EXT4 detección superior",
    "EXT4 generalmente más rápido",
    "EXT4 ligeramente mejor"
]

for i, (cat, ntfs, ext4, obs) in enumerate(zip(categorias, ntfs_scores, ext4_scores, observaciones)):
    if ext4 > ntfs:
        ventaja = "EXT4"
    elif ntfs > ext4:
        ventaja = "NTFS"
    else:
        ventaja = "Empate"
    
    print(f"{cat:<25} {ntfs:<6} {ext4:<6} {ventaja:<15} {obs}")

print("=" * 80)

# Calcular puntuaciones totales
total_ntfs = sum(ntfs_scores)
total_ext4 = sum(ext4_scores)

print("📊 RESUMEN EJECUTIVO:")
print(f"• Puntuación total NTFS: {total_ntfs}/100")
print(f"• Puntuación total EXT4: {total_ext4}/100")
print(f"• Diferencia: {abs(total_ext4 - total_ntfs)} puntos a favor de {'EXT4' if total_ext4 > total_ntfs else 'NTFS'}")
print()
print("🔍 FORTALEZAS CLAVE:")
print("NTFS:")
print("  - Excelente manejo de sectores defectuosos")
print("  - Recuperación robusta con CHKDSK")
print("  - Journaling maduro y estable")
print()
print("EXT4:")
print("  - Checksums extensivos de metadata")
print("  - Detección de errores superior")
print("  - Verificación más rápida del filesystem")
print("=" * 80)

# Crear gráfico de puntuación total
fig3 = go.Figure()

fig3.add_trace(go.Bar(
    x=['NTFS', 'EXT4'],
    y=[total_ntfs, total_ext4],
    marker_color=['#FF6347', '#32CD32'],
    text=[f'{total_ntfs}/100', f'{total_ext4}/100'],
    textposition='outside',
    width=0.6
))

fig3.update_layout(
    title='Puntuación Total de Resiliencia',
    xaxis_title='Sistema de Archivos',
    yaxis_title='Puntuación Total (sobre 100)',
    template='plotly_white',
    width=600,
    height=500,
    yaxis=dict(range=[0, 100])
)

fig3.show()