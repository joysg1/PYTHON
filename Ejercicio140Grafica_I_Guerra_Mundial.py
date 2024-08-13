import matplotlib.pyplot as plt

# Datos de pérdidas de soldados por bando en la Primera Guerra Mundial
paises = ['Imperios Centrales', 'Aliados']
soldados_perdidos = [4000000, 6000000]

# Crear gráfico de barras
plt.bar(paises, soldados_perdidos, color=['red', 'blue'])
plt.xlabel('Bando')
plt.ylabel('Soldados perdidos')
plt.title('Perdidas de soldados por bando en la Primera Guerra Mundial')

# Mostrar gráfico
plt.show()