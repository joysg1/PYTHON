#pip install faker

from faker import Faker





def crear_datos(cantidad):
    datos = {}  
    datos_ficticios = Faker()

    for i in range(cantidad):
     nombre = datos_ficticios.name()
     direccion = datos_ficticios.address()
     datos[nombre]=direccion
 
    return datos    

if __name__=='__main__':
    print(crear_datos(3))
   
#Video 95 min 8.15 
    