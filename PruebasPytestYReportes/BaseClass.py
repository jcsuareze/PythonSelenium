import logging

class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("../logFile2.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        print("Mensaje desde Baseclass,  el nivel se encuentra en INFO")
        return logger
