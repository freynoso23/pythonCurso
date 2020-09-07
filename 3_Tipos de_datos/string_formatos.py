# Formatear un strin es introducir datos dentro de ellas.
combustible = 'Gasolina'
precioPorLitro = 1.3293
duracionPrecio = 5

#Combinamos varios elementos en un string:
mensaje = 'El precio por litro de %s en los proximos %d dias es de %f USA/1' % (combustible,duracionPrecio,precioPorLitro)
print(mensaje)

# Explicaciones:
 # - Las strinfg se formateasn con %s
 # - Los enteros se formatean con %d
 # - Los floats se formateas con %
 
# - Podemos añadir un parametro extra para limitar el tamaño: %10d
pruebaMensaje = 'Mi entero: %10d' %(duracionPrecio)
print(pruebaMensaje)

# - Los foat se formatean con %f
# -- Podemos añadir dos parámetros extra:
# -- a) Para limitar el tamaño: %4f
# -- b) Para limitar el numero de decimales a mostrar: %.2f

floatsMensaje = 'Mi float: %.2f' %(precioPorLitro)
print(floatsMensaje)

# imprimir entrero com float y viceversa
# Ventaja es que podemos cambiar el tipo de dato en el string.
miUltimaPrueba = 'mi entrero como floart: %.3f y mi floa com entero: %d' %(duracionPrecio, precioPorLitro)
print(miUltimaPrueba)

# Utilizar la funcion formart()

print('--------------------')

pruebaMensaje = 'Mi entero: {0:d}' .format(duracionPrecio)
print(pruebaMensaje)

# Forma en que se le pueden pasar varios parametros en un mismo string con format
# La desventaja es que no podemos cambiar el tipo de dato.

floatsMensaje = 'Mi float: {0:f}. mi float con 2 decimales {0:.2f}' .format(precioPorLitro)
print(floatsMensaje)

ultimoTest = 'Mi numero 1: {} y mi numero2: {}' .format(precioPorLitro, duracionPrecio)
print(ultimoTest)