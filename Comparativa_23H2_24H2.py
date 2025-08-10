import plotly.express as px
import pandas as pd

# Datos de rendimiento
datos = {
    "Característica": ["Velocidad de procesamiento", "Uso de memoria", "Rendimiento en juegos", "Estabilidad"],
    "Versión 23H2": [8.5, 60, 7.8, 9.5],
    "Versión 24H2": [9.2, 55, 8.5, 8.8]
}

# Crear DataFrame
df = pd.DataFrame(datos).melt(id_vars="Característica", var_name="Versión", value_name="Valor")

# Crear gráfico
fig = px.bar(df, x="Característica", y="Valor", color="Versión", barmode="group")

# Personalizar gráfico
fig.update_layout(
    title="Comparativa de rendimiento entre Windows 11 23H2 y 24H2",
    xaxis_title="Característica",
    yaxis_title="Valor"
)

# Mostrar gráfico
fig.show()
