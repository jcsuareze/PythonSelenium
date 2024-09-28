import pytest

from PruebasPytestYReportes.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample(BaseClass):

    def test_editarPerfil(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])#metodo heredado de BaseClass
        log.info((dataLoad[2]))
        #diferencia entre log y print
        print(dataLoad[2])



