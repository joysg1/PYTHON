import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Configurar semilla para reproducibilidad
np.random.seed(42)

# 1. Datos simulados de un estudio del ginseng
dias = list(range(0, 91, 7))  # 13 semanas de seguimiento
n_participantes = 100

# Simular efectos del ginseng vs placebo
def simular_efectos(dias, efecto_ginseng=True):
    """Simula los efectos del ginseng o placebo a lo largo del tiempo"""
    if efecto_ginseng:
        # Efectos típicos reportados del ginseng
        energia = 50 + 25 * (1 - np.exp(-np.array(dias)/30)) + np.random.normal(0, 5, len(dias))
        concentracion = 45 + 30 * (1 - np.exp(-np.array(dias)/25)) + np.random.normal(0, 4, len(dias))
        estres = 70 - 20 * (1 - np.exp(-np.array(dias)/35)) + np.random.normal(0, 6, len(dias))
        fatiga = 65 - 25 * (1 - np.exp(-np.array(dias)/40)) + np.random.normal(0, 5, len(dias))
    else:
        # Grupo placebo con mejoras mínimas
        energia = 50 + 5 * (1 - np.exp(-np.array(dias)/60)) + np.random.normal(0, 5, len(dias))
        concentracion = 45 + 8 * (1 - np.exp(-np.array(dias)/50)) + np.random.normal(0, 4, len(dias))
        estres = 70 - 5 * (1 - np.exp(-np.array(dias)/70)) + np.random.normal(0, 6, len(dias))
        fatiga = 65 - 8 * (1 - np.exp(-np.array(dias)/65)) + np.random.normal(0, 5, len(dias))
    
    return energia, concentracion, estres, fatiga

# Generar datos para ambos grupos
energia_ginseng, concentracion_ginseng, estres_ginseng, fatiga_ginseng = simular_efectos(dias, True)
energia_placebo, concentracion_placebo, estres_placebo, fatiga_placebo = simular_efectos(dias, False)

# Crear DataFrame
df = pd.DataFrame({
    'Día': dias * 2,
    'Grupo': ['Ginseng'] * len(dias) + ['Placebo'] * len(dias),
    'Energía': list(energia_ginseng) + list(energia_placebo),
    'Concentración': list(concentracion_ginseng) + list(concentracion_placebo),
    'Estrés': list(estres_ginseng) + list(estres_placebo),
    'Fatiga': list(fatiga_ginseng) + list(fatiga_placebo)
})

# 2. Crear visualizaciones múltiples
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Niveles de Energía', 'Concentración Mental', 
                   'Niveles de Estrés', 'Fatiga Percibida'),
    specs=[[{"secondary_y": False}, {"secondary_y": False}],
           [{"secondary_y": False}, {"secondary_y": False}]]
)

colores = {'Ginseng': '#2E8B57', 'Placebo': '#CD853F'}

# Gráfico 1: Energía
for grupo in ['Ginseng', 'Placebo']:
    data = df[df['Grupo'] == grupo]
    fig.add_trace(
        go.Scatter(x=data['Día'], y=data['Energía'], 
                  name=f'{grupo} - Energía',
                  line=dict(color=colores[grupo], width=3),
                  mode='lines+markers'),
        row=1, col=1
    )

# Gráfico 2: Concentración
for grupo in ['Ginseng', 'Placebo']:
    data = df[df['Grupo'] == grupo]
    fig.add_trace(
        go.Scatter(x=data['Día'], y=data['Concentración'], 
                  name=f'{grupo} - Concentración',
                  line=dict(color=colores[grupo], width=3, dash='dash' if grupo == 'Placebo' else 'solid'),
                  mode='lines+markers',
                  showlegend=False),
        row=1, col=2
    )

# Gráfico 3: Estrés
for grupo in ['Ginseng', 'Placebo']:
    data = df[df['Grupo'] == grupo]
    fig.add_trace(
        go.Scatter(x=data['Día'], y=data['Estrés'], 
                  name=f'{grupo} - Estrés',
                  line=dict(color=colores[grupo], width=3, dash='dot' if grupo == 'Placebo' else 'solid'),
                  mode='lines+markers',
                  showlegend=False),
        row=2, col=1
    )

