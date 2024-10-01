import matplotlib.pyplot as plt

# Datos
etiquetas = ['Clasificaciones Correctas', 'Clasificaciones Incorrectas']
valores = [36, 7]  # 43 total (36 correctas, 7 incorrectas)

# Colores pastel
colores = ['#A8E6CF', '#FF8C94']  # Colores pastel

# Función para mostrar el número de instancias y el porcentaje
def etiqueta_funcion(pct, allvals):
    absolute = int(pct / 100. * sum(allvals))
    return f"{absolute} ({pct:.1f}%)"

# Crear el gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(valores, labels=etiquetas, autopct=lambda pct: etiqueta_funcion(pct, valores), startangle=140, colors=colores)

# Agregar título y poner en negrita
plt.title('Distribución de Clasificaciones del Modelo', fontweight='bold')

# Aumentar tamaño de las leyendas
plt.setp(plt.gca().texts, fontsize=14)  # Cambia el tamaño de las leyendas

# Mostrar el gráfico
plt.axis('equal')  # Para que el pastel se vea como un círculo
plt.show()

