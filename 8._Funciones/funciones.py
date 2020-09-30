# Sintaxis para definir una funcion
# def nombreDeLaFuncion(parametro1, parametros2):
#   codigo a ejecutar por la funcion.
#   return valor de retorno.

def calValorCuadrado(numero):
    numCuadrado = numero * numero
    return numCuadrado

# Para ingresar los valores, que le vamos a pasar a la funcion.
print("Hola amigos, inicio del programa")
miNumero = input("Introduzca un numero: ")
miNumero = int(miNumero)

# Resultado del numero ingresado y pasado a la funcion.
res = calValorCuadrado(miNumero)
print("Mi valor al cuadrado es: ", res) # Para ver el valor del resultado de la funcion.


# ------- funcion sin return -------
def imprimirPalomitas():
    print("PALOMITAS")

imprimirPalomitas()