import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Datos históricos simulados para HDD1 y HDD2
años = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024]).reshape(-1, 1)

# HDD1: desgaste rápido
desgaste_hdd1 = np.array([5, 12, 20, 30, 45, 60, 78])

# HDD2: desgaste lento
desgaste_hdd2 = np.array([2, 4, 7, 12, 18, 25, 30])

# Función para ajustar y predecir polinómico
def predecir_desgaste(años_hist, desgaste_hist):
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(años_hist)
    modelo = LinearRegression()
    modelo.fit(X_poly, desgaste_hist)
    años_pred = np.arange(2018, 2031).reshape(-1, 1)
    X_pred_poly = poly.transform(años_pred)
    prediccion = modelo.predict(X_pred_poly)
    prediccion = np.clip(prediccion, 0, 100)
    return años_pred.flatten(), prediccion

# Predicciones para HDD1 y HDD2
años_pred, pred_hdd1 = predecir_desgaste(años, desgaste_hdd1)
_, pred_hdd2 = predecir_desgaste(años, desgaste_hdd2)

# HDD3: desgaste lineal constante 5% por año desde 2018
años_lineales = np.arange(2018, 2031)
desgaste_hdd3 = 5 * (años_lineales - 2017)  # 5% * número de años desde 2018
desgaste_hdd3 = np.clip(desgaste_hdd3, 0, 100)  # asegurar máximo 100%

# Cerrar ciclos para radar
labels = [str(a) for a in años_pred]
labels.append(labels[0])

pred_hdd1 = np.append(pred_hdd1, pred_hdd1[0])
pred_hdd2 = np.append(pred_hdd2, pred_hdd2[0])
desgaste_hdd3 = np.append(desgaste_hdd3, desgaste_hdd3[0])

# Crear gráfico radar comparativo con 3 discos
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=pred_hdd1,
    theta=labels,
    fill='toself',
    name='HDD 1 (Desgaste rápido)',
    line=dict(color='firebrick'),
    fillcolor='rgba(178,34,34,0.5)'
))

fig.add_trace(go.Scatterpolar(
    r=pred_hdd2,
    theta=labels,
    fill='toself',
    name='HDD 2 (Desgaste lento)',
    line=dict(color='royalblue'),
    fillcolor='rgba(65,105,225,0.5)'
))

fig.add_trace(go.Scatterpolar(
    r=desgaste_hdd3,
    theta=labels,
    fill='toself',
    name='HDD 3 (Incremento lineal 5%/año)',
    line=dict(color='forestgreen'),
    fillcolor='rgba(34,139,34,0.5)'
))

# Configuraciones finales
fig.update_layout(
    title='Comparación Radar de Desgaste de Discos Duros (2018–2030)',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 105],
            tickfont=dict(size=10)
        )
    ),
    template='plotly_white',
    showlegend=True
)

fig.show()
