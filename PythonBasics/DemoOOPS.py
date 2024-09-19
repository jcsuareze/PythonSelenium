#Las Clases son un tipo de estructura de datos que permite encapsular datos y funciones en un solo objeto.
#Las clases son una plantilla para crear objetos. Un objeto es una instancia de una clase.

#En Python, una clase se define utilizando la palabra clave "class" seguida del nombre de la clase.
#Por convencion, el nombre de la clase comienza con una letra mayuscula.

class Calculadora:

    num = 100 #variable de clase
    
    def getDatos(self): #metodo de instancia
        print("Metodo de la clase")

#Con la indentacion se define el alcance de la clase
#Para crear un objeto de una clase, se utiliza el nombre de la clase seguido de parentesis "()"
#Para acceder a los atributos y metodos de un objeto, se utiliza el operador punto "."

obj = Calculadora()
obj.getDatos()
print(obj.num)





