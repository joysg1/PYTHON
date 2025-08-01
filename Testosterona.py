import numpy as np
import plotly.graph_objects as go
from scipy.integrate import simpson

# Días de abstinencia (0 a 14 días)
dias = np.linspace(0, 14, 100)

# Modelo hipotético de testosterona (ng/dL)
testosterona = 500 + 150 * np.exp(-0.5 * (dias - 7)**2)

# Área bajo la curva
auc = simpson(testosterona, dias)

# Crear la figura
fig = go.Figure()

# Curva de testosterona
fig.add_trace(go.Scatter(
    x=dias,
    y=testosterona,
    mode='lines',
    name='Testosterona (ng/dL)',
    line=dict(color='blue')
))

# Área bajo la curva
fig.add_trace(go.Scatter(
    x=np.concatenate([dias, dias[::-1]]),
    y=np.concatenate([testosterona, np.zeros_like(testosterona)]),
    fill='toself',
    fillcolor='rgba(135, 206, 250, 0.5)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo='skip',
    name=f'AUC ≈ {auc:.2f}'
))

# Configuración del gráfico
fig.update_layout(
    title='Aumento de la Testosterona con los Días de Abstinencia',
    xaxis_title='Días de Abstinencia',
    yaxis_title='Nivel de Testosterona (ng/dL)',
    template='plotly_white'
)

fig.show()
