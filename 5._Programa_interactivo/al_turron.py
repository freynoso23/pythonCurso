# Dado un numero introducido por el usuario, tenemos que imprimir por pantalla:
# Sus 5 primeros multiplos.
# Su valor al cuadrado.
# Su valor al cubo.
# Su valor mulplicado por 100.

# >> Hey! Introduce tu numero que calcule cosas:
# Sus 5 primeros multiplos: 23.0 46.0 69.0 92.0 115.0
# >> Su cuadrado y su cubo 529 12167.0
# >> Su valor por 100: 2300.0

calcule = input("Hey! Introduce tu numero que calcule cosas: ")
numeroIntroducido = float(calcule) #Se castea el numero a entero para proceder hacer los calculos y para usar en mas adelante en las diferentes operaciones.
# multiplos = float(calcule), float(calcule) * 2, float(calcule) * 2 + float(calcule), float(calcule) * 2 * 2, float(calcule) * 2 * 2 + float(calcule)
print("Sus 5 primeros multiplos:", numeroIntroducido, numeroIntroducido * 2, numeroIntroducido * 3, numeroIntroducido * 4)
print("Su cuadrado y su cubo:", numeroIntroducido ** 2, numeroIntroducido ** 3)
print("Su valor por 100:", numeroIntroducido * 100)