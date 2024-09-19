#Para abrir un archivo se usa la función open() y para cerrarlo se usa la función close()
#Para leer un archivo se usa la función read()
#Para escribir en un archivo se usa la función write()
#Para leer un archivo línea por línea se usa la función readline()
#Para escribir en un archivo línea por línea se usa la función writelines()
#Para leer un archivo línea por línea se usa la función readlines()

#Abrir un archivo
file = open("../notas.txt", "r")
print(file.read())
print(file.readline())


#Cuando se abre un archivo, hay que asegurarse de cerrarlo
file.close()
print("*****"*20)
with open("../notas.txt", "r") as archivo:
    #leer numero de caracters pasado por parametro
    print(archivo.read(10))

archivo.close()
print("*****"*20)
with open("../notas.txt", "r") as archivo:
    #leer linea por linea usando readline()
    print(archivo.readline())
    print("**")
    print(archivo.readline())

archivo.close()

print("*****"*20 + "usando while")
with open("../notas.txt", "r") as archivo:
    #leer linea por linea usando readline()
    line = archivo.readline()
    while line:
        print("Linea*:"+ line)
        line = archivo.readline()
archivo.close()


