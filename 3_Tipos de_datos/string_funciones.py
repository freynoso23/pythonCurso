miString = 'Hola me llamo franmy'
print('mi string inicial', miString)

# Poner una frase en mayuscula
miStringMayus = miString.upper()
print('String Mayus:', miStringMayus)

# Poner una frase en minuscula
print('String Minu', miString.lower())
print('Esto no modifica la string original:', miString)

# funcion remplazar - Remplazamos letras
print('remplazamos las o por las i', miString.replace('o','i'))

# funcion remplazar - Remplazamos palabras
print('remplazamos franmy  por las arquimedes', miString.replace('franmy','arquimedes'))

# Remplazar las primeras 2 o por i
print('remplazamos las o por las i', miString.replace('o','i',2))

# Reemplazar Espacios, con saltos de linea.
print(miString.replace(' ','\n'))

