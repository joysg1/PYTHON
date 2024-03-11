import math

# Clase padre FiguraGeometrica

class FiguraGeometrica:
    def calcular_area(self):
        pass
    
# Clase hija Circulo que hereda de FiguraGeometrica
   
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):  # Sobrecarga del metodo calcular_area
        return math.pi * self.radio **2   # Retorno del radio al cuadrado para calcular el area del circulo
    
    
# Clase hija Rectangulo que hereda de FiguraGeometrica  

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self): # Sobrecarga del metodo calcular_area
        return (self.base * self.altura)   # Retorno de la base por la altura para calcular el area del rectangulo 

# Funcion para calcular el area de una figura

def calcular_Area_Figura(figura):
    return figura.calcular_area()


# Instanciar los objetos de las clases Circulo y Rectangulo

MiCirculo = Circulo(5)
MiRectangulo = Rectangulo(4,6)

# Llamado de la funcion calcular_area_figura y guardado en variables

resultadoCirculo = calcular_Area_Figura(MiCirculo)
resultadoRectangulo = calcular_Area_Figura(MiRectangulo)

# Impresion de resultados haciendo uso de las variables


print(f"El area del circulo con radio: {MiCirculo.radio} es de: {resultadoCirculo:.2f}")
print(f"El area del rectangulo con base: {MiRectangulo.base} y altura: {MiRectangulo.altura} es de: {resultadoRectangulo:.2f}")

print("\n")
print("*"*80)


# Se coloca el :.2f para dos decimales

