# ----Global Variables----

# Game board
board = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]


# If game still going
game_still_going = True


# Who Won? or Tie?
winner = None


# Whos truns is it  
current_player = "X"


# Display borad
def  dispay_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play game of tic tac toe
def play_game():

    # Display initial board
    dispay_board()

    # While the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

       # check if the game has ended
        check_if_game_over()
        
        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won. ")
    elif winner == None:
        print("Tie.")


# Checking if the game over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Checking for the winner
def check_for_winner():

    # Set up global variables
    global winner
    #check  rows
    row_winner = chack_rows()

    #check  columns
    column_winner = chack_columns()

    #chack diagonals 
    diagonals_winner = chack_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return


# Checking in row winners
def chack_rows():
    # Set up global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    # If ant row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False 
    # Return hte winner (X or O)
    if row_1:
       return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# Checking for column winners
def chack_columns():
    # Set up global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    # If ant row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False 
    # Return hte winner (X or O)
    if column_1:
       return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# checking for diagonal swinners
def chack_diagonals():
    # Set up global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    
    # If ant row does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False 
    # Return hte winner (X or O)
    if diagonals_1:
       return board[0]
    elif diagonals_2:
        return board[6]


# Checking if tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# Flip player 'O' to 'X' and 'X' to 'O'
def flip_player():
    # Set up global variables
    global current_player
    # if current player is X, then change it to O
    if current_player =="X":
        current_player = "O"
        # if current player is O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return


# handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position from 1-9: ")

            position = int(position) - 1

            if board[position] == "-":
                valid = True
            else:
                print("You can't go there. Go again.")

    board[position] = player

    dispay_board()


play_game()  
