# Tenemos una lista con nombres de ciudades:
ciudadesDeEspana = ['Granada', 'Cordoba', 'Santiago de Compostela', 'Paris', 'Malaga', 'Barcelona']
otrasCiudades = ['Toledo', 'Sevilla', 'Cadiz', 'Berlin', 'Alicante']

# Tareas
# 1.- Quitar de las listas las ciudades  que no pertenezcan a espana (Berlin y Paris)
# 2.- Unir ambas listas en una unica
# 3.- Anadir Madrid, la capilta, en la primera posicion de la lista, porque no esta
# 4.- Anadir otras tres ciudades a tu eleccion (por ejemplo: Mallorca, Santander y Burgos)
# 5.- Imprimir la sigueinte frase por Pantalla:
# >> Mi lista de ciudades tiene {numerro de ciudades aqui} ciudades: [Contenido de la lista]

# punto 1
removeCiudades = ciudadesDeEspana.remove('Paris'), otrasCiudades.remove('Berlin')

# punto 2 Extender
ciudadesDeEspana.extend(otrasCiudades)

# Punto 3 añadir
ciudadesDeEspana.insert(0, 'Madrid')
print(ciudadesDeEspana)

# Punto 4 añadir
ciudadesDeEspana.append('Mallorca')
ciudadesDeEspana.append('Santander')
ciudadesDeEspana.append('Burgos')
print(ciudadesDeEspana)


TextoFinal = '>> Mi lista de ciudades tiene', len(ciudadesDeEspana),  'Cidudades:', ciudadesDeEspana
print(TextoFinal)

