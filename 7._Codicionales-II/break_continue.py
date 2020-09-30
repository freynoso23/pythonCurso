nombresUsuarios = ["Juan", "Ana", "Omenga", "Joas", "Franmy"]

for nombre in nombresUsuarios:
    print("Mi Usuario es: ", nombre)
    if nombre == "Omenga":
        break # Interupe el loop y pasa a la siguiente instrucciones fuera de loop!

    print("Esto se ejecuta fuera del loop")



for nombre in nombresUsuarios:
    print("Mi Usuario es: ", nombre)
    if nombre == "Omenga":
        continue # Continua el loop y pasa a la siguiente instruccion de loop!

    print("Esto se ejecuta fuera del loop")