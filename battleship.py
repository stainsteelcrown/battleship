#Andrew Castano
#Codeacademy
#Battleship

from random import randint

#Declare board variable
board = []

#Initialize board
board_size = int(raw_input("Please choose a board size:"))
for x in range(board_size):
    board.append(["O"] * board_size)

#function for printing the board
def print_board(board):
    for row in board:
        print " ".join(row)

#Display to the user
print "Let's play Battleship!"
print_board(board)

#Two functions to generate battleship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#calling the functions and storing the battleship location
ship_row = random_row(board)
ship_col = random_col(board)

#For loop that allows user 4 chances at guessing
for i in range(4):
    guess_row = int(raw_input("Guess Row:")) #gets input from user
    guess_col = int(raw_input("Guess Col:"))
    
    #Conditional statements for the various outcomes of the game
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > (len(board) - 1)) or 
           (guess_col < 0 or guess_col > (len(board[0]) - 1)):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print i + 1
        
        print_board(board)
        
        if i == 3:
            print"Game Over"
