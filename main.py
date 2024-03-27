import heuristic_ai
import random

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
        for y, item in enumerate(row):
            if rows[x][y] == None:
                rows[x][y] = ' '
            if y == 2:
                print(' ' + str(rows[x][y]), end = ' ')
            else:
                print(' ' + str(rows[x][y]) + ' '+ '|' , end = '')
        print('|')
    print('  ' + 12 * '-')


def make_move(board, coords, player):
    x, y = int(coords[1]), int(coords[0])
    if board[x][y] is not None:
        raise Exception("Illegal Move!")
    else:
        board[x][y] = player

    return board


def get_winner(board):
    all_line = heuristic_ai.get_all_line_coords()
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


def play(player1, player2):
    board = new_board()
    players = [[player1, 'X'], [player2, 'O']]
    #players = ['X', 'O']
    turnNumber = 0

    while True:
        x = turnNumber % 2

        print("It's", players[x][1], "turn.")
        player = players[x][1]
        if x == 0: #Player1's turn
            move = player1(board, player)
        elif x == 1:
            move = player2(board, player)
        print(move)
        make_move(board, move, player)
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

def repeated_play(player1, player2):
    board = new_board()
    players = [[player1, 'X'], [player2, 'O']]
    turnNumber = 0

    while True:
        x = turnNumber % 2
        player = players[x][1]
        if x == 0: #Player1's turn
            move = player1(board, player)
        elif x == 1:
            move = player2(board, player)
        make_move(board, move, player)

        winner = get_winner(board)
        if winner is not None:
            return winner
        if is_board_full(board):
            return 0
        turnNumber += 1

#play(heuristic_ai.random_ai, heuristic_ai.finds_winning_and_losing_moves_ai)
        
def repeated_battle(player1, player2, battle_count):
    i = 0
    player1_win = 0
    player2_win = 0
    draw = 0
    while i < battle_count:
        result = repeated_play(player1, player2)
        if result == 'X':
            player1_win += 1
        elif result == 'O':
            player2_win += 1
        else:
            draw += 1
        i += 1
    print("Player 1 wins:", player1_win)
    print("Player 2 wins:", player2_win)
    print("Draws:", draw)

repeated_battle(heuristic_ai.blocks_opponent_winning_moves_ai, heuristic_ai.finds_winning_and_losing_moves_ai, 1000)