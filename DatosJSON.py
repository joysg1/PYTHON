import json
from urllib import request

url = "https://my.api.mockaroo.com/personas.json?key=ac55e430"
respuesta = request.urlopen(url)
# print(respuesta)

contenido = respuesta.read()
# print(contenido)

json_obtenido = json.loads(contenido.decode('utf-8'))

# print(json_obtenido)

for persona in json_obtenido:
    print(persona)
    print("\n")
    
    
for persona in json_obtenido:
    print("*****************************")
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellidos']}")
    print(f"Email: {persona['email']}")
    print("*****************************")
    print("\n")    