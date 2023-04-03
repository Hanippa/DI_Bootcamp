# What you will create

# Create a TicTacToe game in python, where two users can play together.
# tic tac toe


# Instructions

#     The game is played on a grid that’s 3 squares by 3 squares.
#     Players take turns putting their marks (O or X) in empty squares.
#     The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
#     When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

def display_board(board) -> None:
    '''
     To display the Tic Tac Toe board (GUI).
    '''
    print("\n")
    print(" TIC -- TAC -- TOE")
    print("--⌒ Ｙ⌒Ｙ⌒Ｙ⌒Ｙ⌒--")
    for i in board:
        print("|  ", end="")
        for char in i:
            print(char , end="  |  ")
        print("\n")
    print("┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬")
    print("\n")


def player_input(player:str, board, row:int , column:int) -> None:
    '''
     To get the position from the player.
    '''
    if board[row-1][column-1] == "-":
        board[row-1][column-1] = player
    else:
        print("Spot already used!")

def check_win(board , player) -> bool:
    '''
    To check whether there is a winner or not.
    '''

    #vertical scan
    index = 0
    column = 0
    for n in range(len(board)):
        for y in board:
            if y[column] == player:
                index += 1
            if index == 3:
                return True
        column += 1
        index = 0

    #horizontal scan
    index = 0
    for i in board:
        if i.count(player) == 3:
            return True

    
    #left to right diogonal scan
    index = 0
    for h in range(len(board)):
        if board[h-1][h-1] == player:
            index+=1
        if index == 3:
            return True

    # right to left diogonal scan
    index = 0
    count = 0
    for p in range(len(board), 0, -1):
        if board[index][p-1] != player:
            count = 0
        else:
            count += 1
        if count == 3:
            return True
        index += 1
    return False



def play():
    '''
     The main function, which calls all the functions created above.
    '''
    print()
    user_board = (["-","-","-"],
                  ["-","-","-"],
                  ["-","-","-"])
    game_round = 0
    while game_round < 9:
        display_board(user_board)
        player_input("O", user_board, int(input(" Player 'O' Row : ")), int(input(" Player 'O' Column : ")))
        game_round += 1
        if check_win(user_board, "O"):
            display_board(user_board)
            print("Player O won ! ")
            return
        if game_round == 9:
            break
        display_board(user_board)
        player_input("X", user_board, int(input(" Player 'X' Row : ")), int(input(" Player 'X' Column : ")))
        game_round += 1
        if check_win(user_board, "X"):
            display_board(user_board)
            print("Player X won ! ")
            return
    display_board(user_board)
    print("Tie")
play()
