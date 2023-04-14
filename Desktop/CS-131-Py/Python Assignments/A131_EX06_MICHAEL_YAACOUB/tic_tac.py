"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 06 Exercises - Part C
Date: 03/22/2023
---------------------------------------
Write a program that plays tic-tac-toe.
The tic-tac-toe game is played on a 3 × 3 grid as in the photo at right.
The game is played by two players, who take turns. The first player marks moves with
a circle, the second with a cross. The player who has formed a horizontal, vertical,
or diagonal sequence of three marks wins. Your program should draw the game board, ask the user
for the coordinates of the next mark,
change the players after every successful move, and pronounce the winner.
"""


board = [" "," "," ",
         " "," "," ",
         " "," "," "]
current_player = "X"
winner = None
game_on = True

def print_board(board):
    print(board[0] + "  | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(board[3] + "  | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(board[6] + "  | " + board[7] + " | " + board[8])

def player_input(board):
    '''player input'''
    input_player = int(input("Enter a number 1-9: "))
    if input_player >= 1 and input_player <= 9 and board[input_player - 1] == " ":
        board[input_player - 1] = current_player
    else:
        print("Player already has this spot, Please try again: ")

def horizontal(board):
    """Checks for win horizontally"""
    global winner
    if board[0] == board[1] == board[2] and board[1] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner == board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

def check_row(board):
    """chacks  in for board row and returns a boolean"""
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True

def diagonal(board):
    """Check win diagonal"""
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True

def tie(board):
    """Checks if a tie"""
    global game_on
    if " " not in board:
        print_board(board)
        print("You got a tie!")
        game_on = False

def check_to_win():
    """Checks for win"""
    global game_on
    if horizontal(board) or diagonal(board) or check_row(board):
        print("The winner is " + winner)
        game_on = False

def player_y():
    """second player for the game"""
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

while game_on:
    """Checking to see who won or a tie"""
    print_board(board)
    player_input(board)
    check_to_win()
    tie(board)
    player_y()