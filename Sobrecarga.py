'''
Lista de metodos para sobrecargar operadores
__add__ +
__sub__(self,other)
__mul__(self,other)
__truediv__(self,other)
__eq__ ==
__ne__ !=
__lt__ <
__le__ <=
__gt__ >
__ge__ >=

'''

# Sobrecarga del operador + 

class MiNumero: #Clase mi numero 
    def __init__(self, valor): #Constructor
        self.valor = valor
    def __add__(self, other):        #Sobrecargar el metodo de la suma  
        if isinstance(other, MiNumero): #Comprobar instancia
            return MiNumero(self.valor + other.valor)
        elif isinstance(other, (int, float)):
            return MiNumero(self.valor + other)
        else:
            raise TypeError("Operacion no soportada")
    def __str__(self):
        return str(self.valor)    
    
    
# Crear objetos de la clase MiNumero

numero1 = MiNumero(5)
numero2 = MiNumero(10)   
resultado1 = numero1 + numero2
resultado2 = numero1 + 5
print(f"Resultado1 = {resultado1}") 
print(f"Resultado2 = {resultado2}")
print("\n")
print("*"*80)

texto = "Hola"

try:
   resultado3 = numero1 + texto
   print(resultado3)
except Exception as e:
    print("Error") 

print("\n")
print("*"*80)

# En este ejemplo se sobrecarga el operador suma mediante el metodo add 
# Este metodo verifica si el otro objeto es una instancia de MiNumero
# O un numero int o float y luego realiza la operacion de suma correspondiente
# Esto permite que los objetos de MiNumero se sumen de manera personalizada
# La sobrecarga de operadores permite personalizar el comportamiento de tus clases
# y hacer que los objetos de esa clase se comporten como desees cuando se utilizan
# con operadores incorporados 


# Sobrecarga del operador = 

class Persona:
  def __init__(self, nombre, edad):  # Constructor
      self.nombre = nombre
      self.edad = edad
  def __eq__(self, other):   # Sobrecarga del operador =
      if isinstance(other, Persona): # Comprobar instancia
          return self.nombre == other.nombre and self.edad == other.edad
      return False
  def __str__(self):
      return f"Nombre: {self.nombre} - Edad: {self.edad}"
  
  
  
  
# Crear objetos de la clase Persona

persona1 = Persona("Juan",30)
persona2 = Persona("Luisa",21)
persona3 = Persona("Luisa",21)

igualdad1 = persona1 == persona2
igualdad2 = persona2 == persona3

print(f"Datos de la persona1 = {persona1}") 
print(f"Datos de la persona2 = {persona2}") 
print(f"Datos de la persona3 = {persona3}")
print(f"Es la persona1 {persona1} igual a la persona2 {persona2} ? {igualdad1}")
print(f"Es la persona2 {persona2} igual a la persona3 {persona3} ? {igualdad2}")

print("\n")
print("*"*80)
  
  

# Al usar la sobrecarga del operador igualdad podemos comparar objetos
# de la clase persona de manera personalizada y determinar si representan
# a la misma persona basados en sus atributos nombre y edad   