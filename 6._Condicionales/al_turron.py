# Objetivo: decirle al usuario el precio que tendria que pagar por su entrada a un museo.
# Las tarifas son:
# Niño (hasta 6 años): No Paga
# Joven (hasta 21 años): 9 USA
# Adulto: 14 USA
# Jubilado (A partir de 67 años): 6 USA
# Ademas, hemos repartido unos descuentos en el último mes del 10%. Si un usuario tiene un descuento y 
# lo dice, tenemos que descontarle ese 10% del precio.
# Normas extras:
# - Si es un niño, no preguntar si tiene descuento o no. Si es gratis, es gratis.
# - Si tiene descuento, mostrar precio con y sin descuento
# - Si no tiene descuento, mostrar únicamente el precio normal.

#Ejemplo:
# >> !Hola! Bienvenido al museo de python.
# >>
# >> Si quiere saber el precio de su entrada, por favor indique su edad: 37
# >> !De acuerdo! Tiene usted el bono de descuento del 10% para este mes/ (s/n): s
# >> 
# El precio de su entrada sin descuento es de 14.0 USA. Cone el descuento, con 12.6 USA

bienvenida = print("!Hola! Bienvenido al museo de python.")
entradaEdad = int(input("Si quiere saber el precio de su entrada, por favor indique su edad: "))

if entradaEdad <= 6:
    print("El niño no paga")
elif entradaEdad <= 21: 
    siNo = input("!De acuerdo! Tiene usted el bono de descuento del 10% para este mes/ (s/n): ")
    if siNo == "s":
        porciento = 9 * 10 / 100 
        total = 9 - porciento
        print(f"Su precio con descuento es:", total)
    else:
        siNo == "n"
        print(f"Su precio con sin descuento es: 9 USA")
elif entradaEdad <= 66: 
    siNo = input("!De acuerdo! Tiene usted el bono de descuento del 10% para este mes/ (s/n): ")
    if siNo == "s":
        porciento = 14 * 10 / 100 
        total = 14 - porciento
        print(f"Su precio con descuento es:", total)
    else:
        siNo == "n"
        print(f"Su precio con sin descuento es: 14 USA")
else:
    print(f"Su precio con sin descuento es: 6 USA")
            
    