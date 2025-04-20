import plotly.graph_objects as go

# Categorías a comparar
categories = [
    "Facilidad de uso", "Soporte de RAID", "Sistema de archivos",
    "Plugins/extensiones", "Comunidad/soporte", "Rendimiento",
    "Seguridad", "Precio/licencia"
]

# Datos comparativos (0-10)
openmediavault = [8, 8, 7, 9, 8, 7, 7, 10]
truenas = [7, 10, 10, 6, 9, 9, 9, 10]
unraid = [9, 7, 6, 10, 8, 8, 8, 5]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=openmediavault,
    theta=categories,
    fill='toself',
    name='OpenMediaVault'
))
fig.add_trace(go.Scatterpolar(
    r=truenas,
    theta=categories,
    fill='toself',
    name='TrueNAS'
))
fig.add_trace(go.Scatterpolar(
    r=unraid,
    theta=categories,
    fill='toself',
    name='Unraid'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )
    ),
    title="Comparativa de OpenMediaVault vs TrueNAS vs Unraid",
    showlegend=True
)

fig.show()
