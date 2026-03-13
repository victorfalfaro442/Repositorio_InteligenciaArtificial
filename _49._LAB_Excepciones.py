def leer_entero(mensaje, min_val, max_val):
    while True:
        try:
            # Intentamos convertir la entrada a entero
            valor = int(input(mensaje))
            
            # Si la conversión tiene éxito, verificamos el rango
            if valor < min_val or valor > max_val:
                print(f"Error: el valor no está dentro del rango permitido ({min_val}..{max_val})")
            else:
                # Si todo está bien, salimos del bucle devolviendo el valor
                return valor
                
        except ValueError:
            # Si int() falla porque el usuario escribió letras, atrapamos el error
            print("Error: entrada incorrecta")

# Prueba de la función
v = leer_entero("Introduce un número entre -10 y 10: ", -10, 10)

print("El número es:", v)
