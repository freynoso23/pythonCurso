usuario = input("Introduce tu usuario: ")
contraseña = input("Introduce tu contraseña: ")

# Para evaluar dos condiciones en una misma linea se usa AND
if usuario == "franmy" and contraseña == "@dm1n0225$":
    print("Bienvienido Franmy")
else:
    print("Usuario y Contraseña Incorrecto")

####### Otra Forma para evaluar condiciones, mas codigo #######

# if usuario == "franmy":
#     if contraseña == "@dm1n0225$":
#         print("Bienvienido Franmy")
#     else:
#         print("Usuario y Contraseña Incorrecto")
# else:
#     print("Usuario y Contraseña Incorrecto")

######## Pababras clave que unen resultados / condiciones #######
# and - para que la condicion general se cumpla, todas las condiciones especificas tiene que ser verdaderas
# or - Para que la condicion general se cumpla, al menos uns de las especificaciones tiene que ser verdaderas

condicionA = 5 > 3
condicionB = 5 < 3

if condicionA and condicionB:
    print("Todas las condiciones son verdaderas")

if condicionA or condicionB:
    print("Al menos una de las condiciones es verdadera")

