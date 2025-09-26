import pandas as pd
import plotly.express as px

# Cargar el archivo limpio
df = pd.read_csv("/home/userlm/Documentos/WWI_MACHINE_LEARNING/WW1_Clean.csv", parse_dates=["StartDate_clean", "EndDate_clean"])

# Extraer el año de inicio de la batalla
df["Year"] = df["StartDate_clean"].dt.year

# Contar batallas por año, filtrando de 1914 a 1919
battles_per_year = (
    df["Year"].value_counts()
    .sort_index()
    .loc[1914:1919]  # acotar al rango 1914-1919
)

# Crear gráfico interactivo con plotly
fig = px.bar(
    x=battles_per_year.index,
    y=battles_per_year.values,
    labels={"x": "Año", "y": "Número de batallas"},
    title="Número de batallas por año (1914–1919, Primera Guerra Mundial)",
    text=battles_per_year.values  # mostrar valores arriba
)

# Ajustar estilo del texto en las barras
fig.update_traces(textposition="outside")

# Mostrar gráfico
fig.show()
