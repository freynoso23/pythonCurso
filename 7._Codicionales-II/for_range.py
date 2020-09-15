# la funcion range() genera una lista de numeros con los siguientes parametros:
# range(start, end, step)
# Start: Numero desde el que se inicia
# End: Numero maximo
# Step: "Salto" entre un numero y otros


miRange = range(1,10,1)

for numero in miRange:
    print(numero)

# Solo 1 parametro: estamos pasando el parametro final (end)
print("----- 1 paramentros -----")
for num in range(10):
    print(num)

# Solo 2 parametro: (start a end)
print("----- 2 paramentros -----")
for num in range(10,50):
    print(num)

# Solo 3 parametro: (start, end step)
print("----- 3 paramentros -----")
for num in range(10,50, 5):
    print(num)