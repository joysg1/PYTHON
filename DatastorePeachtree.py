import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Configuración del escenario
# Datastore: 1TB, VM Windows Server 2012 R2, Peachtree, 5 usuarios, 6 días/semana

# Generar datos horarios para una semana típica (Lunes a Sábado)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
horas = list(range(24))

# Patrones de uso basados en software contable Peachtree y requisitos encontrados
# Peachtree es intensivo en I/O durante: apertura, guardado, respaldos, reportes

def generar_patron_io(dia_semana, hora):
    """Genera patrón de I/O basado en uso típico de Peachtree"""
    base_io = 5  # MB/s baseline para Windows Server 2012 R2
    
    # Domingo - día de descanso
    if dia_semana == 6:
        # Solo tareas de mantenimiento del SO y antivirus
        return base_io + random.uniform(2, 8)
    
    # Días laborales - patrón típico de oficina contable
    if 7 <= hora <= 8:  # Arranque de sistemas
        return base_io + random.uniform(15, 25)
    elif 9 <= hora <= 11:  # Pico matutino - apertura de Peachtree, consultas
        return base_io + random.uniform(20, 40)
    elif 12 <= hora <= 13:  # Almuerzo - actividad reducida
        return base_io + random.uniform(5, 15)
    elif 14 <= hora <= 17:  # Pico vespertino - transacciones, reportes
        return base_io + random.uniform(25, 50)
    elif 17 <= hora <= 18:  # Respaldos y cierre
        return base_io + random.uniform(30, 60)
    elif 19 <= hora <= 22:  # Mantenimiento nocturno
        return base_io + random.uniform(8, 20)
    else:  # Horas nocturnas
        return base_io + random.uniform(1, 10)

def generar_uso_cpu(io_mbps):
    """Genera uso de CPU correlacionado con I/O"""
    # Windows Server 2012 R2 + Peachtree con 5 usuarios
    base_cpu = 15  # % baseline
    io_factor = io_mbps * 0.8  # I/O intensivo incrementa CPU
    return min(95, base_cpu + io_factor + random.uniform(-5, 15))

def generar_uso_memoria(dia_semana, hora, usuarios_activos):
    """Genera uso de memoria basado en Peachtree multiusuario"""
    # Requisitos base: Windows Server 2012 R2 + Peachtree
    base_memoria = 2.5  # GB base del sistema
    peachtree_base = 1.0  # GB base de Peachtree server
    usuario_overhead = 0.3  # GB por usuario activo
    
    memoria_total = base_memoria + peachtree_base + (usuarios_activos * usuario_overhead)
    
    # Variación por actividades específicas
    if 9 <= hora <= 17 and dia_semana < 6:  # Horario laboral
        memoria_total += random.uniform(0.5, 1.5)  # Consultas, reportes
    
    return min(16, memoria_total)  # Máximo 16GB (configuración típica)

def usuarios_activos_por_hora(dia_semana, hora):
    """Determina usuarios activos según horario"""
    if dia_semana == 6:  # Domingo
        return 0
    
    if dia_semana == 5:  # Sábado - medio día
        if 8 <= hora <= 13:
            return random.randint(1, 3)
        return 0
    
    # Días laborales (Lunes-Viernes)
    if 9 <= hora <= 17:
        return random.randint(3, 5)  # 3-5 usuarios activos
    elif 8 <= hora <= 9 or 17 <= hora <= 18:
        return random.randint(1, 3)  # Llegada/salida
    else:
        return 0

# Generar datos para la semana
datos_semana = []
for dia_idx, dia in enumerate(dias):
    for hora in horas:
        usuarios = usuarios_activos_por_hora(dia_idx, hora)
        io_mbps = generar_patron_io(dia_idx, hora)
        cpu_pct = generar_uso_cpu(io_mbps)
        memoria_gb = generar_uso_memoria(dia_idx, hora, usuarios)
        
        datos_semana.append({
            'Dia': dia,
            'Dia_Num': dia_idx,
            'Hora': hora,
            'Timestamp': f"{dia} {hora:02d}:00",
            'IO_MBps': round(io_mbps, 1),
            'CPU_Porcentaje': round(cpu_pct, 1),
            'Memoria_GB': round(memoria_gb, 1),
            'Usuarios_Activos': usuarios,
            'IOPS': round(io_mbps * 8, 0)  # Estimación IOPS basada en I/O
        })

# Crear DataFrame
df = pd.DataFrame(datos_semana)

# Crear subplots para múltiples métricas
fig = make_subplots(
    rows=4, cols=1,
    subplot_titles=[
        'Demanda I/O del Datastore (MB/s)',
        'Uso de CPU del Servidor (%)',
        'Uso de Memoria RAM (GB)',
        'Usuarios Activos en Peachtree'
    ],
    vertical_spacing=0.08,
    shared_xaxes=True
)

# Colores para cada día
colores_dias = {
    'Lunes': '#FF6B6B',
    'Martes': '#4ECDC4', 
    'Miércoles': '#45B7D1',
    'Jueves': '#96CEB4',
    'Viernes': '#FECA57',
    'Sábado': '#FF9FF3',
    'Domingo': '#95A5A6'
}

# Gráfico 1: I/O del Datastore
x_labels = [f"{dia} {hora:02d}:00" for dia, hora in zip(df['Dia'], df['Hora'])]

