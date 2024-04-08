class Articulo():
    def __init__(self,desc,cantidad,coste):
        self.desc = desc
        self.cantidad = cantidad
        self.coste = coste
        self.venta = self.coste * self.cantidad
        
    def __str__(self):
       return  f"Precio {self.desc} = {self.coste} -- Cantidad de {self.desc} X {self.cantidad} "
            
    def vender(self,unidades_v):
        self.cantidad = self.cantidad - unidades_v 
        
        return F"Unidades vendidas = {unidades_v} - Ganacia = {self.coste * unidades_v}" 
    
    def dar_cantidad(self):
        return f"Tenemos disponibles = {self.cantidad} {self.desc}"  
       

miCompra = Articulo("Laptop",5,1000)   
print(miCompra)   

print("\n")
print("*"*80)


print(miCompra.vender(2))
print(miCompra.dar_cantidad())

class ArticulosOficina(Articulo):
    def __init__(self,desc,cantidad,coste):
        self.desc = desc
        self.cantidad = cantidad
        self.coste = coste
        self.venta = self.coste * self.cantidad
    def __str__(self):
        return f"Creado {self.desc}, {self.cantidad} con precio de {self.coste}"  
    def devolver(self, unidades):
        self.cantidad = self.cantidad + unidades
        return f"Se han devuelto {unidades} de {self.desc} - Valor de devolucion = {self.coste * unidades}"
 
print("\n")
print("*"*80)    
folder = ArticulosOficina("Folder",20,0.50)  
print(folder)  
print(folder.dar_cantidad()) 
print(folder.vender(11)) 
print(folder.dar_cantidad())
print(folder.devolver(2))
print(folder.dar_cantidad())
        
   