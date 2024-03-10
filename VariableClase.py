# Las variables de la clase de definen dentro de la clase pero
# fuera de cualquier metodo

# Creacion de la clase

class Miclase:
    variable_de_clase = 2
    def __init__(self, valor):  #Constructor
        self.valor = valor 
        
        
# Acceder al valor de la variable de clase

# Al ser una variable de clase, no se debe hacer una instancia para
# acceder a su valor

print(f" Valor de la variable de clase = {Miclase.variable_de_clase}")   
print("\n")
print("*"*80)

# Instanciar objetos de la clase

Objeto1 = Miclase(1)
Objeto2 = Miclase(2)     

# Obtener el valor de la variable de clase desde las instancias

print(f"Valor de la variable de clase desde el objeto 1 = {Objeto1.variable_de_clase}")
print(f"Valor de la variable de clase desde el objeto 2 = {Objeto2.variable_de_clase}")
print("\n")
print("*"*80)

# Obtener el valor del atributo para cada objeto

print(f"Valor del atributo valor en el objeto 1 = {Objeto1.valor}")
print(f"Valor del atributo valor en el objeto 2 = {Objeto2.valor}")
print("\n")
print("*"*80)