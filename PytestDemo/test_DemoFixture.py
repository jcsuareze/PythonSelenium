import pytest
'''
@pytest.fixture()
def setUp():
    print("\nSe ejecuta siempre antes de cada prueba")
    yield
    print("\nSe ejecuta siempre despues de cada prueba\n")


'''
#pasamos el fixture como parametro

def test_demo1(setUp):
    print("Esta es la ejecucion de la prueba test_demo1, su estatus es:")

@pytest.mark.xfail
def test_demo2(setUp):
    print("Esta es la ejecucion de la prueba test_demo2, su estatus es:")


