def es_valido(secuencia):
    # Una secuencia es válida si contiene los dígitos del 1 al 9 exactamente una vez
    return sorted(list(secuencia)) == [str(i) for i in range(1, 10)]

def validar_sudoku():
    tablero = []
    
    # 1. Lectura y validación de entrada
    for i in range(9):
        fila = input(f"Introduce la fila {i+1} (9 dígitos): ").strip()
        if len(fila) != 9 or not fila.isdigit():
            print("Entrada no válida. Deben ser 9 dígitos.")
            return
        tablero.append(list(fila))

    # 2. Verificar Filas
    for fila in tablero:
        if not es_valido(fila):
            print("No")
            return

    # 3. Verificar Columnas
    for col in range(9):
        columna = [tablero[fila][col] for fila in range(9)]
        if not es_valido(columna):
            print("No")
            return

    # 4. Verificar Subcuadrículas 3x3
    # r y c definen el inicio de cada cuadro de 3x3
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            cuadrante = []
            for i in range(3):
                for j in range(3):
                    cuadrante.append(tablero[r + i][c + j])
            if not es_valido(cuadrante):
                print("No")
                return

    print("Sí")

if __name__ == "__main__":
    validar_sudoku()
