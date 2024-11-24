import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Confusion matrix: clases a, b, c, d, e
conf_matrix = np.array([
    [91, 0, 0, 0, 0],  # DrugY
    [0, 16, 0, 0, 0],  # drugC
    [0, 0, 54, 0, 0],  # drugX
    [0, 0, 0, 23, 0],  # drugA
    [0, 0, 0, 0, 16]   # drugB
])

# Etiquetas de las clases
class_labels = ['DrugY', 'drugC', 'drugX', 'drugA', 'drugB']

# Graficar la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
plt.title("Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()
