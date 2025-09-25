import wikipedia

def buscar_en_wikipedia():
    idiomas = {
        '1': 'es',
        '2': 'en'
    }
    
    while True:
        termino_de_busqueda = input("Ingrese el término de búsqueda (o 'salir' para terminar): ")
        
        if termino_de_busqueda.lower() == 'salir':
            break
        
        print("Seleccione un idioma:")
        print("1. Español")
        print("2. Inglés")
        
        opcion_idioma = input("Ingrese el número del idioma: ")
        
        if opcion_idioma not in idiomas:
            print("Idioma no soportado. Por defecto se utilizará inglés.")
            wikipedia.set_lang('en')
        else:
            wikipedia.set_lang(idiomas[opcion_idioma])
        
        try:
            resumen = wikipedia.summary(termino_de_busqueda)
            print(resumen)
            print("\n------------------------\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Se encontraron varias páginas para '{termino_de_busqueda}'. Por favor, especifique más.")
            print("Opciones:")
            for opcion in e.options:
                print(opcion)
        except wikipedia.exceptions.PageError:
            print(f"No se encontró ninguna página para '{termino_de_busqueda}'.")

if __name__ == "__main__":
    buscar_en_wikipedia()

