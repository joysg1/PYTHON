import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Configuración para evitar errores comunes
import warnings
warnings.filterwarnings('ignore')

def crear_visualizaciones_ciberseguridad():
    """
    Función principal para crear visualizaciones de ciberseguridad en Panamá
    """
    
    print("Iniciando creación de visualizaciones...")
    
    # === DATOS DE EJEMPLO ===
    # Evolución de incidentes de ciberseguridad
    df_incidentes = pd.DataFrame({
        'Año': [2019, 2020, 2021, 2022, 2023, 2024],
        'Incidentes_Reportados': [67, 89, 123, 156, 178, 201],
        'Incidentes_Resueltos': [59, 78, 110, 142, 165, 189],
        'Tiempo_Resolucion_Dias': [12, 10, 8, 6, 5, 4]
    })
    
    # Inversión en ciberseguridad
    df_inversion = pd.DataFrame({
        'Año': [2019, 2020, 2021, 2022, 2023, 2024],
        'Inversion_Millones_USD': [3.2, 4.1, 5.8, 7.2, 8.9, 10.5],
        'Profesionales_Capacitados': [165, 210, 280, 350, 420, 510]
    })
    
    # Comparación regional
    df_regional = pd.DataFrame({
        'Pais': ['Panamá', 'Costa Rica', 'Guatemala', 'Honduras', 'El Salvador'],
        'Indice_Ciberseguridad': [0.72, 0.68, 0.45, 0.38, 0.42]
    })
    
    # === VISUALIZACIÓN 1: EVOLUCIÓN DE INCIDENTES ===
    print("Creando gráfico 1: Evolución de incidentes...")
    
    fig1 = go.Figure()
    
    # Línea de incidentes reportados
    fig1.add_trace(go.Scatter(
        x=df_incidentes['Año'],
        y=df_incidentes['Incidentes_Reportados'],
        mode='lines+markers',
        name='Incidentes Reportados',
        line=dict(color='red', width=3),
        marker=dict(size=8)
    ))
    
    # Línea de incidentes resueltos
    fig1.add_trace(go.Scatter(
        x=df_incidentes['Año'],
        y=df_incidentes['Incidentes_Resueltos'],
        mode='lines+markers',
        name='Incidentes Resueltos',
        line=dict(color='green', width=3),
        marker=dict(size=8)
    ))
    
    fig1.update_layout(
        title='Evolución de Incidentes de Ciberseguridad en Panamá',
        xaxis_title='Año',
        yaxis_title='Número de Incidentes',
        template='plotly_white',
        hovermode='x unified'
    )
    
    # === VISUALIZACIÓN 2: INVERSIÓN Y CAPACITACIÓN ===
    print("Creando gráfico 2: Inversión y capacitación...")
    
    fig2 = px.bar(df_inversion, 
                  x='Año', 
                  y='Inversion_Millones_USD',
                  title='Inversión en Ciberseguridad en Panamá',
                  labels={'Inversion_Millones_USD': 'Inversión (Millones USD)'},
                  color='Inversion_Millones_USD',
                  color_continuous_scale='Blues')
    
    fig2.update_layout(template='plotly_white')
    
    # === VISUALIZACIÓN 3: COMPARACIÓN REGIONAL ===
    print("Creando gráfico 3: Comparación regional...")
    
    # Ordenar por índice para mejor visualización
    df_regional_sorted = df_regional.sort_values('Indice_Ciberseguridad', ascending=True)
    
    fig3 = px.bar(df_regional_sorted, 
                  x='Indice_Ciberseguridad', 
                  y='Pais',
                  orientation='h',
                  title='Índice de Ciberseguridad - Comparación Regional',
                  labels={'Indice_Ciberseguridad': 'Índice de Ciberseguridad (0-1)'},
                  color='Indice_Ciberseguridad',
                  color_continuous_scale='RdYlGn')
    
    fig3.update_layout(template='plotly_white')
    
    # === VISUALIZACIÓN 4: TIEMPO DE RESOLUCIÓN ===
    print("Creando gráfico 4: Tiempo de resolución...")
    
    fig4 = go.Figure()
    
    fig4.add_trace(go.Scatter(
        x=df_incidentes['Año'],
        y=df_incidentes['Tiempo_Resolucion_Dias'],
        mode='lines+markers',
        name='Tiempo Promedio',
        line=dict(color='orange', width=3),
        marker=dict(size=10),
        fill='tozeroy',
        fillcolor='rgba(255,165,0,0.2)'
    ))
    
    fig4.update_layout(
        title='Mejora en Tiempo de Resolución de Incidentes',
        xaxis_title='Año',
        yaxis_title='Días Promedio',
        template='plotly_white'
    )
    
    # === VISUALIZACIÓN 5: CRECIMIENTO DE PROFESIONALES ===
    print("Creando gráfico 5: Crecimiento de profesionales...")
    
    fig5 = px.area(df_inversion, 
                   x='Año', 
                   y='Profesionales_Capacitados',
                   title='Crecimiento de Profesionales Capacitados en Ciberseguridad',
                   labels={'Profesionales_Capacitados': 'Número de Profesionales'})
    
    fig5.update_traces(fill='tonexty', fillcolor='rgba(0,100,80,0.2)', line_color='teal')
    fig5.update_layout(template='plotly_white')
    
    # === MOSTRAR TODAS LAS VISUALIZACIONES ===
    try:
        print("Mostrando visualizaciones...")
        fig1.show()
        fig2.show()
        fig3.show() 
        fig4.show()
        fig5.show()
        
        print("\n✅ Todas las visualizaciones se crearon exitosamente!")
        
    except Exception as e:
        print(f"❌ Error al mostrar gráficos: {e}")
        print("💡 Intenta guardar las visualizaciones como archivos HTML:")
        
        # Guardar como archivos HTML si hay problemas para mostrar
        fig1.write_html("incidentes_panama.html")
        fig2.write_html("inversion_panama.html")
        fig3.write_html("comparacion_regional.html")
        fig4.write_html("tiempo_resolucion.html")
        fig5.write_html("profesionales_panama.html")
        
        print("📁 Archivos HTML guardados exitosamente!")
    
    return fig1, fig2, fig3, fig4, fig5

