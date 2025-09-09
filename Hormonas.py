import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Datos
hormonas_data = {
    'Hormona': ['Oxitocina', 'Dopamina', 'Serotonina', 'Testosterona', 'Estrógeno', 
                'Noradrenalina', 'Vasopresina', 'Cortisol'],
    'Nivel_Hombres': [65, 85, 70, 90, 30, 80, 75, 45],
    'Nivel_Mujeres': [80, 75, 85, 25, 85, 85, 60, 55],
    'Impacto_Atraccion': [95, 90, 75, 80, 85, 85, 70, -30],
    'Fase_Relacion': ['Apego', 'Atracción', 'Bienestar', 'Deseo', 'Atracción', 
                      'Pasión', 'Compromiso', 'Estrés'],
    'Descripcion': [
        'Hormona del vínculo y confianza',
        'Neurotransmisor del placer y recompensa', 
        'Regula el estado de ánimo',
        'Hormona del deseo sexual masculino',
        'Hormona femenina, regula ciclos',
        'Excitación y energía romántica',
        'Fidelidad y compromiso',
        'Hormona del estrés, inhibe atracción'
    ]
}

df = pd.DataFrame(hormonas_data)

# Crear subplots sin el radar (que se hará por separado)
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Niveles por Género', 'Impacto en Atracción', 
                    'Comparación Directa', ' '),  # Eliminamos título de radar aquí
    specs=[[{"secondary_y": False}, {"secondary_y": False}],
           [{"secondary_y": False}, {"secondary_y": False}]]
)

# 1. Barras agrupadas
fig.add_trace(
    go.Bar(name='Hombres', x=df['Hormona'], y=df['Nivel_Hombres'],
           marker_color='lightblue', text=df['Nivel_Hombres'], textposition='outside'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(name='Mujeres', x=df['Hormona'], y=df['Nivel_Mujeres'],
           marker_color='lightcoral', text=df['Nivel_Mujeres'], textposition='outside'),
    row=1, col=1
)

# 2. Impacto en atracción
colors = ['red' if x < 0 else 'green' for x in df['Impacto_Atraccion']]
fig.add_trace(
    go.Bar(x=df['Hormona'], y=df['Impacto_Atraccion'], marker_color=colors,
           name='Impacto', text=df['Impacto_Atraccion'], textposition='outside'),
    row=1, col=2
)

# 3. Comparación directa (scatter)
fig.add_trace(
    go.Scatter(x=df['Nivel_Hombres'], y=df['Nivel_Mujeres'], mode='markers+text',
               text=df['Hormona'], textposition='top center', name='Hormonas',
               marker=dict(size=abs(df['Impacto_Atraccion'])/3,
                           color=df['Impacto_Atraccion'],
                           colorscale='RdYlGn', showscale=True,
                           colorbar=dict(title="Impacto"))),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=[0, 100], y=[0, 100], mode='lines',
               line=dict(dash='dash', color='gray'), name='Igualdad H=M'),
    row=2, col=1
)

# Layout
fig.update_layout(
    title={'text': 'Análisis Hormonal en la Atracción Humana', 'x': 0.5, 'font': {'size': 20}},
    height=800,
    showlegend=True,
    template='plotly_white'
)

# Ejes
fig.update_xaxes(tickangle=45, row=1, col=1)
fig.update_xaxes(tickangle=45, row=1, col=2)
fig.update_xaxes(title_text="Nivel en Hombres", row=2, col=1)
fig.update_yaxes(title_text="Nivel en Mujeres", row=2, col=1)

fig.show()

# --- Nuevo gráfico separado: Radar por fase de relación ---
valores_fase = df.groupby('Fase_Relacion')['Impacto_Atraccion'].mean()

fig3 = go.Figure()
fig3.add_trace(
    go.Scatterpolar(
        r=list(valores_fase.values),
        theta=list(valores_fase.index),
        fill='toself',
        name='Fases Relación',
        line_color='purple'
    )
)

fig3.update_layout(
    title="Impacto Promedio de Hormonas por Fase de la Relación",
    polar=dict(
        radialaxis=dict(visible=True, range=[min(valores_fase)-10, max(valores_fase)+10])
    ),
    showlegend=False,
    template='plotly_white',
    height=500
)
fig3.show()

# --- Timeline hormonal (fig2 ya estaba bien) ---
tiempo = np.linspace(0, 30, 100)
oxitocina = 50 + 20 * np.sin(tiempo/5) + np.random.normal(0, 3, 100)
dopamina = 60 + 25 * np.exp(-tiempo/10) * np.sin(tiempo/2) + np.random.normal(0, 5, 100)
serotonina = 65 + 15 * np.cos(tiempo/7) + np.random.normal(0, 4, 100)
noradrenalina = 55 + 30 * np.exp(-tiempo/8) + np.random.normal(0, 6, 100)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=tiempo, y=oxitocina, name='Oxitocina', line=dict(color='blue', width=3)))
fig2.add_trace(go.Scatter(x=tiempo, y=dopamina, name='Dopamina', line=dict(color='red', width=3)))
fig2.add_trace(go.Scatter(x=tiempo, y=serotonina, name='Serotonina', line=dict(color='green', width=3)))
fig2.add_trace(go.Scatter(x=tiempo, y=noradrenalina, name='Noradrenalina', line=dict(color='orange', width=3)))

fig2.add_vrect(x0=0, x1=7, fillcolor="lightgray", opacity=0.3,
               annotation_text="Atracción Inicial", annotation_position="top left")
fig2.add_vrect(x0=7, x1=15, fillcolor="lightblue", opacity=0.3,
               annotation_text="Enamoramiento", annotation_position="top left")
fig2.add_vrect(x0=15, x1=30, fillcolor="lightgreen", opacity=0.3,
               annotation_text="Apego", annotation_position="top left")

fig2.update_layout(
    title='Evolución Hormonal Durante el Proceso de Atracción',
    xaxis_title='Días desde el primer encuentro',
    yaxis_title='Nivel hormonal (unidades arbitrarias)',
    hovermode='x unified',
    template='plotly_white',
    height=500
)
fig2.show()

# --- Imprimir información ---
print("\n=== INFORMACIÓN SOBRE LAS HORMONAS EN LA ATRACCIÓN ===\n")
for i, row in df.iterrows():
    print(f"🧬 {row['Hormona']}: {row['Descripcion']}")
    print(f"   Nivel promedio - Hombres: {row['Nivel_Hombres']}% | Mujeres: {row['Nivel_Mujeres']}%")
    print(f"   Impacto en atracción: {row['Impacto_Atraccion']}%")
    print(f"   Fase principal: {row['Fase_Relacion']}\n")

print("📊 Análisis:")
print("• Las mujeres tienen niveles más altos de oxitocina y serotonina")
print("• Los hombres tienen niveles más altos de testosterona")
print("• La dopamina y noradrenalina son cruciales en la atracción inicial")
print("• El cortisol (estrés) puede inhibir la atracción")
print("• La vasopresina está más asociada con el compromiso a largo plazo")
