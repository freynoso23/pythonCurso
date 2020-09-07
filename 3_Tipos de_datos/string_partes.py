# Un parrafo es un grupo de frases
# Una frase es un grupo de palabras y de signos de puntuacion
# una palabre es un grupo de letras.

miFrase = 'Hola amigo, como estas?'
miContestacion = 'Muy bien gracias'

print(miFrase)

# Imprimir la primera letra
print(miFrase[0])

# Imprimir un rango de letras (de la 3era a la 6ta)
print(miFrase[2:5])

# Imprimir el inicio hasta la posicion 11
print(miFrase[:11])

# Imprimir desde la posicion 11 hasta el final del string
print(miFrase[11:])

# imprimir una frase 2 veces
print(miFrase  * 2)

## Concatenar dos string 

miConversacion = miFrase + '\n' + miContestacion

print(miConversacion)