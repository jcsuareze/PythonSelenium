import logging

logger = logging.getLogger(__name__)

#El FileHandler nos permite estabblecer la ruta y nombre del archivo donde sera guardada la informacion del log
fileHandler = logging.FileHandler("../logFile.log")



logger.addHandler(fileHandler) #fileHandler

logger.debug("Una declaracion debug ha sido ejecutada")

logger.info("Una declaracion de informacion")

logger.warning("Una declaracion de advertencia")

logger.error("Una declaracion de error")

logger.critical("una declaracion critica")