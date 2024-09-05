
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definimos los conjuntos de las estructuras repetitivas
# Utilizamos valores que representen intersecciones y etiquetas precisas
sets = {
    '100': 1,       # 'for'
    '010': 1,       # 'while'
    '001': 1,       # 'do while'
    '110': 0.5,     # 'for' & 'while'
    '101': 0.5,     # 'for' & 'do while'
    '011': 0.5,     # 'while' & 'do while'
    '111': 0.25     # 'All'
}

# Crear el diagrama de Venn
plt.figure(figsize=(30, 22))
venn = venn3(subsets=sets, set_labels=('For', 'While', 'Do While'))

# Etiquetas precisas para cada sección
venn.get_label_by_id('100').set_text('Sobre secuencia')
venn.get_label_by_id('010').set_text('Mientras condición')
venn.get_label_by_id('001').set_text('Al menos una vez')
venn.get_label_by_id('110').set_text('Breaks y continues')
venn.get_label_by_id('101').set_text('Breaks y continues')
venn.get_label_by_id('011').set_text('Variables de control')
venn.get_label_by_id('111').set_text('Iteran')

# Ajustar el título
plt.title("Diagrama de Venn: Estructuras Repetitivas")

# Mostrar el diagrama
plt.show()




