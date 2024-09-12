#Funciones
#Las funciones son bloques de código que se pueden ejecutar múltiples veces, con la posibilidad de recibir parámetros que pueden modificar su comportamiento.
#Las funciones se definen con la palabra clave def seguida del nombre de la función y paréntesis que pueden contener los parámetros de la función.
#Las funciones pueden devolver un valor con la palabra clave return, aunque no es obligatorio.

#Ejemplo de función sin argumentos
def saludar():
    print("Hola, bienvenido a Python")

saludar()

#Ejemplo de función con argumentos
def saludar(nombre):
    print(f"Hola, funcion con un argumento {nombre}")

saludar("Juan")

#Ejemplo de función con 2 argumentos
def saludar(nombre, apellido):
    print(f"Hola, funcion con 2 argumentos {nombre} {apellido}")

saludar("Juan", "Suárez")

#Ejemplo de función con argumgumentos de tipo lista
def saludar(nombres):
    for nombre in nombres:
        print(f"Hola, funcion con argumentos tipo lista {nombre}")

nombres = ["Juan", "Pedro", "María"]
saludar(nombres)

#Ejemplo de función con argumentos de tipo diccionario
def saludar(persona):
    print(f"Hola, funcion con argumentos tipo diccionario {persona['nombre']} {persona['apellido']}")

persona = {"nombre": "Juan", "apellido": "Suárez"}
saludar(persona)

#Ejemplo de función con argumentos por defecto
def saludar(nombre="Juan"):
    print(f"Hola, funcion con argumento por defecto {nombre}")

saludar()

#Ejemplo de función numero variable de argumentos
def saludar(*nombres):
    for nombre in nombres:
        print(f"Hola, funcion con argumentos diferentes {nombre}")

saludar("Juan", "Pedro", "María")

#Ejemplo 2 de funcion numero variable de argumentos
def sumar(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print(resultado)

#Ejemplo de función con argumentos de tipo clave-valor
def saludar(**persona):
    print(f"Hola, funcion con argumentos clave-valor {persona['nombre']} {persona['apellido']}")

saludar(nombre="Juan", apellido="Suárez")








