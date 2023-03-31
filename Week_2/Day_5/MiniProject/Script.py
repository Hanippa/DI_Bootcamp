# What you will create

# Create a TicTacToe game in python, where two users can play together.
# tic tac toe


# Instructions

#     The game is played on a grid that’s 3 squares by 3 squares.
#     Players take turns putting their marks (O or X) in empty squares.
#     The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
#     When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
# ["x","x","x"],["x","x","x"],["x","x","x"]

def display_board(board) -> None:
    '''
     To display the Tic Tac Toe board (GUI).
    '''
    print(board[0])
    print(board[1])
    print(board[2])


def player_input(player:str, board, row:int , column:int) -> None:
    '''
     To get the position from the player.
    '''
    if board[row-1][column-1] == "-":
        board[row-1][column-1] = player
    else:
        print("Spot already used!")

def check_win(board , player):
    '''
    To check whether there is a winner or not.
    '''
    index = 0
    for y in board:
        for z in range(len(y)):
            if y[z] == player:
                index += 1
            if index == 3:
                return True


    index = 0
    for i in board:
        if i.count(player) == 3:
            return True



    for h in range(len(board)):
        if board[h-1][h-1] == player:
            index+=1
        if index == 3:
            return True


    index = 0
    for p in range(len(board), 0, -1):
        if board[index][p-1] != player:
            index = 0
        index+=1
        if index == 3:
            return True
    return False
def play():
    '''
     The main function, which calls all the functions created above.
    '''

user_board = (["X","O","O"],
              ["O","O","X"],
              ["X","X","X"])
print(check_win(user_board, "O"))
