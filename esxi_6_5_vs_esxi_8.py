import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

# Categorías de comparación enfocadas en seguridad y rendimiento
categorias = [
    'Secure Boot',
    'TPM 2.0 Support', 
    'Encryption Features',
    'vTPM (Virtual TPM)',
    'DPU Support',
    'Network Security',
    'VM Hardware Version',
    'Performance Baseline',
    'Security Patches',
    'Identity Federation',
    'Trust Authority',
    'Hardware Acceleration'
]

# Puntuaciones comparativas (1-10) basadas en características técnicas
# ESXi 6.5 capabilities
esxi_6_5_scores = [
    2,  # Secure Boot - Soporte muy limitado
    3,  # TPM 2.0 Support - Soporte básico introducido después
    4,  # Encryption Features - vSAN encryption básico
    0,  # vTPM - No disponible en 6.5
    0,  # DPU Support - No disponible
    5,  # Network Security - Funcionalidad básica
    6,  # VM Hardware Version - Versión 13 máximo
    6,  # Performance Baseline - Base sólida
    4,  # Security Patches - EOL, sin patches recientes
    0,  # Identity Federation - No disponible
    0,  # Trust Authority - No disponible
    5   # Hardware Acceleration - Limitado
]

# ESXi 8.0 capabilities
esxi_8_0_scores = [
    9,  # Secure Boot - Soporte completo y robusto
    9,  # TPM 2.0 Support - Soporte completo y mejorado
    9,  # Encryption Features - Encryption comprehensivo
    10, # vTPM - Soporte completo para Virtual TPM
    9,  # DPU Support - Soporte nativo para DPUs
    9,  # Network Security - NSX distributed firewall en DPUs
    10, # VM Hardware Version - Versión 20, características avanzadas
    8,  # Performance Baseline - Mejoras significativas
    10, # Security Patches - Actualizaciones activas
    8,  # Identity Federation - Disponible y maduro
    8,  # Trust Authority - Disponible
    9   # Hardware Acceleration - Amplio soporte
]

# Calcular mejoras porcentuales
mejoras_porcentuales = []
for i, (score_65, score_80) in enumerate(zip(esxi_6_5_scores, esxi_8_0_scores)):
    if score_65 == 0:
        mejora = 1000 if score_80 > 0 else 0  # Característica nueva
    else:
        mejora = ((score_80 - score_65) / score_65) * 100
    mejoras_porcentuales.append(mejora)

# Crear DataFrame
df = pd.DataFrame({
    'Categoría': categorias,
    'ESXi_6.5': esxi_6_5_scores,
    'ESXi_8.0': esxi_8_0_scores,
    'Mejora_%': mejoras_porcentuales
})

# Crear figura principal con áreas bajo la curva
fig = go.Figure()

# Índices para el eje X
x_indices = list(range(len(categorias)))

# Añadir línea base en y=0 para crear áreas
fig.add_trace(go.Scatter(
    x=x_indices,
    y=[0] * len(categorias),
    mode='lines',
    line=dict(color='rgba(0,0,0,0)'),
    showlegend=False,
    hoverinfo='skip'
))

# Área para ESXi 8.0 (superior)
fig.add_trace(go.Scatter(
    x=x_indices,
    y=esxi_8_0_scores,
    mode='lines+markers',
    name='ESXi 8.0 (Actual)',
    line=dict(color='#00AA44', width=4),
    marker=dict(size=10, color='#00AA44', symbol='diamond'),
    fill='tonexty',
    fillcolor='rgba(0, 170, 68, 0.4)',
    hovertemplate='<b>ESXi 8.0</b><br>%{text}: %{y}/10<extra></extra>',
    text=categorias
))

# Área para ESXi 6.5 (inferior)  
fig.add_trace(go.Scatter(
    x=x_indices,
    y=esxi_6_5_scores,
    mode='lines+markers',
    name='ESXi 6.5 (Legacy)',
    line=dict(color='#FF4444', width=3),
    marker=dict(size=8, color='#FF4444', symbol='circle'),
    fill='tonexty',
    fillcolor='rgba(255, 68, 68, 0.3)',
    hovertemplate='<b>ESXi 6.5</b><br>%{text}: %{y}/10<extra></extra>',
    text=categorias
))

# Personalizar el diseño
fig.update_layout(
    title={
        'text': 'ESXi 6.5 vs ESXi 8.0: Evolución en Rendimiento y Seguridad<br><sub>Área bajo la curva = Capacidades acumuladas • Énfasis en características de seguridad</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    xaxis_title='Características de Seguridad y Rendimiento',
    yaxis_title='Puntuación de Capacidad (0-10)',
    template='plotly_white',
    width=1400,
    height=700,
    hovermode='x unified',
    font=dict(family="Arial, sans-serif", size=12),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=1.02,
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="rgba(0,0,0,0.2)",
        borderwidth=1
    )
)

# Personalizar ejes
fig.update_xaxes(
    tickmode='array',
    tickvals=x_indices,
    ticktext=categorias,
    tickangle=-45,
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray'
)

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    range=[0, 11],
    dtick=1
)

# Añadir anotaciones para características clave de seguridad
fig.add_annotation(
    x=3, y=10,
    text="🔒 vTPM Completo<br>Nuevo en 8.0",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#00AA44",
    ax=0, ay=-50,
    bgcolor="white",
    bordercolor="#00AA44",
    borderwidth=2,
    font=dict(size=11)
)

fig.add_annotation(
    x=4, y=9,
    text="🚀 DPU Support<br>Aceleración Hardware",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#00AA44",
    ax=30, ay=-40,
    bgcolor="white",
    bordercolor="#00AA44",
    borderwidth=2,
    font=dict(size=11)
)

