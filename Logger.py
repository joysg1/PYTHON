import logging
logging.basicConfig(level = logging.DEBUG, format =' %(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Con level se establece el nivel de registro, que puede ser
# debug, info, warning, error y critical

# Solo se registran los mensajes con un nivel igual o superior al
# especificado 

# asctime permite incluir fecha y hora

# name permite definir el nombre del logger

# levelname permite definir el nivel

# message permite definir el mensaje


# Creacion de un objeto logger 

logger = logging.getLogger(__name__)

# El atributo __name__ tiene dos guiones bajos para asegurar 
# que el logger tenga un nombre unico basado en el modulo actual


# Ahora usaremos el logger para registrar mensajes 

# utilizando metodos de logger como logger.debug 
# logger.warning - logger.info - logger.error  o logger.critical 


# Ejemplo de un mensaje de nivel info 


logger.info("Este es un mensaje de informacion")


# Ejemplo de un mensaje de debug

logger.debug("Este es un mensaje de depuracion")

# Ejemplo de un mensaje de warning

logger.warning("Este es un mensaje de advertencia")

# Ejemplo de un mensaje de criticidad

logger.critical("Este es un mensaje de criticidad")

# Ejemplo de un mensaje de error

logger.error("Este es un mensaje de error")


