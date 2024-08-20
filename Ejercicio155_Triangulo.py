import matplotlib.pyplot as plt
import numpy as np

varT = float(input("Ingrese la longitud del primer lado del triangulo: "))
varT2 = float(input("Ingrese la longitud del segundo lado del triangulo: "))
varT3 = float(input("Ingrese la longitud del tercer lado del triangulo: "))

# Calulo semiperimetro
semiperimetro = (varT + varT2 + varT3) / 2

# Calculo area usando el semiperimetro
area = (semiperimetro * (semiperimetro - varT) * (semiperimetro - varT2) * (semiperimetro - varT3)) ** 0.5

# Impresion del semiperimetro y del area redondeados a tres decimales
print("El semiperimetro del triangulo es: %.3f" % semiperimetro)
print("El area del triangulo es: %.3f" % area)

# Determinar el tipo de triángulo
if varT == varT2 == varT3:
    tipo_triangulo = "Equilátero"
elif varT == varT2 or varT2 == varT3 or varT == varT3:
    tipo_triangulo = "Isósceles"
else:
    tipo_triangulo = "Escaleno"

# Calculo de los vértices del triángulo
# Suponiendo que el primer lado es el que se encuentra en el eje x
x1, y1 = 0, 0
x2, y2 = varT, 0
x3, y3 = (varT2**2 - varT3**2 + varT**2) / (2*varT), np.sqrt(varT2**2 - ((varT2**2 - varT3**2 + varT**2) / (2*varT))**2)

# Creación de la figura
plt.figure()

# Dibujado del triángulo
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'b-')

# Etiquetas de los vértices
plt.annotate("A", (x1, y1), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate("B", (x2, y2), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate("C", (x3, y3), textcoords="offset points", xytext=(0,10), ha='center')

# Etiquetas de los lados
plt.annotate(str(varT), ((x1+x2)/2, (y1+y2)/2), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(str(varT2), ((x2+x3)/2, (y2+y3)/2), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(str(varT3), ((x3+x1)/2, (y3+y1)/2), textcoords="offset points", xytext=(0,10), ha='center')

# Etiqueta del área y tipo de triángulo
plt.annotate(f"Área: {area:.3f} u^2\nTipo: {tipo_triangulo}", (0.5, 0.9), xycoords='axes fraction', ha='center', fontsize=12)

# Mostrar la gráfica
plt.axis('equal')
plt.show()





