#diccionario

#creacion de un diccionario
data = {"name": "John", "age": 30, "city": "New York"}

print(data)

#creacion de un diccionario sin valores
data = {}

data["name"] = "John"
data["age"] = 35
data["city"] = "Mexico"

print(data)

#modificar un valor del diccionario
data["age"] = 40

print(data)

for key in data:
    print(key)
    print(data[key])
    print(data)
