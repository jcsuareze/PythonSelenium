import pytest



class TestExample3:
#Toma los valores de conftest.py y el fixture seleccionaBrowser
   def test_crossBrowser(self, seleccionaBrowser):
       print(seleccionaBrowser)
