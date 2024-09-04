import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define las características de cada tipo de nube
nube_privada = {'Seguridad', 'Control', 'Costo', 'Cumplimiento'}
nube_publica = {'Escalabilidad', 'Flexibilidad', 'Costo', 'Accesibilidad'}
nube_hibrida = {'Seguridad', 'Escalabilidad', 'Flexibilidad', 'Costo', 'Integración'}

# Crea el diagrama de Venn
venn = venn3([nube_privada, nube_publica, nube_hibrida], 
             ('Nube Privada', 'Nube Pública', 'Nube Híbrida'))

# Añade etiquetas a cada subconjunto
venn.get_label_by_id('100').set_text('\n'.join(nube_privada - nube_publica - nube_hibrida))
venn.get_label_by_id('010').set_text('\n'.join(nube_publica - nube_privada - nube_hibrida))
venn.get_label_by_id('001').set_text('\n'.join(nube_hibrida - nube_privada - nube_publica))
venn.get_label_by_id('110').set_text('\n'.join((nube_privada & nube_publica) - nube_hibrida))
venn.get_label_by_id('101').set_text('\n'.join((nube_privada & nube_hibrida) - nube_publica))
venn.get_label_by_id('011').set_text('\n'.join((nube_publica & nube_hibrida) - nube_privada))
venn.get_label_by_id('111').set_text('\n'.join(nube_privada & nube_publica & nube_hibrida))

# Añade un título
plt.title('Características de los Tipos de Nube')

# Muestra el diagrama
plt.show()





