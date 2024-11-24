import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
train_data = pd.read_csv('train.csv')

# Filtro 1: Edad promedio de los sobrevivientes en función del género
sobrevivientes = train_data[train_data['Survived'] == 1]
edad_promedio = sobrevivientes.groupby('Sex')['Age'].mean()
plt.figure(figsize=(8,6))
sns.set_palette("pastel")
sns.barplot(x=edad_promedio.index, y=edad_promedio.values, color="#C7B8EA")
for i, v in enumerate(edad_promedio.values):
    plt.text(i, v + 1, str(round(v, 2)), color='black', ha='center', fontsize=14, fontweight='bold')
plt.title('Edad promedio de los sobrevivientes en función del género', fontsize=16, fontweight='bold')
plt.xlabel('Género', fontsize=14, fontweight='bold')
plt.ylabel('Edad promedio', fontsize=14, fontweight='bold')
plt.show()

# Filtro 2: Agrupar los sobrevivientes por género y clase
sobrevivientes = train_data[train_data['Survived'] == 1]
sobrevivientes_grupo = sobrevivientes.groupby(['Sex', 'Pclass'])['Survived'].count().unstack()
plt.figure(figsize=(10,8))
sns.set_palette("pastel")
sns.heatmap(sobrevivientes_grupo, annot=True, cmap='Pastel1', fmt='d', linewidths=0.5, linecolor='white')
plt.title('Sobrevivientes agrupados por género y clase', fontsize=16, fontweight='bold')
plt.xlabel('Clase', fontsize=14, fontweight='bold')
plt.ylabel('Género', fontsize=14, fontweight='bold')
plt.show()

