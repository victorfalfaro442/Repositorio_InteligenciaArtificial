def generar_histograma_simple():
    # 1. Pedir el nombre del archivo
    nombre_archivo = input("Introduce el nombre del archivo de entrada: ")
    
    # Diccionario para almacenar las frecuencias
    histograma = {}

    try:
        # 2. Abrir y leer el archivo
        # 'rt' significa lectura de texto
        with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
            for linea in archivo:
                for char in linea:
                    # Solo procesamos letras latinas
                    if char.isalpha():
                        letra = char.lower()
                        histograma[letra] = histograma.get(letra, 0) + 1

        # 3. Imprimir el histograma ordenado alfabéticamente
        # sorted() sobre las llaves del diccionario nos da el orden a, b, c...
        for llave in sorted(histograma.keys()):
            print(f"{llave} -> {histograma[llave]}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no pudo ser encontrado.")
    except IOError as e:
        print(f"Ocurrió un error de entrada/salida: {e}")

if __name__ == "__main__":
    generar_histograma_simple()
