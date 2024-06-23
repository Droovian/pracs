player, opponent = 'x', 'o'


def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                return True
    return False

def evaluate(board):

    for i in range(3): # check rows
        if(board[i][0] == board[i][1]  and board[i][1] == board[i][2]):
            if(board[i][0] == player):
                return 10
            elif(board[i][0] == opponent):
                return -10

    for col in range(3): # check columns
        if(board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            if(board[0][col] == player):
                return 10
            elif(board[0][col] == opponent):
                return -10

    if(board[0][0] == board[1][1] and board[1][1] == board[2][2]): # principal diagonal
        if(board[0][0] == player):
            return 10
        elif(board[0][0] == opponent):
            return -10

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]): # other diagonal
        if (board[0][2] == player):
            return 10
        elif(board[0][2] == opponent):
            return -10

    return 0


def minimax(board, depth, is_max):

    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    # do one more check here to see if any moves are left simple 2 for loops( return 0 )
    if(is_moves_left(board) == False):
        return 0

    if(is_max):
        best = -1000

        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = player

                    best = max( best, minimax(board, depth+1, not is_max))

                    board[i][j] = '_'
        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = opponent

                    best = min(best, minimax(board, depth+1, not is_max))

                    board[i][j] = '_'
        return best

def find_best_move(board):

    best_val = -1000
    best_move= (-1, -1)

    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'): # if board is empty, make a move ( player )
                board[i][j] = player

                mov_val = minimax(board, 0 , False) # recursive minimax , computing evaluation for this move

                board[i][j]= '_'

                if(mov_val > best_val):
                    best_val =  mov_val
                    best_move = (i, j)

    print()
    return best_move


board = [
    ['x', 'o', 'x'],
    ['o', 'o', 'x'],
    ['_', '_', '_']
]

best_move = find_best_move(board)
print(best_move)
print("ROW:", best_move[0], " COL:", best_move[1])