def crear_dashboard_simple():
    """
    Función alternativa para crear un dashboard más simple
    """
    print("Creando dashboard simplificado...")
    
    # Datos básicos
    años = [2020, 2021, 2022, 2023, 2024]
    incidentes = [89, 123, 156, 178, 201]
    inversion = [4.1, 5.8, 7.2, 8.9, 10.5]
    
    # Crear figura simple
    fig = go.Figure()
    
    # Agregar línea de incidentes
    fig.add_trace(go.Scatter(
        x=años,
        y=incidentes,
        mode='lines+markers+text',
        name='Incidentes Ciberseguridad',
        text=incidentes,
        textposition="top center",
        line=dict(color='red', width=2),
        marker=dict(size=8)
    ))
    
    # Configurar layout
    fig.update_layout(
        title='Ciberseguridad en Panamá - Tendencia de Incidentes',
        xaxis_title='Año',
        yaxis_title='Número de Incidentes',
        template='simple_white',
        showlegend=True,
        width=800,
        height=500
    )
    
    return fig

# === EJECUCIÓN PRINCIPAL ===
if __name__ == "__main__":
    try:
        # Intentar crear todas las visualizaciones
        figuras = crear_visualizaciones_ciberseguridad()
        
    except Exception as error:
        print(f"❌ Error en visualizaciones completas: {error}")
        print("🔄 Intentando con dashboard simplificado...")
        
        try:
            # Dashboard alternativo más simple
            fig_simple = crear_dashboard_simple()
            fig_simple.show()
            print("✅ Dashboard simplificado creado exitosamente!")
            
        except Exception as error2:
            print(f"❌ Error en dashboard simplificado: {error2}")
            print("\n🛠️  SOLUCIONES SUGERIDAS:")
            print("1. Instalar dependencias: pip install plotly pandas numpy")
            print("2. Actualizar plotly: pip install --upgrade plotly")
            print("3. Verificar versión Python: python --version")
            print("4. Ejecutar en Jupyter Notebook si es posible")

# Mensaje de ayuda
print("\n" + "="*50)
print("INSTRUCCIONES DE USO:")
print("="*50)
print("1. Asegúrate de tener instalado: pip install plotly pandas numpy")
print("2. Ejecuta el script: python nombre_del_archivo.py")
print("3. Si hay errores, revisa las soluciones sugeridas")
print("4. Reemplaza los datos de ejemplo con información real")
print("="*50)