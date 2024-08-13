import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# crear base de datos 
db = cliente["ventas"]

# crear coleccion
coleccion = db["articulos"]

# insertar datos
articulo1 = {"nombre": "Laptop", "precio": 800, "cantidad": 10}
articulo2 = {"nombre": "Mouse", "precio": 20, "cantidad": 50}
articulo3 = {"nombre": "Teclado", "precio": 15, "cantidad": 30}

# insertar documentos en la coleccion
articulos = [articulo1, articulo2,articulo3]
coleccion.insert_many(articulos)

# Listado de colecciones
colecciones = db.list_collection_names()
print("Colecciones en la base de datos:")
for col in colecciones:
    print(col)


# Listado de documentos
documentos = coleccion.find()
print("\nDocumentos en la colección:")
for doc in documentos:
    print(doc)

# Edicion

# Actualizar un documento
filtro = {"nombre": "Laptop"}
nuevo_valor = {"$set": {"precio": 850}}
coleccion.update_one(filtro, nuevo_valor)

# Eliminar un documento
filtro = {"nombre": "Mouse"}
coleccion.delete_one(filtro)




