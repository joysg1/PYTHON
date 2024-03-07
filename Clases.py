# Las clases son plantillas para instanciar objetos con sus atributos y
# metodos

# Creacion de la clase
class Auto:
    def __init__(self, color, velocidadMaxima, marca): #Metodo constructor
        self.color = color
        self.velocidadMaxima = velocidadMaxima
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