# Ojetivos de este "Al Turron"
# A partir de 4 datos dados en variables, obtener el precio de un deposito de gasolina
# Imprimir el precio para que parezca una factura
# Componerlo todo en una unica string
# Resultado  esperado:

# --------- Factura ---------
# Combustible: DIESEL
# Precio 1.395 USA/1
# Litros: 44.59
# Surtidor:17
# Importe total: 62.20 USA

# --------------------------
precio = '1.394934'
litros = 44.59
surtidor = 17.0
combustible = 'diesel'

print('--------- Factura ---------')
print('Combustible:', combustible.upper())

precio = float(precio) #Convertimos primero el tipo de dato de entero a float
precioRedondeado = 'Precio %.3f' %(precio) #Luego en una nueva variable convertimos el dato con dos decimales
print(precioRedondeado) # Imprimimos el dato 

LitroFloat = ('Litros %.2f' %(litros))#Luego en una nueva variable convertimos el dato con dos decimales
print(LitroFloat)# Imprimimos el dato 

surtidor = int(surtidor) #Convertimos el dato en entero
print('Surtidor:', surtidor) # Imprimimos el dato

importeTotal = (litros * precio) # Multiplicamos los dos datos que tenemos en float
importeTotal = ('Importe Total %.2f'%(importeTotal)) #Luego en una nueva variable convertimos el dato con dos decimales
print(importeTotal)# Imprimimos el dato 

