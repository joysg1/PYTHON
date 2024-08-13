import pymongo
# conexion
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# bd
db = cliente["ventas"]

# coleccion
coleccion = db["articulos"]

while True:
    print("*"*80)
    print("\t\t\t Menu principal ")
    print("1. Listar articulos")
    print("2. Agregar articulos")
    print("3. Editar articulos")
    print("4. Eliminar articulos")
    print("5. Salir")
    print("*"*80)
    print("\n")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        documentos = coleccion.find()
        print("\nDocumentos en la colección:")
        for doc in documentos:
            print(doc)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del articulo: ")
        precio = float(input("Ingrese el precio del articulo: "))
        cantidad = int(input("Ingrese la cantidad del articulo: "))
        coleccion.insert_one({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print("Articulo agregado correctamente.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del articulo a editar: ")
        filtro = {"nombre": nombre}
        nuevo_nombre = input("Ingrese el nuevo nombre del articulo: ")
        nuevo_precio = float(input("Ingrese el nuevo precio del articulo: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad del articulo: "))
        nuevos_valores = {"$set": {"nombre": nuevo_nombre, "precio": nuevo_precio, "cantidad": nueva_cantidad}}
        coleccion.update_one(filtro, nuevos_valores)
        print("Articulo editado correctamente.")
       
    elif opcion == "4":
        nombre = input("Ingrese el nombre del articulo a eliminar: ")
        filtro = {"nombre": nombre}
        coleccion.delete_one(filtro)
        print("Articulo eliminado correctamente.")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")


