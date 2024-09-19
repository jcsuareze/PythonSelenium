#En python, una funcion
#es un bloque de codigo que solo se ejecuta cuando se llama.

#Para declarar una funcion se utiliza la palabra clave "def" seguida del nombre de la funcion y parentesis "()"

def saludo():
    print("Buenos dias")

#Para llamar a una funcion se utiliza el nombre de la funcion seguido de parentesis "()"
saludo()

#En python, una funcion puede recibir parametros (argumentos) y devolver un valor
def saludoConNombre(nombre):
    print(f"Buenos dias {nombre}")
    print("Buenos dias " + nombre)

saludoConNombre("Juan")

#En python, una funcion puede recibir parametros (argumentos) y devolver un valor
def sumaEnteros(a, b) -> float:
    return a + b

resultado = sumaEnteros(10, 20)
print(resultado)
print(type(resultado))



