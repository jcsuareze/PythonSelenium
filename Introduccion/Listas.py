#Ejemplos de listas
lenguajes = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'PHP', 'Ruby', 'Perl', 'Go', 'Swift']
print("Lenguaje seleccionado " + lenguajes[2])

lenguajes[2] = 'C'
print("Lenguaje seleccionado " + lenguajes[2])

print("Lenguajes desde el segundo hasta el cuarto " + str(lenguajes[1:4]))

lenguajes.append('Rust')
print("Lenguajes " + str(lenguajes))

lenguajes.insert(2, 'C++')
print("Lenguajes " + str(lenguajes))


