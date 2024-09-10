#Diccionarios
#Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben con llaves y tienen claves y valores.
#Ejemplo
#Crear un diccionario:

thisDict = { "marca": "Ford", "modelo": "Mustang", "año": 1964 }
print(thisDict)

#Acceder a un elemento
#Se puede acceder a los elementos de un diccionario haciendo referencia a su clave, entre corchetes:
#Ejemplo
#Obtener el valor de la clave "modelo":

x = thisDict["modelo"]
print(x)

#Cambiar valores
#Se puede cambiar el valor de un elemento específico haciendo referencia a su clave:
#Ejemplo
#Cambiar el año a 2018:

thisDict["año"] = 2018
print(thisDict)

#También se puede usar el método get() para acceder a los valores de las claves:
#Ejemplo
#Obtener el valor de la clave "modelo":

x = thisDict.get("modelo")
print(x)

print(thisDict.keys())
print(thisDict.values())
print(thisDict.items())


#Añadir elementos

#Se puede añadir un elemento nuevo a un diccionario especificando una nueva clave y un valor:
#Ejemplo
#Añadir una nueva clave "color" con el valor "rojo":

thisDict["color"] = "rojo"
print(thisDict)


