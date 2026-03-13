def es_anagrama():
    # 1. Pedir los dos textos
    texto1 = input("Introduce el primer texto: ")
    texto2 = input("Introduce el segundo texto: ")

    # 2. Limpieza: quitar espacios y pasar a minúsculas
    limpio1 = texto1.replace(" ", "").lower()
    limpio2 = texto2.replace(" ", "").lower()

    # 3. Comprobar si están vacíos
    if limpio1 == "" or limpio2 == "":
        print("No son anagramas (una o ambas cadenas están vacías)")
        return

    # 4. Lógica principal:
    # Convertimos a listas, ordenamos y comparamos
    # Si las listas ordenadas son iguales, son anagramas
    if sorted(limpio1) == sorted(limpio2):
        print("Son anagramas")
    else:
        print("No son anagramas")

if __name__ == "__main__":
    es_anagrama()
