import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample:

    def test_editarPerfil(self, dataLoad):
        print(dataLoad)
        print(dataLoad[2])



