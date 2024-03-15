import logging
logging.basicConfig(filename = 'mi_registro.log' , level = logging.DEBUG, format =' %(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Creacion de un objeto logger 

logger = logging.getLogger(__name__)


# Registro de mensaje

logger.debug("Este mensaje se guardara en archivo")
logger.info("Este mensaje se guardara en archivo")


