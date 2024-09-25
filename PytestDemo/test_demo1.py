#Cualquier archivo de prueba debe comenzar con test_ o termine con _test.py
#pytest -v -s test_demo1.py
#Para ejecutar una prueba en especifico se debe de ejecutar el comando pytest -k test_firstProgram -v -s
import pytest


#Las pruebas deben de ser funciones que comiencen con test
#def test_firstProgram():
#    print("Hello")

@pytest.mark.smoke
def test_firstProgram():
   print("Hello")

def test_SecondProgram():
    print("Good Morning")
