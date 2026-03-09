def mostrar_siete_segmentos(numero):
    # Definimos cada dígito como una lista de 5 niveles (filas)
    patrones = {
        '0': ["###", "# #", "# #", "# #", "###"],
        '1': ["  #", "  #", "  #", "  #", "  #"],
        '2': ["###", "  #", "###", "#  ", "###"],
        '3': ["###", "  #", "###", "  #", "###"],
        '4': ["# #", "# #", "###", "  #", "  #"],
        '5': ["###", "#  ", "###", "  #", "###"],
        '6': ["###", "#  ", "###", "# #", "###"],
        '7': ["###", "  #", "  #", "  #", "  #"],
        '8': ["###", "# #", "###", "# #", "###"],
        '9': ["###", "# #", "###", "  #", "###"]
    }

    # Convertimos el número a string para iterar por cada dígito
    num_str = str(numero)
    
    # Imprimimos fila por fila (hay 5 filas en total)
    for fila in range(5):
        linea_a_imprimir = ""
        for digito in num_str:
            # Añadimos el patrón del dígito para esa fila específica + un espacio de separación
            linea_a_imprimir += patrones[digito][fila] + "  "
        print(linea_a_imprimir)

# Solicitar datos al usuario
try:
    entrada = input("Introduce un número entero no negativo: ")
    if entrada.isdigit():
        mostrar_siete_segmentos(entrada)
    else:
        print("Por favor, introduce solo números.")
except EOFError:
    pass
