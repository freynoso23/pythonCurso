miLista = ['a', 'b', 'c', 'd']
print(miLista)

# Añadir elemento al final de la lista:
miLista.append('e')
print('Tras añadir:', miLista)

# Insertar un elemento en la lista en la posicion que quiero
# Lista + insert (posicion, 'parametro')
miLista.insert(2, 'x')
print('Tras insertar',miLista)

# NOTA: La diferencia entre append y insert es que insert añade el valor a la posicion que deseo en la lista.

#Eleminar un elemento de mi lista
del miLista[2]
print('Tras eliminar:', miLista)

# Combinar Listas
miSegundaLista = ['z', 'f', 'a']
miLista.extend(miSegundaLista)
print('Tras extender:', miLista)

# Comprobar si un elemento existe en una lista
print('Existe c en mi lista')
resultado = 'c' in miLista # En la variable resultado buscamos el elemento c en miLista (Esto los que devuelve es true o false)
print(resultado)
#Otra forma de hacer la comprobacion pero arrojando un valor que no existe en la lista
print('Existe x en mi lista')
print('x' in miLista)

# Contar el numero de elemento en la lista.
numeroDeElemento = len(miLista)
print('Mi lista tiene %d elementos' %(numeroDeElemento)) # Se casteo el numero de elementos por un entero.

# Eliminar un elemento en concreto de mi lista (por valor)
miLista.remove('a') # NOTA: remueve el primer valor de coincidencia no lo remueve todos los valores
print('Tras eliminar a:', miLista)