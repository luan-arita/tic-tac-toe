import random
#import main

def human_player(board, player):
    x = input("What is your move's X co-ordinate? ")
    y = input("What is your move's Y co-ordinate? ")
    return (x, y)

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

def finds_legal_move(board):
    moves_list = []
    for x, row in enumerate(board):
        for y, item in enumerate(row):
            if board[x][y] is None:
                moves_list.append((y, x))
    return moves_list

def get_opponent(who_am_i):
    if who_am_i == 'X':
        return 'O'
    elif who_am_i == 'O':
        return 'X'
    else:
        raise Exception("Unknown player:", who_am_i)

def random_move(board):
    moves_list = finds_legal_move(board)

    return random.choice(moves_list)

def random_ai(board, player):
    return random_move(board)

def find_winning_move(board, player):
    all_line_coords = get_all_line_coords()
    for line in all_line_coords:
        count_me = 0
        count_them = 0
        count_new = 0

        last_new_coord = None
        for x,y in line:
            value = board[x][y]
            if value == player:
                count_me += 1
            elif value == None:
                count_new += 1
                last_new_coord = (y,x)
            else:
                count_them += 1
        if count_me == 2 and count_new == 1:
            return last_new_coord

def blocks_opponent_winning_moves_ai(board, player):
    opponent = get_opponent(player)
    opponent_winning_move = find_winning_move(board, opponent)

    if opponent_winning_move:
        return opponent_winning_move
    else:
        return random_move(board)

def finds_own_winning_moves_ai(board, player):
    my_winning_move = find_winning_move(board, player)

    if my_winning_move:
        return my_winning_move
    else:
        return random_move(board)
    
def finds_winning_and_losing_moves_ai(board, player):
    my_winning_move = find_winning_move(board, player)
    opponent = get_opponent(player)
    opponent_winning_move = find_winning_move(board, opponent)

    if my_winning_move:
        return my_winning_move
    
    if opponent_winning_move:
        return opponent_winning_move
    return random_move(board)

    