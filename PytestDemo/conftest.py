import pytest
#Este archivo es leido en tiempo de ejecucion por parte de todos los archivos Test_  dentro de la misma carpeta
#Lo que hará que se ejecuten las caracteristicas dentro del fixture

#@pytest.fixture(scope = "class")
def setUp(setUp):
    print("\nSe ejecuta siempre antes de cada prueba")
    yield
    print("\nSe ejecuta siempre despues de cada prueba\n")




#Es posible cargar datos desde el conftest para enviarlos a las pruebas con los fixtures
#definimos nuestra fixture
@pytest.fixture()
def dataLoad():
    print("Datos del usuario siendo creados...")
    #vamos a crear una tupla  ( recordatorio:  las tuplas no se pueden modificar )
    return("Juan Carlos","Suárez", "juan.suarez@my.unitec.edu.mx")

#Trabaja de forma similar a DataProvider de TestNg,  se guardan los datos en params,  que a su vez los manda como
#un objeto al argumento a la variable request que a su vez puede devolverlo a travez del objeto request
@pytest.fixture(params=("Chrome", "Edge", "Firefox"))
def seleccionaBrowser(request):
    return request.param