fig.add_annotation(
    x=0, y=9,
    text="🛡️ Secure Boot<br>Mejorado significativamente",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#00AA44",
    ax=-30, ay=-40,
    bgcolor="white",
    bordercolor="#00AA44",
    borderwidth=2,
    font=dict(size=11)
)

fig.show()

# Crear gráfico de mejoras porcentuales
fig2 = go.Figure()

# Colores basados en el nivel de mejora
colores_mejora = []
for mejora in mejoras_porcentuales:
    if mejora >= 1000:
        colores_mejora.append('#006600')  # Verde oscuro - característica nueva
    elif mejora >= 100:
        colores_mejora.append('#00AA44')  # Verde - gran mejora
    elif mejora >= 50:
        colores_mejora.append('#88DD44')  # Verde claro - mejora moderada
    elif mejora >= 0:
        colores_mejora.append('#FFAA44')  # Naranja - mejora pequeña
    else:
        colores_mejora.append('#FF4444')  # Rojo - no hay mejora

fig2.add_trace(go.Bar(
    x=categorias,
    y=mejoras_porcentuales,
    marker_color=colores_mejora,
    text=[f'+{int(mejora)}%' if mejora < 1000 else 'NUEVO' for mejora in mejoras_porcentuales],
    textposition='outside',
    name='Mejora ESXi 8.0 vs 6.5'
))

fig2.update_layout(
    title='Mejoras Porcentuales: ESXi 8.0 vs ESXi 6.5<br><sub>Enfoque en características de seguridad y rendimiento</sub>',
    xaxis_title='Características',
    yaxis_title='Mejora Porcentual (%)',
    template='plotly_white',
    width=1400,
    height=600,
    xaxis_tickangle=-45
)

fig2.show()

# Crear gráfico de área acumulada para mostrar la brecha de seguridad total
fig3 = go.Figure()

# Calcular áreas acumuladas
area_65 = np.trapz(esxi_6_5_scores, x_indices)
area_80 = np.trapz(esxi_8_0_scores, x_indices)

fig3.add_trace(go.Bar(
    x=['ESXi 6.5<br>(Legacy)', 'ESXi 8.0<br>(Current)'],
    y=[area_65, area_80],
    marker_color=['#FF4444', '#00AA44'],
    text=[f'{area_65:.0f}<br>Área Total', f'{area_80:.0f}<br>Área Total'],
    textposition='auto',
    width=0.6
))

# Añadir la diferencia como anotación
diferencia_area = area_80 - area_65
fig3.add_annotation(
    x=0.5, y=max(area_65, area_80) * 0.8,
    text=f'🔺 Brecha de Seguridad<br>+{diferencia_area:.0f} puntos<br>({((area_80/area_65)-1)*100:.0f}% mejor)',
    showarrow=False,
    bgcolor="rgba(255,255,255,0.9)",
    bordercolor="black",
    borderwidth=2,
    font=dict(size=14, color='black')
)

fig3.update_layout(
    title='Área Total Bajo la Curva: Capacidades de Seguridad y Rendimiento',
    yaxis_title='Área Total (Puntos Acumulados)',
    template='plotly_white',
    width=800,
    height=600
)

fig3.show()

# Análisis detallado
print("=" * 90)
print("ANÁLISIS COMPARATIVO: ESXi 6.5 vs ESXi 8.0 - ENFOQUE EN SEGURIDAD")
print("=" * 90)
print(f"{'Característica':<25} {'ESXi 6.5':<10} {'ESXi 8.0':<10} {'Mejora':<12} {'Impacto Seguridad'}")
print("-" * 90)

impactos_seguridad = [
    'CRÍTICO - Boot integrity',
    'CRÍTICO - Hardware security', 
    'CRÍTICO - Data protection',
    'CRÍTICO - VM-level security',
    'ALTO - Network acceleration',
    'ALTO - East-West traffic',
    'MEDIO - VM capabilities',
    'MEDIO - General performance',
    'CRÍTICO - Vulnerability mgmt',
    'ALTO - Access management',
    'ALTO - Infrastructure trust',
    'MEDIO - Performance boost'
]

for i, (cat, score65, score80, mejora, impacto) in enumerate(zip(categorias, esxi_6_5_scores, esxi_8_0_scores, mejoras_porcentuales, impactos_seguridad)):
    mejora_str = f"+{mejora:.0f}%" if mejora < 1000 else "NUEVO"
    print(f"{cat:<25} {score65:<10} {score80:<10} {mejora_str:<12} {impacto}")

print("=" * 90)
print("📊 RESUMEN EJECUTIVO DE SEGURIDAD:")
print(f"• Capacidad total ESXi 6.5: {sum(esxi_6_5_scores)}/120 ({(sum(esxi_6_5_scores)/120)*100:.1f}%)")
print(f"• Capacidad total ESXi 8.0: {sum(esxi_8_0_scores)}/120 ({(sum(esxi_8_0_scores)/120)*100:.1f}%)")
print(f"• Mejora general: {((sum(esxi_8_0_scores)/sum(esxi_6_5_scores))-1)*100:.0f}%")
print()
print("🔒 CARACTERÍSTICAS DE SEGURIDAD NUEVAS EN ESXi 8.0:")
nuevas_caracteristicas = [cat for i, cat in enumerate(categorias) if esxi_6_5_scores[i] == 0 and esxi_8_0_scores[i] > 0]
for caracteristica in nuevas_caracteristicas:
    print(f"  • {caracteristica}")

print()
print("⚠️ RECOMENDACIONES:")
print("• ESXi 6.5 alcanza EOL - Sin parches de seguridad")
print("• Migración a ESXi 8.0 crítica para seguridad empresarial")
print("• vTPM esencial para Windows 11 y aplicaciones modernas")
print("• DPU support mejora significativamente rendimiento de red")
print("=" * 90)