from gtts import gTTS
import io
import pygame
import os
from datetime import datetime

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal"""
    print("=" * 50)
    print("        SISTEMA DE TEXTO A VOZ")
    print("=" * 50)
    print("1. Configurar voz y mensaje")
    print("2. Reproducir último mensaje")
    print("3. Salir")
    print("=" * 50)

def mostrar_menu_idioma():
    """Muestra el menú de selección de idioma"""
    print("\n--- SELECCIONAR IDIOMA ---")
    print("1. Español")
    print("2. Inglés")
    return input("Elige una opción (1-2): ")

def mostrar_menu_genero():
    """Muestra el menú de selección de género de voz"""
    print("\n--- SELECCIONAR TIPO DE VOZ ---")
    print("1. Voz Femenina")
    print("2. Voz Masculina")
    return input("Elige una opción (1-2): ")

def obtener_saludo(idioma, genero):
    """
    Genera un saludo personalizado según la hora del día, idioma y género
    
    Args:
        idioma (str): 'es' para español, 'en' para inglés
        genero (str): '1' para femenino, '2' para masculino
    
    Returns:
        str: Saludo personalizado
    """
    hora_actual = datetime.now().hour
    
    if idioma == 'es':
        # Determinar momento del día en español
        if 5 <= hora_actual < 12:
            momento = "buenos días"
        elif 12 <= hora_actual < 19:
            momento = "buenas tardes"
        else:
            momento = "buenas noches"
        
        # El saludo es igual para ambos géneros en español
        return f"Hola, {momento}. ¿Qué desea?"
    
    else:  # Inglés
        # Determinar momento del día en inglés
        if 5 <= hora_actual < 12:
            momento = "good morning"
        elif 12 <= hora_actual < 19:
            momento = "good afternoon"
        else:
            momento = "good evening"
        
        # El saludo es igual para ambos géneros en inglés
        return f"Hello, {momento}. What would you like?"

def reproducir_saludo(codigo_idioma, genero):
    """
    Reproduce el saludo personalizado
    
    Args:
        codigo_idioma (str): Código del idioma para gTTS
        genero (str): Género de la voz ('1' femenino, '2' masculino)
    """
    # Inicializar pygame si no está inicializado
    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    
    try:
        saludo = obtener_saludo(codigo_idioma, genero)
        print(f"Saludo: {saludo}")
        print("Reproduciendo saludo...")
        
        tts_saludo = gTTS(text=saludo, lang=codigo_idioma)
        fp_saludo = io.BytesIO()
        tts_saludo.write_to_fp(fp_saludo)
        fp_saludo.seek(0)
        
        pygame.mixer.music.load(fp_saludo)
        pygame.mixer.music.play()
        
        # Esperar a que termine la reproducción
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        print("Saludo completado.")
        
    except Exception as e:
        print(f"Error al reproducir saludo: {e}")

def obtener_fecha_formateada(idioma, genero):
    """
    Obtiene la fecha actual formateada según el idioma y género
    
    Args:
        idioma (str): 'es' para español, 'en' para inglés
        genero (str): '1' para femenino, '2' para masculino
    
    Returns:
        str: Fecha formateada con el mensaje apropiado
    """
    fecha_actual = datetime.now()
    
    if idioma == 'es':
        # Formatear fecha en español
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        dias_semana = [
            "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
        ]
        
        dia_semana = dias_semana[fecha_actual.weekday()]
        dia = fecha_actual.day
        mes = meses[fecha_actual.month - 1]
        año = fecha_actual.year
        hora = fecha_actual.strftime("%H:%M")
        
        if genero == "1":  # Femenino
            return f"Programa ejecutado el {dia_semana} {dia} de {mes} de {año} a las {hora}"
        else:  # Masculino
            return f"Programa ejecutado el {dia_semana} {dia} de {mes} de {año} a las {hora}"
    
    else:  # Inglés
        # Formatear fecha en inglés
        fecha_formateada = fecha_actual.strftime("%A, %B %d, %Y at %I:%M %p")
        
        if genero == "1":  # Femenino
            return f"Program executed on {fecha_formateada}"
        else:  # Masculino
            return f"Program executed on {fecha_formateada}"

def obtener_codigo_idioma(opcion_idioma, opcion_genero):
    """
    Obtiene el código de idioma para gTTS basado en las selecciones
    
    Args:
        opcion_idioma (str): Opción de idioma seleccionada
        opcion_genero (str): Opción de género seleccionada
    
    Returns:
        tuple: (código_idioma, descripción)
    """
    if opcion_idioma == "1":  # Español
        if opcion_genero == "1":  # Femenina
            return "es", "Español - Voz Femenina", "1"
        else:  # Masculina
            return "es", "Español - Voz Masculina", "2"
    else:  # Inglés
        if opcion_genero == "1":  # Femenina
            return "en", "Inglés - Voz Femenina", "1"
        else:  # Masculina
            return "en", "Inglés - Voz Masculina", "2"

def texto_a_voz_con_fecha(texto, codigo_idioma, genero):
    """
    Convierte texto a voz, reproduce el mensaje y luego dice la fecha de ejecución.
    
    Args:
        texto (str): El texto que se quiere convertir a voz
        codigo_idioma (str): Código del idioma para gTTS
        genero (str): Género de la voz ('1' femenino, '2' masculino)
    """
    # Inicializar pygame si no está inicializado
    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    
    try:
        # Reproducir mensaje principal
        print("Generando audio del mensaje...")
        tts_mensaje = gTTS(text=texto, lang=codigo_idioma)
        fp_mensaje = io.BytesIO()
        tts_mensaje.write_to_fp(fp_mensaje)
        fp_mensaje.seek(0)
        
        pygame.mixer.music.load(fp_mensaje)
        print("Reproduciendo mensaje...")
        pygame.mixer.music.play()
        
        # Esperar a que termine la reproducción del mensaje
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Pequeña pausa entre mensajes
        pygame.time.wait(500)
        
        # Obtener y reproducir fecha
        fecha_texto = obtener_fecha_formateada(codigo_idioma, genero)
        print("Generando audio de la fecha...")
        tts_fecha = gTTS(text=fecha_texto, lang=codigo_idioma)
        fp_fecha = io.BytesIO()
        tts_fecha.write_to_fp(fp_fecha)
        fp_fecha.seek(0)
        
        pygame.mixer.music.load(fp_fecha)
        print("Reproduciendo fecha de ejecución...")
        pygame.mixer.music.play()
        
        # Esperar a que termine la reproducción de la fecha
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        print("Reproducción completada.")
        
    except Exception as e:
        print(f"Error al convertir texto a voz: {e}")

def texto_a_voz(texto, codigo_idioma):
    """
    Convierte texto a voz y lo reproduce usando pygame.
    
    Args:
        texto (str): El texto que se quiere convertir a voz
        codigo_idioma (str): Código del idioma para gTTS
    """
    # Inicializar pygame si no está inicializado
    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    
    try:
        print("Generando audio...")
        # Crear el objeto gTTS
        tts = gTTS(text=texto, lang=codigo_idioma)
        
        # Crear buffer en memoria
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        # Cargar y reproducir el audio
        pygame.mixer.music.load(fp)
        print("Reproduciendo...")
        pygame.mixer.music.play()
        
        # Esperar a que termine la reproducción
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        print("Reproducción completada.")
        
    except Exception as e:
        print(f"Error al convertir texto a voz: {e}")

def configurar_y_reproducir():
    """Función para configurar la voz y reproducir el mensaje"""
    
    # Selección de idioma
    while True:
        opcion_idioma = mostrar_menu_idioma()
        if opcion_idioma in ["1", "2"]:
            break
        print("Opción inválida. Por favor, elige 1 o 2.")
    
    # Selección de género
    while True:
        opcion_genero = mostrar_menu_genero()
        if opcion_genero in ["1", "2"]:
            break
        print("Opción inválida. Por favor, elige 1 o 2.")
    
    # Obtener código de idioma
    codigo_idioma, descripcion, genero = obtener_codigo_idioma(opcion_idioma, opcion_genero)
    
    # Mostrar configuración y reproducir saludo
    print(f"\n--- CONFIGURACIÓN SELECCIONADA ---")
    print(f"Tipo de voz: {descripcion}")
    print("\n--- SALUDO DE BIENVENIDA ---")
    
    # Reproducir saludo personalizado
    reproducir_saludo(codigo_idioma, genero)
    
    print("\nNota: gTTS no diferencia entre voces masculinas y femeninas,")
    print("pero puedes ajustar el texto para que suene más natural.")
    print("Después de cada mensaje se reproducirá la fecha de ejecución.")
    
    mensaje = input("\nEscribe el mensaje a reproducir: ")
    
    if mensaje.strip():
        # Guardar configuración para reutilizar
        return mensaje, codigo_idioma, descripcion, genero
    else:
        print("No se ingresó ningún mensaje.")
        return None, None, None, None

def main():
    """Función principal del programa"""
    ultimo_mensaje = None
    ultimo_codigo = None
    ultima_descripcion = None
    ultimo_genero = None
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            resultado = configurar_y_reproducir()
            if resultado[0]:  # Si se configuró correctamente
                ultimo_mensaje, ultimo_codigo, ultima_descripcion, ultimo_genero = resultado
                print("\nReproduciendo mensaje con fecha...")
                texto_a_voz_con_fecha(ultimo_mensaje, ultimo_codigo, ultimo_genero)
                input("\nPresiona Enter para continuar...")
            else:
                input("\nPresiona Enter para continuar...")
                
        elif opcion == "2":
            if ultimo_mensaje and ultimo_codigo:
                print(f"\nÚltima configuración: {ultima_descripcion}")
                print(f"Mensaje: {ultimo_mensaje}")
                print("\nReproduciendo mensaje con fecha...")
                texto_a_voz_con_fecha(ultimo_mensaje, ultimo_codigo, ultimo_genero)
                input("\nPresiona Enter para continuar...")
            else:
                print("\nNo hay ningún mensaje configurado.")
                print("Por favor, usa la opción 1 primero.")
                input("\nPresiona Enter para continuar...")
                
        elif opcion == "3":
            print("\n¡Gracias por usar el sistema de texto a voz!")
            break
            
        else:
            print("\nOpción inválida. Por favor, elige una opción del 1 al 3.")
            input("Presiona Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()