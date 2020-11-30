# MinMaxConnect4 Function Description

def __init__ (self):
•	Used to initialize the board
•	Initializes:  
o	Number of rows/cols
o	An empty board filled with zeroes
o	The round players are on
o	The last moves made
o	Possible moves
o	Maximum number of moves



def initiate_empty_connect4 (self):
•	Resets:  
o	Board
o	The round players are on
o	The last move made
o	Maximum number of moves


def print_board (self):
•	Prints the board as a 2D array
o	B stands for the blue token
o	R stands for the Red token
o	0 stands for No token


def fill_space (self, command):
•	Takes a command as a parameter. Determines if the command is valid and if so, adds it to the current board
•	Every time function is called it increments the round by 1
•	If command is invalid or impossible, user will receive error “NOT A POSSIBLE MOVE” and the maximum number of moves will be incremented by 1
•	If command is “undo” but there is nothing to undo, user will receive error “NOTHING TO UNDO”
•	Commands (f1, f2, f3, f4, f5, f6, f7, f8, undo)


def checkVertical (self, player):
•	Checks all Vertical positions for win states based on the player


def checkHorizontal (self, player):
•	Checks all Horizontal positions for win states based on the player


def checkDiagonal (self, player):
•	Checks all Diagonal positions for win states based on the player
