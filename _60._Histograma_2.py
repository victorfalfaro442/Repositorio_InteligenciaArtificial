import os

def generar_histograma_ordenado():
    # 1. Pedir el nombre del archivo al usuario
    nombre_archivo = input("Introduce el nombre del archivo de entrada: ")
    
    # Intentamos abrir el archivo de entrada
    try:
        with open(nombre_archivo, "rt", encoding="utf-8") as f:
            contenido = f.read().lower()
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return
    except IOError as e:
        print(f"Error de E/S: {e}")
        return

    # 2. Crear el histograma (solo para letras latinas)
    histograma = {}
    for char in contenido:
        if char.isalpha():
            histograma[char] = histograma.get(char, 0) + 1

    # 3. Ordenar el histograma por frecuencia (de mayor a menor)
    # Convertimos el diccionario a una lista de tuplas para poder ordenarlo
    # La lambda toma el segundo elemento (frecuencia) para ordenar: items()[1]
    lista_ordenada = sorted(histograma.items(), key=lambda x: x[1], reverse=True)

    # 4. Crear el nombre del archivo de salida (.hist)
    nombre_salida = nombre_archivo + ".hist"

    # 5. Escribir el resultado en el nuevo archivo
    try:
        with open(nombre_salida, "wt", encoding="utf-8") as f_out:
            for char, cuenta in lista_ordenada:
                linea = f"{char} -> {cuenta}\n"
                f_out.write(linea)
                # También lo imprimimos en consola para verificar
                print(linea, end="")
        
        print(f"\nÉxito: El histograma se ha guardado en '{nombre_salida}'.")

    except IOError as e:
        print(f"Error al escribir el archivo de salida: {e}")

if __name__ == "__main__":
    generar_histograma_ordenado()
