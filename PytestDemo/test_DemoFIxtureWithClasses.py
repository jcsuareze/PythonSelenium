import pytest

#Aqui usaremos una clase y el valor  useFixtures() a nivel de clase
#Se debe definir el conftest para que el fixture tenga nivel de clase y tome estas pruebas
#ejemplo de conf en confTest.py   @pytest.fixture(scope="class")

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("Se ejecutan los pasos dentro del metodo fixtureDemo1")

    def test_fixtureDemo2(self):
        print("Se ejecutan los pasos dentro del metodo fixtureDemo2")

    def test_fixtureDemo3(self):
        print("Se ejecutan los pasos dentro del metodo fixtureDemo3")

    def test_fixtureDemo4(self):
        print("Se ejecutan los pasos dentro del metodo fixtureDemo4")