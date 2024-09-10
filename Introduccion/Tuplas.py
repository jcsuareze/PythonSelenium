#tuplas
#Las tuplas son una estructura de datos que permite almacenar colecciones de datos inmutables.
#Una tupla es una colección de objetos que no puede modificarse (es inmutable).

#Las tuplas son similares a las listas, pero con la diferencia de que no se pueden modificar una vez creadas.
#Las tuplas se crean utilizando paréntesis en lugar de corchetes.
#Ejemplo
#Crear una tupla:
#
tupla = ("manzana", "plátano", "cereza")
print(tupla)
#Acceder a los elementos de una tupla
#Se puede acceder a los elementos de una tupla haciendo referencia a su índice, entre corchetes.
#Ejemplo
#Imprimir el segundo elemento de la tupla:

print(tupla[1])
#Modificar una tupla
#Las tuplas son inmutables, lo que significa que no se pueden cambiar una vez creadas.

#Pero hay una solución. Se pueden convertir la tupla en una lista, cambiar la lista y convertirla de nuevo en una tupla.
#Ejemplo
#Convertir la tupla en una lista para poder cambiarla:

x = list(tupla)
x[1] = "kiwi"
tupla = tuple(x)
print(tupla)
#La longitud de una tupla
#Para determinar cuántos elementos tiene una tupla, se puede utilizar la función len().
#Ejemplo
#Imprimir la longitud de la tupla:

print(len(tupla))




