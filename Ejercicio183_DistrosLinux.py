import seaborn as sns
import matplotlib.pyplot as plt

# Datos de ejemplo (puedes reemplazarlos con tus propios datos)
sistemas_operativos = ['Ubuntu', 'Debian', 'Fedora', 'CentOS', 'Arch Linux', 'openSUSE']
distribucion = [23, 17, 12, 10, 8, 5]

# Colores para cada barra
colores = ['#4CAF50', '#FF9800', '#2196F3', '#F44336', '#8BC34A', '#9C27B0']

# Crear un gráfico de barras
sns.set()
plt.figure(figsize=(10, 6))
sns.barplot(x=sistemas_operativos, y=distribucion, palette=colores)

# Agregar título y etiquetas
plt.title('Distribución de sistemas operativos libres')
plt.xlabel('Sistema operativo')
plt.ylabel('Porcentaje de uso')

# Mostrar el gráfico
plt.show()
