def esta_oculta():
    # 1. Pedir las dos cadenas y normalizar a minúsculas
    palabra = input("Introduce la palabra que buscas: ").lower()
    contenedor = input("Introduce la cadena donde buscar: ").lower()

    posicion_actual = 0
    encontrada = True

    # 2. Buscar cada letra de la palabra una por una
    for letra in palabra:
        # Buscamos la letra a partir de la última posición encontrada
        posicion_actual = contenedor.find(letra, posicion_actual)
        
        # Si find() devuelve -1, la letra no existe en lo que queda de cadena
        if posicion_actual == -1:
            encontrada = False
            break
        
        # Si la encuentra, sumamos 1 para que la próxima búsqueda
        # empiece DESPUÉS de esta letra
        posicion_actual += 1

    # 3. Imprimir el resultado
    if encontrada:
        print("Si")
    else:
        print("No")

if __name__ == "__main__":
    esta_oculta()
