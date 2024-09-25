#Cualquier archivo de prueba debe comenzar con test_ o termine con _test.py
#Para ejecutar la suite de pruebas se debe de ejecutar el comando py.test -v -s
#mientras se encuentre dentro de la carpeta donde se encuentran los archivos de prueba
import pytest
 #Se pueden marcar las pruebas con un tag para poder ejecutarlas de manera independiente
    #pytest -v -s -m smoke test_demo2.py
    #pytest -v -s -m "not smoke" test_demo2.py

#Se pueden saltar las pruebas con el decorador skip
    #pytest -v -s -m smoke test_demo2.py
    #pytest -v -s -m "not smoke" test_demo2.py
    #pytest -v -s -k test_firstProgram test_demo2.py
    #pytest -v -s -k test_SecondProgram test_demo2.py

#Se pueden saltar los reportes de las pruebas con el decorador xfail
    #pytest -v -s -m smoke test_demo2.py
    #pytest -v -s -m "not smoke" test_demo2.py
    #pytest -v -s -k test_firstProgram test_demo2.py
    #pytest -v -s -k test_SecondProgram test_demo2.py


#Las pruebas deben de ser funciones que comiencen con test
#def test_firstProgram():
#    print("Hello")

@pytest.mark.skip
def test_firstProgram():
    print("No Se ejecuta la prueba sin fixtures en conftest")
    message = "Hello"
    assert message == "Hi", "Test failed because strings do not match"

@pytest.mark.smoke
def test_SecondProgram(setUp):
    print("Se ejecuta la prueba con fixtures en conftest")
    a=4
    b=5
    assert a+1 == b, "Test failed because a+1 is not equal to b"


