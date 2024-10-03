import logging

import pytest


@pytest.mark.skip
def test_logging():

    logger = logging.getLogger(__name__)


    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #El FileHandler nos permite estabblecer la ruta y nombre del archivo donde sera guardada la informacion del log
    fileHandler = logging.FileHandler("../logFile.log")
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.INFO)


    logger.addHandler(fileHandler) #fileHandler

    logger.debug("Una declaracion debug ha sido ejecutada")

    logger.info("Una declaracion de informacion")

    logger.warning("Una declaracion de advertencia")

    logger.error("Una declaracion de error")

    logger.critical("una declaracion critica")