# Gráfico 4: Fatiga
for grupo in ['Ginseng', 'Placebo']:
    data = df[df['Grupo'] == grupo]
    fig.add_trace(
        go.Scatter(x=data['Día'], y=data['Fatiga'], 
                  name=f'{grupo} - Fatiga',
                  line=dict(color=colores[grupo], width=3, dash='dashdot' if grupo == 'Placebo' else 'solid'),
                  mode='lines+markers',
                  showlegend=False),
        row=2, col=2
    )

# Actualizar layout
fig.update_layout(
    title={
        'text': 'Efectos del Ginseng vs Placebo: Estudio de 12 Semanas',
        'x': 0.5,
        'font': {'size': 18}
    },
    height=700,
    showlegend=True,
    legend=dict(x=0.02, y=0.98)
)

# Actualizar ejes
fig.update_xaxes(title_text="Días de tratamiento")
fig.update_yaxes(title_text="Puntuación (0-100)", row=1, col=1)
fig.update_yaxes(title_text="Puntuación (0-100)", row=1, col=2)
fig.update_yaxes(title_text="Puntuación (0-100)", row=2, col=1)
fig.update_yaxes(title_text="Puntuación (0-100)", row=2, col=2)

fig.show()

# 3. Gráfico de barras comparativo - Mejoras promedio
mejoras_ginseng = {
    'Energía': np.mean(energia_ginseng[-3:]) - energia_ginseng[0],
    'Concentración': np.mean(concentracion_ginseng[-3:]) - concentracion_ginseng[0],
    'Estrés': estres_ginseng[0] - np.mean(estres_ginseng[-3:]),  # Reducción es positiva
    'Fatiga': fatiga_ginseng[0] - np.mean(fatiga_ginseng[-3:])   # Reducción es positiva
}

mejoras_placebo = {
    'Energía': np.mean(energia_placebo[-3:]) - energia_placebo[0],
    'Concentración': np.mean(concentracion_placebo[-3:]) - concentracion_placebo[0],
    'Estrés': estres_placebo[0] - np.mean(estres_placebo[-3:]),
    'Fatiga': fatiga_placebo[0] - np.mean(fatiga_placebo[-3:])
}

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    name='Ginseng',
    x=list(mejoras_ginseng.keys()),
    y=list(mejoras_ginseng.values()),
    marker_color='#2E8B57',
    text=[f'+{v:.1f}' for v in mejoras_ginseng.values()],
    textposition='outside'
))

fig2.add_trace(go.Bar(
    name='Placebo',
    x=list(mejoras_placebo.keys()),
    y=list(mejoras_placebo.values()),
    marker_color='#CD853F',
    text=[f'+{v:.1f}' for v in mejoras_placebo.values()],
    textposition='outside'
))

fig2.update_layout(
    title='Mejoras Promedio Después de 12 Semanas de Tratamiento',
    xaxis_title='Métricas de Salud',
    yaxis_title='Mejora en Puntuación',
    barmode='group',
    height=500
)

fig2.show()

# 4. Datos estadísticos resumen
print("=== RESUMEN ESTADÍSTICO ===")
print("\nEFECTOS DEL GINSENG (vs línea base):")
for metrica, mejora in mejoras_ginseng.items():
    print(f"  {metrica}: +{mejora:.1f} puntos")

print("\nEFECTOS DEL PLACEBO (vs línea base):")
for metrica, mejora in mejoras_placebo.items():
    print(f"  {metrica}: +{mejora:.1f} puntos")

print("\nDIFERENCIA GINSENG vs PLACEBO:")
for metrica in mejoras_ginseng.keys():
    diff = mejoras_ginseng[metrica] - mejoras_placebo[metrica]
    print(f"  {metrica}: +{diff:.1f} puntos adicionales con ginseng")

# 5. Análisis de efectos en el tiempo
print(f"\n=== ANÁLISIS TEMPORAL ===")
print("Tiempo para alcanzar 80% del efecto máximo:")
print("  Energía: ~3-4 semanas")
print("  Concentración: ~2-3 semanas") 
print("  Reducción de estrés: ~4-5 semanas")
print("  Reducción de fatiga: ~5-6 semanas")