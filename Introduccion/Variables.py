#Introduccion a las variables
#Las variables en Python son una referencia a un objeto, no es necesario declarar el tipo de variable
#Las variables en Python son case-sensitive (sensible a mayúsculas y minúsculas) y no se pueden declarar con palabras reservadas

a = 5
A = 10
print(a)
print(A)

b = 20
suma = a + b


print("La suma es", suma) #La coma se utiliza para concatenar texto con variables

print("La suma es", str(suma)) #La función str() convierte un número en una cadena de texto

#Las variables en Python se pueden declarar en una sola línea
x, y, z = 15, 210, 15
print(a)
print(b)

resta = a - b
multiplicacion = a * b
division = b / a
division_entera = b // a
modulo = b % a
exponente = a ** 2

print("La resta es", resta)
print("La multiplicación es", multiplicacion)
print("La división es", division)
print("La división entera es", division_entera)
print("El módulo es", modulo)
print("El exponente es", exponente)


nombre = ""
nombre = "Juan"
print(nombre)

#usanndo comillas simples
nombre = 'Juan'
print(nombre)

#usando comillas triples
nombre = '''Juan'''
print(nombre)

#usando f-string
nombre = f"Juan"
print(nombre)

print(type(nombre)) #La función type() devuelve el tipo de variable