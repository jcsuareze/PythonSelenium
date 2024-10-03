import pytest

#Explicacion en Pytest Demo folder
@pytest.fixture()
def dataLoad():
    print("Datos del usuario siendo creados.. Mensaje desde Conftest de Pruebas Y reportes.")
    return("Juan Carlos","Suárez", "juan.suarez@my.unitec.edu.mx")

@pytest.fixture(params=("Chrome", "Edge", "Firefox"))
def seleccionaBrowser(request):
    return request.param
