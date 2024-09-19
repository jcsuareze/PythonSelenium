
values = [1, 2, 3, 4, 5, "Hello", 3.14, 2.71, 6, 7, 8, 9, 10]
print(values)
print(values[0])
print(values[5])
print(values[-1])
print(values[1:3])

values.insert(3, "Python")
print(f"Valores despues de insertar{values}")

values.append("Selenium") #agrega al final

print(f"Valores al final de la lista {values}")

#mostar valores de la lista en reversa
values.reverse()
print(f"Valores en reversa {values}")

