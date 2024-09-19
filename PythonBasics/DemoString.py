str1 = "Python y selenium"
str2 = " con el curso de python"
str3 = "Python"
str4 = "python.java.C++.c#"

print(str1[1])
print(str1[0:5])
print(str1[5:])  #Imprime desde la posicion 5 hasta el final
print(str1[:5])

print(str1 + str2) #Concatenacion
print(str1 * 3) #Repetir la cadena 3 veces
print("***" * 20)
print(str3 in str1) #Verifica si str3 esta en str1
print(str3 not in str1) #Verifica si str3 no esta en str1
print("***" * 20)

var = str4.split(".") #Separa la cadena por el punto y lo convierte en una lista
print(var)
print(var[0])
print("***" * 20)
quitaEspacios = "    Hola Mundo    "
print(quitaEspacios.strip()) #Quita los espacios en blanco
print(quitaEspacios.lstrip()) #Quita los espacios en blanco de la izquierda
print(quitaEspacios.rstrip()) #Quita los espacios en blanco de la derecha
