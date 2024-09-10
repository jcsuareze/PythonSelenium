
texto = "Hola, bienvenidos a Python"
print("El texto es: " + texto)
print("Este es un ejemplo de interpolación de cadenas: %s" % texto)
print("Este es un ejemplo de interpolación de cadenas: {}".format(texto))

# Ejemplos de indexación
print("El primer caracter es: " + texto[0])
print("El último caracter es: " + texto[-1])
print("Los primeros 5 caracteres son: " + texto[0:5])
print("Los últimos 5 caracteres son: " + texto[-6:])
print("Los caracteres en posiciones pares son: " + texto[::2])
print("Los caracteres en posiciones impares son: " + texto[1::2])
print("El texto en reversa es: " + texto[::-1])

#Saltos de línea
print("\n\n\n*******FUNCIONES DE CADENAS*******\n\n\n")

# Ejemplos de funciones de cadenas
print("El texto en mayúsculas es: " + texto.upper())
print("El texto en minúsculas es: " + texto.lower())
print("El texto en formato título es: " + texto.title())
print("El texto en formato de capitalización es: " + texto.capitalize())
print("El texto en formato de swapcase es: " + texto.swapcase())
print("El texto en formato de justificado a la izquierda es: " + texto.ljust(100))
print("El texto en formato de justificado a la derecha es: " + texto.rjust(100))
print("El texto en formato de justificado al centro es: " + texto.center(100))

# Ejemplos de búsqueda
print("El texto contiene la palabra 'Python'?: " + str("Python" in texto))
print("El texto NO contiene la palabra 'Python'?: " + str("Python" not in texto))

# Ejemplos de búsqueda
print("El texto contiene la palabra 'Python'?: " + str(texto.find("Python")))
print("El texto NO contiene la palabra 'Python'?: " + str(texto.rfind("Python")))
print("'?: " + str(texto.index("Python")))
print("El texto NO contiene la palabra 'Python'?: " + str(texto.rindex("Python")))
print("Cuantas veces contiene la palabra 'Python'?: " + str(texto.count("Python")))

# Ejemplos de reemplazo
print("El texto reemplazando 'Python' por 'Java' es: " + texto.replace("Python", "Java"))
print("El texto reemplazando 'Python' por 'Java' 2 veces es: " + texto.replace("Python", "Java", 2))

# Ejemplos de separación
print("El texto separadas letras por comas  incluyendo espacios es: " + ",".join(texto))
print("El texto separado palabras  por comas incluyendo espacios es: " + ",".join(texto.split()))



nom = "Juan Carlos"
ape ="Suárez"
ame = "Estrada"

print("Mi nombre completo es: %s %s %s" % (nom, ape, ame))
print("Mi nombre completo es: {} {} {}".format(nom, ape, ame))
print("Mi nombre completo es: {0} {1} {2}".format(nom, ape, ame))
print("Mi nombre completo es: {2} {1} {0}".format(nom, ape, ame))
print("Mi nombre completo es: {n} {a} {a}".format(n=nom, a=ape, m=ame))
print(f"Mi nombre completo es: {nom} {ape} {ame}")
print(f"Mi nombre completo es: {nom} {ape} {ame}".upper())
print(f"Mi nombre completo es: {nom} {ape} {ame}".lower())
print(f"Mi nombre completo es: {nom} {ape} {ame}".title())
