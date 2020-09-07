miNombre = input('Introduce tu nombre: ')
miEdad = input('Introduce tu edad: ')

print('Hola mi nombre es:', miNombre, 'y tengo', miEdad, 'años')

# Un imput siempre sera un string, por ende no se pueden hacer acciones matematicas con enteros o float, la forma es castear la variable.
print('El año que viene tendras', int(miEdad) + 1, 'años')