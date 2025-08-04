import plotly.express as px
import pandas as pd
import numpy as np

# Datos hipotéticos de proporciones de CH4 vs CO2 (en Gt, gigatoneladas) desde 2025 a 2030
anos = np.array([2025, 2026, 2027, 2028, 2029, 2030])
ch4_proporciones = np.array([3.5, 3.7, 4.0, 4.2, 4.5, 4.8])
co2_proporciones = np.array([40, 42, 45, 48, 50, 52])

# Crear DataFrames separados para CH4 y CO2
df_ch4 = pd.DataFrame({
    'Año': anos,
    'Gas': ['CH4'] * len(anos),
    'Emisiones (Gt)': ch4_proporciones
})

df_co2 = pd.DataFrame({
    'Año': anos,
    'Gas': ['CO2'] * len(anos),
    'Emisiones (Gt)': co2_proporciones
})

# Concatenar los DataFrames
df = pd.concat([df_ch4, df_co2])

# Gráfico de barras
fig = px.bar(df, x='Año', y='Emisiones (Gt)', color='Gas', barmode='group')
fig.update_layout(title='Emisiones de CH4 y CO2',
                  xaxis_title='Año',
                  yaxis_title='Emisiones (Gt)')

# Cálculo de la proporción CH4/CO2
proporcion_ch4_vs_co2 = ch4_proporciones / co2_proporciones

# DataFrame para la proporción
df_proporcion = pd.DataFrame({
    'Año': anos,
    'Proporción CH4/CO2': proporcion_ch4_vs_co2
})

# Gráfico de línea para la proporción CH4/CO2
fig2 = px.line(df_proporcion, x='Año', y='Proporción CH4/CO2')
fig2.update_layout(title='Proporción de Emisiones CH4 vs CO2',
                   xaxis_title='Año',
                   yaxis_title='Proporción CH4/CO2')

# Mostrar los gráficos
fig.show()
fig2.show()
