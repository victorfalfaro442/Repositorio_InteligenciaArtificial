def es_palindromo_v2():
    texto = input("Introduce el texto: ")
    procesado = texto.replace(" ", "").lower()
    
    if procesado == "":
        print("No es un palíndromo")
        return

    es_palin = True
    longitud = len(procesado)
    
    # Solo necesitamos recorrer hasta la mitad
    for i in range(longitud // 2):
        if procesado[i] != procesado[longitud - 1 - i]:
            es_palin = False
            break
            
    if es_palin:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

es_palindromo_v2()
