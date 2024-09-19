#Para heredar en python se utiliza la palabra clave "class" seguida del nombre de la clase
# y el nombre de la clase de la que se hereda entre parentesis "()"
#se importa la clase de la que se quiere heredar y se pasa como argumento en la definicion de la clase
from PythonBasics.DemoConstructorYSelf import Calculadora2
#la sintaxis para heredar para importar una clase es la siguiente:
#class Child(Parent):
#se puede heredar de una clase que a su vez hereda de otra clase

class Child(Calculadora2):
    num2 = 200
    #se pueden llamar ahora los metodos sin necesidad de crear un objeto de la clase padre
    #se puede sobreescribir un metodo de la clase pad
    def getCompleteData(self):
        print("Metodo de la clase hija")
        return self.primerNumero + self.segundoNumero + Calculadora2.num + Child.num2

#El constructor de la clase padre se llama automaticamente cuando se crea un objeto de la clase hija
object = Child(10, 20)
print(object.getCompleteData())
