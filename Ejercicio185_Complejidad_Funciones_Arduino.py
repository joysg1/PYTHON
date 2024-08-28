import plotly.graph_objects as go
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Datos para el gráfico
funciones = ['Ciclo for', 'Ciclo do-while', 'pinMode', 'DigitalRead', 'DigitalWrite', 'analogRead', 'analogWrite', 'delay', 'millis', 'min', 'max']
frecuencia_uso = [20, 15, 10, 8, 8, 6, 6, 4, 2, 2, 2]
sintaxis = ['for (inicialización; condición; incremento) { código a ejecutar }', 'do { código a ejecutar } while (condición);', 'pinMode(pin, modo)', 'digitalRead(pin)', 'digitalWrite(pin, valor)', 'analogRead(pin)', 'analogWrite(pin, valor)', 'delay(tiempo)', 'millis()', 'min(a, b)', 'max(a, b)']
ejemplos = ['for (int i = 0; i < 10; i++) { Serial.println(i); }', 'int i = 0; do { Serial.println(i); i++; } while (i < 10);', 'pinMode(13, OUTPUT);', 'int estado = digitalRead(2);', 'digitalWrite(13, HIGH);', 'int valor = analogRead(A0);', 'analogWrite(9, 128);', 'delay(1000);', 'unsigned long tiempo = millis();', 'int minimo = min(5, 10);', 'int maximo = max(5, 10);']

# Crear un DataFrame
df = pd.DataFrame({'Función': funciones, 'Frecuencia de uso': frecuencia_uso, 'Sintaxis': sintaxis, 'Ejemplo': ejemplos})

# Crear el gráfico de pastel
fig = go.Figure(data=[go.Pie(labels=df['Función'], values=df['Frecuencia de uso'], hovertext=df['Sintaxis'] + '<br>' + df['Ejemplo'], hoverinfo='text', hoverlabel=dict(font_size=24))])

# Configurar el tamaño del gráfico
fig.update_layout(width=800, height=600, font_size=24)

# Crear un cuadro con un resumen de la sintaxis de cada función
cuadro_sintaxis = html.Div([
    html.H2('Resumen de la sintaxis de cada función', style={'textAlign': 'center', 'marginBottom': '20px', 'fontSize': 24}),
    html.Table([
        html.Tr([html.Th('Función'), html.Th('Sintaxis')], style={'backgroundColor': '#f0f0f0', 'padding': '10px', 'fontSize': 20}),
        *[html.Tr([html.Td(funcion, style={'padding': '10px', 'fontSize': 20}), html.Td(sintaxis, style={'padding': '10px', 'fontSize': 20})]) for funcion, sintaxis in zip(df['Función'], df['Sintaxis'])]
    ], style={'border': '1px solid #ddd', 'borderRadius': '10px', 'padding': '20px'})
])

# Crear la aplicación Dash
app = Dash(__name__)

# Definir la estructura de la aplicación
app.layout = html.Div([
    html.H1('Frecuencia de uso de las funciones en Arduino', style={'textAlign': 'center', 'marginBottom': '20px', 'fontSize': 36}),
    dcc.Graph(figure=fig, style={'width': '60%', 'display': 'inline-block', 'marginBottom': '20px'}),
    cuadro_sintaxis
], style={'width': '80%', 'margin': 'auto', 'padding': '20px', 'backgroundColor': '#f9f9f9', 'border': '1px solid #ddd', 'borderRadius': '10px'})

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server()