fig.add_trace(
    go.Scatter(
        x=list(range(len(df))),
        y=df['IO_MBps'],
        mode='lines+markers',
        name='I/O Datastore',
        line=dict(color='#FF6B6B', width=2),
        marker=dict(size=4),
        fill='tonexty',
        fillcolor='rgba(255, 107, 107, 0.3)',
        hovertemplate='<b>%{text}</b><br>I/O: %{y} MB/s<br>IOPS: %{customdata}<extra></extra>',
        text=[f"{dia} {hora:02d}:00" for dia, hora in zip(df['Dia'], df['Hora'])],
        customdata=df['IOPS']
    ), row=1, col=1
)

# Gráfico 2: CPU
fig.add_trace(
    go.Scatter(
        x=list(range(len(df))),
        y=df['CPU_Porcentaje'],
        mode='lines+markers',
        name='CPU Usage',
        line=dict(color='#4ECDC4', width=2),
        marker=dict(size=4),
        fill='tonexty',
        fillcolor='rgba(78, 205, 196, 0.3)',
        hovertemplate='<b>%{text}</b><br>CPU: %{y}%<extra></extra>',
        text=[f"{dia} {hora:02d}:00" for dia, hora in zip(df['Dia'], df['Hora'])]
    ), row=2, col=1
)

# Gráfico 3: Memoria
fig.add_trace(
    go.Scatter(
        x=list(range(len(df))),
        y=df['Memoria_GB'],
        mode='lines+markers',
        name='Memoria RAM',
        line=dict(color='#45B7D1', width=2),
        marker=dict(size=4),
        fill='tonexty',
        fillcolor='rgba(69, 183, 209, 0.3)',
        hovertemplate='<b>%{text}</b><br>RAM: %{y} GB<extra></extra>',
        text=[f"{dia} {hora:02d}:00" for dia, hora in zip(df['Dia'], df['Hora'])]
    ), row=3, col=1
)

# Gráfico 4: Usuarios Activos (barras)
fig.add_trace(
    go.Bar(
        x=list(range(len(df))),
        y=df['Usuarios_Activos'],
        name='Usuarios Activos',
        marker_color='#FECA57',
        opacity=0.8,
        hovertemplate='<b>%{text}</b><br>Usuarios: %{y}<extra></extra>',
        text=[f"{dia} {hora:02d}:00" for dia, hora in zip(df['Dia'], df['Hora'])]
    ), row=4, col=1
)

# Personalizar diseño
fig.update_layout(
    height=1000,
    title={
        'text': 'Demandas del Datastore 1TB - Windows Server 2012 R2 con Peachtree<br><sub>5 usuarios • 6 días laborales • Patrón semanal de uso contable</sub>',
        'x': 0.5,
        'font': {'size': 18}
    },
    showlegend=False,
    template='plotly_white',
    hovermode='x unified'
)

# Configurar ejes X con etiquetas de días
tick_positions = []
tick_labels = []
for i in range(0, len(df), 24):  # Cada 24 horas (inicio de día)
    tick_positions.append(i)
    tick_labels.append(df.iloc[i]['Dia'])

fig.update_xaxes(
    tickmode='array',
    tickvals=tick_positions,
    ticktext=tick_labels,
    row=4, col=1
)

# Añadir líneas de referencia
fig.add_hline(y=50, line_dash="dash", line_color="red", opacity=0.7, 
              annotation_text="Alto I/O", row=1, col=1)
fig.add_hline(y=80, line_dash="dash", line_color="orange", opacity=0.7, 
              annotation_text="CPU Alta", row=2, col=1)
fig.add_hline(y=12, line_dash="dash", line_color="blue", opacity=0.7, 
              annotation_text="RAM Alta", row=3, col=1)

fig.show()

# Crear resumen estadístico
print("=" * 80)
print("ANÁLISIS DE DEMANDAS DEL DATASTORE - PEACHTREE MULTIUSUARIO")
print("=" * 80)
print("CONFIGURACIÓN:")
print("• Datastore: 1TB VMFS")
print("• VM: Windows Server 2012 R2") 
print("• Software: Peachtree/Sage 50 Multiusuario")
print("• Usuarios: 5 concurrentes")
print("• Operación: 6 días/semana")
print("=" * 80)

# Estadísticas por día
for dia in dias:
    df_dia = df[df['Dia'] == dia]
    if len(df_dia) > 0:
        print(f"{dia}:")
        print(f"  I/O promedio: {df_dia['IO_MBps'].mean():.1f} MB/s")
        print(f"  I/O pico: {df_dia['IO_MBps'].max():.1f} MB/s")
        print(f"  CPU promedio: {df_dia['CPU_Porcentaje'].mean():.1f}%")
        print(f"  RAM promedio: {df_dia['Memoria_GB'].mean():.1f} GB")
        print(f"  Usuarios máximo: {df_dia['Usuarios_Activos'].max()}")
        print()

print("RECOMENDACIONES TÉCNICAS:")
print("• SSD recomendado para mejor rendimiento de Peachtree")
print("• Respaldo automático fuera de horario laboral (18:00-07:00)")  
print("• Monitoreo de IOPS durante picos de reportes (14:00-17:00)")
print("• RAM: 8-16GB suficiente para esta carga")
print("=" * 80)