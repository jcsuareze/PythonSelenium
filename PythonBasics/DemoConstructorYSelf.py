
class Calculadora2:
    num = 100 #variable de clase

    #Un constructor es un metodo especial que se llama automaticamente cuando se crea un objeto de una clase.
    #En Python, el constructor se define utilizando el metodo __init__()
    #El constructor siempre toma como primer argumento una referencia al objeto actual "self"
    #constructor por defecto
    '''def __init__(self):
        print("Constructor por defecto y se llama automaticamente cuando se crea un objeto de la clase")'''

    def __init__(self, a, b):
        print("Constructor con parametros, se llama automaticamente cuando se crea un objeto de la clase")
        self.primerNumero = a #variable de instancia
        self.segundoNumero = b #variable de instancia

    def getDatos(self): #metodo de instancia
        print("Metodo de la clase")

    #Self es una referencia al objeto actual y es obligatorio incluirlo en la definicion de un metodo de instancia
    #En Python no se puede sobrecargar metodos y constructores
    #Tampoco llamar variables de instancia directamente, se deben llamar a traves de self o nombre de la clase
    def sumaEnteros(self):
        return self.primerNumero + self.segundoNumero + Calculadora2.num

obj = Calculadora2(10, 20)
print(obj.sumaEnteros())


