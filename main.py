def new_board():
    board = []
    for i in range(3):
        row = [None] * 3
        board.append(row)
    return board

def render(board):
    rows = []
    for y in range(0, 3):
        row = []
        for x in range(0, 3):
            row.append(board[x][y])
        rows.append(row)

    print('   ' + '0' + '   ' + '1' + '   ' + '2')
    print('  ' + 12 * '-')
    for x, row in enumerate(rows):
        print(str(x) + '|', end = '')
        for y, item in enumerate(rows):
            if rows[x][y] == None:
                rows[x][y] = ' '
            if y == 2:
                print(' ' + str(rows[x][y]), end = ' ')
            else:
                print(' ' + str(rows[x][y]) + ' '+ '|' , end = '')
        print('|')
    print('  ' + 12 * '-')

def get_move():
    x = input("What is your move's X co-ordinate? ")
    y = input("What is your move's Y co-ordinate? ")
    return (x, y)

def make_move(board, coords, player):
    x, y = int(coords[1]), int(coords[0])

    if board[x][y] is not None:
        raise Exception("Illegal Move!")
    
    else:
        board[x][y] = player

    return board

def get_all_line_coords():
    cols = []
    for x in range(0, 3):
        col = []
        for y in range(0,3):
            col.append((x,y))
        cols.append(col)

    rows = []
    for y in range(0, 3):
        row = []
        for x in range(0, 3):
            row.append((x, y))
        rows.append(row)
    
    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    return cols + rows + diagonals

def get_winner(board):
    all_line = get_all_line_coords()
    for i in all_line:
        line_values = [board[x][y] for (x,y) in i]

        if all(cell == 'X' for cell in line_values):
            return 'X'
        if all(cell == 'O' for cell in line_values):
            return 'O'
        
def is_board_full(board):
    for row in board:
        for col in row:
            if col is None:
                return False
    return True


def play():
    board = new_board()
    #players = [(player_1, 'X'), (player_2, 'O')]
    players = ['X', 'O']
    turnNumber = 0

    while True:
        x = turnNumber % 2
        print("It's", players[x], "turn.")
        move = get_move()
        make_move(board, move, players[x])
        render(board)


        winner = get_winner(board)
        if winner is not None:
            render(board)
            print("The winner is", winner, "!")
            break
        if is_board_full(board):
            render(board)
            print("It's a draw!")
            break
        turnNumber += 1


play()