import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# Datos de avances médicos importantes tras la Primera Guerra Mundial
avances_medicina = {
    'Año': [1920, 1922, 1924, 1925, 1928, 1930, 1932, 1935, 1938, 1940, 1941, 1942, 1945, 1948, 1950],
    'Descubrimiento': [
        'Insulina descubierta',
        'Vitamina D sintetizada',
        'Primeras transfusiones de sangre organizadas',
        'Desarrollo de prótesis modernas',
        'Penicilina descubierta',
        'Sulfonamidas desarrolladas',
        'Primeros microscopios electrónicos',
        'Cortisona sintetizada',
        'Técnicas de neurocirugía avanzada',
        'Factor Rh descubierto',
        'Penicilina producida en masa',
        'Primeros antibióticos de amplio espectro',
        'Fluor añadido al agua potable',
        'OMS fundada',
        'Primeros trasplantes de riñón'
    ],
    'Categoría': [
        'Endocrinología', 'Nutrición', 'Hematología', 'Cirugía reconstructiva',
        'Microbiología', 'Farmacología', 'Diagnóstico', 'Endocrinología',
        'Neurocirugía', 'Hematología', 'Microbiología', 'Farmacología',
        'Salud pública', 'Organización sanitaria', 'Trasplantes'
    ],
    'Impacto': [9, 7, 8, 6, 10, 8, 7, 6, 7, 7, 10, 8, 8, 9, 9],
    'Vidas_salvadas_estimadas': [1000000, 500000, 200000, 100000, 5000000, 1000000, 
                                300000, 200000, 150000, 100000, 8000000, 2000000,
                                3000000, 2000000, 50000]
}

# Crear DataFrame
df = pd.DataFrame(avances_medicina)

# Definir colores por categoría
colores_categoria = {
    'Endocrinología': '#FF6B6B',
    'Nutrición': '#4ECDC4',
    'Hematología': '#45B7D1',
    'Cirugía reconstructiva': '#96CEB4',
    'Microbiología': '#FFEAA7',
    'Farmacología': '#DDA0DD',
    'Diagnóstico': '#98D8C8',
    'Neurocirugía': '#F7DC6F',
    'Salud pública': '#BB8FCE',
    'Organización sanitaria': '#85C1E9',
    'Trasplantes': '#F8C471'
}

# Crear subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Línea de tiempo de avances médicos', 
                   'Impacto por categoría médica',
                   'Vidas salvadas por descubrimiento',
                   'Evolución acumulativa del impacto'),
    specs=[[{"secondary_y": False}, {"type": "bar"}],
           [{"type": "scatter"}, {"secondary_y": False}]]
)

# Gráfico 1: Línea de tiempo con scatter plot
fig.add_trace(
    go.Scatter(
        x=df['Año'],
        y=df['Impacto'],
        mode='markers+lines',
        marker=dict(
            size=12,
            color=[colores_categoria[cat] for cat in df['Categoría']],
            line=dict(width=2, color='white')
        ),
        text=df['Descubrimiento'],
        hovertemplate='<b>%{text}</b><br>Año: %{x}<br>Impacto: %{y}<extra></extra>',
        line=dict(width=3, color='rgba(100, 100, 100, 0.3)'),
        name='Avances médicos'
    ),
    row=1, col=1
)

# Gráfico 2: Impacto por categoría
categoria_impacto = df.groupby('Categoría')['Impacto'].mean().sort_values(ascending=True)
fig.add_trace(
    go.Bar(
        x=categoria_impacto.values,
        y=categoria_impacto.index,
        orientation='h',
        marker_color=[colores_categoria[cat] for cat in categoria_impacto.index],
        text=[f'{val:.1f}' for val in categoria_impacto.values],
        textposition='inside',
        name='Impacto promedio'
    ),
    row=1, col=2
)

# Gráfico 3: Vidas salvadas (escala logarítmica)
fig.add_trace(
    go.Scatter(
        x=df['Año'],
        y=df['Vidas_salvadas_estimadas'],
        mode='markers',
        marker=dict(
            size=[val/500000 + 8 for val in df['Vidas_salvadas_estimadas']],
            color=[colores_categoria[cat] for cat in df['Categoría']],
            opacity=0.7,
            line=dict(width=2, color='white')
        ),
        text=df['Descubrimiento'],
        hovertemplate='<b>%{text}</b><br>Año: %{x}<br>Vidas salvadas: %{y:,.0f}<extra></extra>',
        name='Vidas salvadas'
    ),
    row=2, col=1
)

