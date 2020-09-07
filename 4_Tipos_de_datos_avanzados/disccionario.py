# Crear un diccionario con usuarios y sus edades
# dicionario = { 'identificador' : datoAsociado }

edadesUsuarios = {'Pedro' : 32, 'Franmy': 38, 'Mercedes': 37}
print('Que edad tiene Franmy?' 'Franmy Tiene:' , edadesUsuarios['Franmy'])


# IMPORTANTE: No podemos tener identificadores iguales o repetidos. si es asi tomara el ultimo identificador insertado.

# Forma alternativa de crear un diccionario: la funcion dic()
# dict(identificado = datoAsociado)

lasEdadesUsuarios2 = dict(Marta = 23, Jose = 43, Joas = 25)
print('Que edad tiene Joas?\n' 'Joas Tiene:', lasEdadesUsuarios2['Joas'])

# Que pasa si intento acceder a un dato que  no existe en un diccionario

# print(edadesUsuarios['pepo']) 
# Key error de que es dato no se encontro en el diccionario

# Para cambiar un dato a un diccionario, el dato debe de existir.
edadesUsuarios ['Franmy'] = 39
print(edadesUsuarios)


# Para agregar un dato a un diccionario
lasEdadesUsuarios2['paco'] = 64
print(lasEdadesUsuarios2)

# Para eliminar un dato de un diccionario, es igual que en la lista.
del lasEdadesUsuarios2['Marta']
print(lasEdadesUsuarios2, '\n')

# Funciones extras
#Limpiar un diccionario completo.
print(edadesUsuarios)
edadesUsuarios.clear()
print(edadesUsuarios, '\n')

# Saber cuales son mis Keys/identificadores en un diccionario - funcion keys
print('Los keys de mi lasEdadesUsuarios2 son:', lasEdadesUsuarios2.keys())

# Saber cuales son mis valores en un diccionario - funcion values
print('Los values de mi lasEdadesUsuarios2 son:', lasEdadesUsuarios2.values())

# Saber cuantos elementos tenemos en un diccionario
print('Saber cuantos elementos tenemos en el diccionario:', len(lasEdadesUsuarios2))
