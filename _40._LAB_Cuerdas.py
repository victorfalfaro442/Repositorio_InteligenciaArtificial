def mysplit(strng):
    # Si la cadena está vacía o solo tiene espacios, devolvemos lista vacía
    if strng == "" or strng.isspace():
        return []

    lista_resultado = []
    palabra_actual = ""
    en_palabra = False

    for carac in strng:
        if carac != " ":  # Si el carácter NO es un espacio
            palabra_actual += carac
            en_palabra = True
        else:
            if en_palabra:  # Si veníamos de una palabra y encontramos un espacio
                lista_resultado.append(palabra_actual)
                palabra_actual = ""
                en_palabra = False
                
    # Al terminar el bucle, si quedó una palabra pendiente, la agregamos
    if en_palabra:
        lista_resultado.append(palabra_actual)

    return lista_resultado

# Pruebas solicitadas
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser,esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" ABC "))
print(mysplit(""))
