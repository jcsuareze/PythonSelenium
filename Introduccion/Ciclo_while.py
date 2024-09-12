#ciclo while
#while condicion:   #mientras la condicion sea verdadera
#    bloque de codigo

#Ejemplo 1

i = 0
while i < 10:
    print(i)
    i += 1

#Ejemplo 2

arreglo = [1,2,3,4,5,6,7,8,9,10]
a = 0
while a < len(arreglo):
    if arreglo[a] % 2 == 0:
        print(arreglo[a])
    a += 1

#Ejemplo 3

i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

#Ejemplo 4

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

#Ejemplo 5

i = 0
while i < 10:
    if i == 5:
        pass
    print(i)
    i += 1






