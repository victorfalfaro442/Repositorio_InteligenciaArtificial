def cifrado_cesar_mejorado():
    # 1. Pedir el texto a cifrar
    texto = input("Introduce el mensaje a cifrar: ")

    # 2. Pedir y validar el desplazamiento (1-25)
    while True:
        try:
            desplazamiento = int(input("Introduce el valor de desplazamiento (1-25): "))
            if 1 <= desplazamiento <= 25:
                break
            else:
                print("Error: El valor debe estar entre 1 y 25.")
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

    resultado = ""

    # 3. Procesar cada carácter
    for carac in texto:
        if carac.isalpha():
            # Determinar si es mayúscula o minúscula para saber el punto de partida (A o a)
            codigo_base = ord('A') if carac.isupper() else ord('a')
            
            # Algoritmo de desplazamiento:
            # a. Convertir el carácter a un rango 0-25 (restando la base)
            # b. Sumar el desplazamiento
            # c. Aplicar módulo 26 para que 'z' salte a 'a'
            # d. Volver a sumar la base para recuperar el código ASCII original
            nuevo_codigo = (ord(carac) - codigo_base + desplazamiento) % 26 + codigo_base
            resultado += chr(nuevo_codigo)
        else:
            # Si no es letra (espacios, números, signos), se queda igual
            resultado += carac

    print("\nTexto cifrado:", resultado)

if __name__ == "__main__":
    cifrado_cesar_mejorado()
