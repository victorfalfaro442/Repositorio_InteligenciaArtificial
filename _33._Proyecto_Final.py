from random import randrange

def display_board(board):
# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for col in row:
            print(f"|   {col}   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
# La función acepta el estado actual del tablero y pregunta al usuario sobre su movimiento, 
# verifica la entrada y actualiza el tablero según la decisión del usuario.
    ok = False
    while not ok:
        move = input("Introduce tu movimiento (1-9): ")
        if not (len(move) == 1 and move >= '1' and move <= '9'):
            print("¡Entrada inválida! Introduce un número del 1 al 9.")
            continue
        
        move = int(move) - 1  # Convertir a índice 0-8
        row = move // 3
        col = move % 3
        
        if board[row][col] in ['X', 'O']:
            print("¡Esa casilla ya está ocupada! Elige otra.")
            continue
        
        board[row][col] = 'O'
        ok = True

def make_list_of_free_fields(board):
# La función examina el tablero y construye una lista de todos los cuadros libres. 
# La lista contiene tuplas (fila, columna).
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free.append((r, c))
    return free

def victory_for(board, sign):
# La función analiza el estado del tablero para verificar si 
# el jugador que utiliza las 'X' o las 'O' ha ganado el juego.
    
    # Comprobar filas
    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True
    # Comprobar columnas
    for c in range(3):
        if board[0][c] == sign and board[1][c] == sign and board[2][c] == sign:
            return True
    # Comprobar diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    return False

def draw_move(board):
# La función dibuja el movimiento del ordenador y actualiza el tablero.
    free = make_list_of_free_fields(board)
    if len(free) > 0:
        idx = randrange(len(free))
        row, col = free[idx]
        board[row][col] = 'X'

# --- Lógica principal del juego ---

# Inicializar tablero
board = [[(i + j * 3) + 1 for i in range(3)] for j in range(3)]

# El primer movimiento pertenece al ordenador (siempre en el centro)
board[1][1] = 'X'
human_turn = True

while True:
    display_board(board)
    
    if human_turn:
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("¡Has ganado!")
            break
    else:
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("¡El ordenador ha ganado!")
            break
    
    # Comprobar empate
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("¡Empate!")
        break
    
    human_turn = not human_turn
