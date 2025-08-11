import plotly.graph_objects as go

# Definimos las funcionalidades a comparar
funcionalidades = ['Virtualización', 'Clustering', 'Almacenamiento', 'Redes', 'Seguridad', 'Escalabilidad']

# Definimos las puntuaciones para cada plataforma
proxmox_puntuaciones = [9, 8, 7, 8, 9, 8]
esxi_puntuaciones = [8, 9, 8, 7, 8, 9]

# Creamos el gráfico de radar
fig = go.Figure(data=[
    go.Scatterpolar(
        r=proxmox_puntuaciones,
        theta=funcionalidades,
        fill='toself',
        name='Proxmox'
    ),
    go.Scatterpolar(
        r=esxi_puntuaciones,
        theta=funcionalidades,
        fill='toself',
        name='ESXi'
    )
])

# Configuramos el gráfico
fig.update_layout(
    title='Comparativa de funcionalidades entre Proxmox y ESXi',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )
    ),
    showlegend=True
)

# Mostramos el gráfico
fig.show()
