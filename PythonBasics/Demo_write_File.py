#read the file and store all the lines in list
#reverse the list

#Abrir un archivo
with open("../borrarEsteArchivo.txt", "r") as lectura:
    contenido = lectura.readlines()
    reversed(contenido)
    with open("../borrarEsteArchivo.txt", "w") as escritura:
        for line in contenido:
            escritura.write(line)
        escritura.close()
    lectura.close()

