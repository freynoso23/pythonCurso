num1 = input("Introduce el primer numero: ")
num2 = input("Introduce el segundo numero: ")

# res = num1 / num2
# print("El resultado de la division es:", res)
# print("------ fin del programa ------")

# Try-except para manejar errores
try:
    res = int(num1) / int(num2)
    print("El resultado de la division es:", res)
except:
    print("El programa contiene un EROORRRR")

print("------ fin del programa ------")