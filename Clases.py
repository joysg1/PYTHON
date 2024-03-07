# Las clases son plantillas para instanciar objetos con sus atributos y
# metodos

# Creacion de la clase
class Auto:
    def __init__(self, color, velocidadMaxima, marca): #Metodo constructor
        self.color = color
        self.velocidadMaxima = velocidadMaxima #Atributos
        self.velocidad = 0 
        self.marca = marca
         
    def arrancar(self):   #Metodos 
        print('Arrancado')
    def acelerar(self):
        if self.velocidad == 0:
            self.velocidad = 10 
        else:
            self.velocidad = self.velocidad +10 
        print(f"Velocidad actual = {self.velocidad}")       
    def frenar(self):
        if self.velocidad > 10:
            self.velocidad = self.velocidad -10
        else:
            self.velocidad = 0
        print(f'Velocidad actual = {self.velocidad}')  
    def muestraEstado(self):
        print(f'Auto marca = {self.marca}, Color = {self.color}, Velocidad Maxima = {self.velocidadMaxima}')                    

# Instanciar un objetos
AutoToyota = Auto('Negro',100,'Toyota')
AutoNissan = Auto('Azul',200,'Nissan')
AutoSuzuki = Auto('Verde',150,'Suzuki')

# Llamar a los metodos para el AutoToyota

AutoToyota.arrancar()
AutoToyota.acelerar()
AutoToyota.acelerar()
AutoToyota.frenar()
AutoToyota.muestraEstado()
print("\n")
print("*"*80)

# Llamar a los metodos para el AutoNissan

AutoNissan.arrancar()
AutoNissan.acelerar()
AutoNissan.acelerar()
AutoNissan.frenar()
AutoNissan.muestraEstado()
print("\n")
print("*"*80)

# Llamar a los metodos para el AutoSuzuki

AutoSuzuki.arrancar()
AutoSuzuki.acelerar()
AutoSuzuki.acelerar()
AutoSuzuki.frenar()
AutoSuzuki.muestraEstado()
print("\n")
print("*"*80)


# Herencia, sirve para crear objetos con metodos y atributos de otros objetos 
# y solo agregar los atributos o metodos que lo diferencien

# Creacion de la clase Moto que hereda de la clase Auto

class Moto(Auto):
   def __init__(self, color, velocidadMaxima, marca, tipo): #Constructor de la clase Moto
       Auto.__init__(self, color, velocidadMaxima, marca) #Constructor de la clase Padre: Auto
       self.tipo = tipo   #Colocamos el atributo que difiere entre Moto y auto

   def muestraEstado(self):
        print(f'Moto marca = {self.marca}, Color = {self.color}, Velocidad Maxima = {self.velocidadMaxima}, Tipo = {self.tipo}') 



# Creacion de la clase Camion que hereda de la clase Auto

class Camion(Auto):
    def __init__(self, color, velocidadMaxima, marca, peso):   #Constructor de la clase Camion
        Auto.__init__(self, color, velocidadMaxima, marca) #Constructor de la clase padre: Auto
        self.peso = peso  #Colocamos el atributo que difiere entre Camion y Auto
        
    def muestraEstado(self):
        print(f'Camion marca = {self.marca}, Color = {self.color}, Velocidad Maxima = {self.velocidadMaxima}, Peso = {self.peso}')   
        
        
        
# Instanciar objetos de las clases Moto y Camion

MotoYamaha = Moto('Rojo',200,'Yamaha','Scooter') 

CamionIsuzu = Camion('Blanco',120,'Isuzu','1 Tonelada')   


# Llamar a los metodos para la MotoYamaha 

MotoYamaha.arrancar()
MotoYamaha.acelerar()  
MotoYamaha.acelerar()  
MotoYamaha.frenar()
MotoYamaha.muestraEstado()
print("\n")
print("*"*80)


# Llamar a los metodos para el camion Isuzu

CamionIsuzu.arrancar()
CamionIsuzu.acelerar()
CamionIsuzu.acelerar()
CamionIsuzu.frenar()
CamionIsuzu.muestraEstado()
print("\n")
print("*"*80)
          