# Gráfico 4: Evolución acumulativa del impacto
impacto_acumulativo = df['Impacto'].cumsum()
fig.add_trace(
    go.Scatter(
        x=df['Año'],
        y=impacto_acumulativo,
        mode='lines+markers',
        fill='tonexty',
        fillcolor='rgba(74, 144, 226, 0.3)',
        line=dict(width=4, color='#4A90E2'),
        marker=dict(size=8, color='#4A90E2'),
        name='Impacto acumulativo'
    ),
    row=2, col=2
)

# Actualizar layouts
fig.update_xaxes(title_text="Año", row=1, col=1)
fig.update_yaxes(title_text="Nivel de Impacto", row=1, col=1)

fig.update_xaxes(title_text="Impacto Promedio", row=1, col=2)
fig.update_yaxes(title_text="Categoría Médica", row=1, col=2)

fig.update_xaxes(title_text="Año", row=2, col=1)
fig.update_yaxes(title_text="Vidas Salvadas (log)", type="log", row=2, col=1)

fig.update_xaxes(title_text="Año", row=2, col=2)
fig.update_yaxes(title_text="Impacto Acumulativo", row=2, col=2)

# Layout general
fig.update_layout(
    height=800,
    title={
        'text': 'Avances de la Medicina tras la Primera Guerra Mundial (1920-1950)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': '#2C3E50'}
    },
    showlegend=False,
    plot_bgcolor='white',
    paper_bgcolor='#F8F9FA'
)

# Mostrar la figura
fig.show()

# Crear una segunda visualización: Gráfico de barras animado por década
fig2 = go.Figure()

# Datos por década
decadas = ['1920-1929', '1930-1939', '1940-1950']
avances_por_decada = [
    df[(df['Año'] >= 1920) & (df['Año'] < 1930)]['Descubrimiento'].count(),
    df[(df['Año'] >= 1930) & (df['Año'] < 1940)]['Descubrimiento'].count(),
    df[(df['Año'] >= 1940) & (df['Año'] <= 1950)]['Descubrimiento'].count()
]

impacto_por_decada = [
    df[(df['Año'] >= 1920) & (df['Año'] < 1930)]['Impacto'].sum(),
    df[(df['Año'] >= 1930) & (df['Año'] < 1940)]['Impacto'].sum(),
    df[(df['Año'] >= 1940) & (df['Año'] <= 1950)]['Impacto'].sum()
]

# Crear gráfico de barras con doble eje Y
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(
    go.Bar(
        x=decadas,
        y=avances_por_decada,
        name='Número de avances',
        marker_color='#3498DB',
        opacity=0.7
    ),
    secondary_y=False
)

fig2.add_trace(
    go.Scatter(
        x=decadas,
        y=impacto_por_decada,
        mode='lines+markers',
        name='Impacto total',
        line=dict(color='#E74C3C', width=4),
        marker=dict(size=12, color='#E74C3C')
    ),
    secondary_y=True
)

fig2.update_xaxes(title_text="Década")
fig2.update_yaxes(title_text="Número de avances médicos", secondary_y=False)
fig2.update_yaxes(title_text="Impacto total", secondary_y=True)

fig2.update_layout(
    title={
        'text': 'Progreso médico por década (1920-1950)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    height=500,
    plot_bgcolor='white'
)

fig2.show()

# Mostrar estadísticas resumidas
print("\n=== RESUMEN DE AVANCES MÉDICOS POST-PRIMERA GUERRA MUNDIAL ===")
print(f"Período analizado: {df['Año'].min()} - {df['Año'].max()}")
print(f"Total de avances registrados: {len(df)}")
print(f"Impacto promedio: {df['Impacto'].mean():.1f}/10")
print(f"Total estimado de vidas salvadas: {df['Vidas_salvadas_estimadas'].sum():,}")
print(f"\nCategoría médica más impactante: {df.groupby('Categoría')['Impacto'].mean().idxmax()}")
print(f"Año con mayor número de avances: {df['Año'].mode().iloc[0]}")

# Mostrar los 5 avances más impactantes
print("\n=== TOP 5 AVANCES MÁS IMPACTANTES ===")
top5 = df.nlargest(5, 'Impacto')[['Año', 'Descubrimiento', 'Impacto', 'Vidas_salvadas_estimadas']]
for idx, row in top5.iterrows():
    print(f"{row['Año']}: {row['Descubrimiento']} (Impacto: {row['Impacto']}/10, Vidas: {row['Vidas_salvadas_estimadas']:,})")