import pytest
#Este archivo es leido en tiempo de ejecucion por parte de todos los archivos Test_  dentro de la misma carpeta
#Lo que hará que se ejecuten las caracteristicas dentro del fixture

@pytest.fixture(scope = "class")
def setUp(setUp):
    print("\nSe ejecuta siempre antes de cada prueba")
    yield
    print("\nSe ejecuta siempre despues de cada prueba\n")
