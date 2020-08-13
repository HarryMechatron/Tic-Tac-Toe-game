def display_board(positions):
	'''
	input    : A list with length 9 (game characters 'x' and 'o')
	output   : -
	function : Print the Tic Tac Toe board with respect to the player inputs
	'''
	p = positions[::]
	print("\n")
	print(f" {p[0]} | {p[1]} | {p[2]} ")
	print("-----------")
	print(f" {p[3]} | {p[4]} | {p[5]} ")
	print("-----------")
	print(f" {p[6]} | {p[7]} | {p[8]} ")
	print("\n")

def print_intro():
	'''
	input    : -
	output   : -
	function : Printing the intro with the initial board positions
	'''
	print("Welcome to Tic Tac Toe game!")
	print("\n")
	print("The board with initial position is: ")
	display_board([1, 2, 3, 4, 5, 6, 7, 8, 9])

def get_player_info():
	'''
	input    : -
	output   : Player names
	function : Get the two player names from user 
	'''
	player1 = input("Player 1: Enter your name: ")
	print(f"Hi {player1}, your symbol is 'X'")
	player2 = input("Player 2: Enter your name: ")
	print(f"Hi {player2}, your symbol is 'O'")
	return player1, player2

def check_winning_pattern(player_pattern):
        winning_patterns = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                            {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                            {1, 5, 9}, {3, 5, 7}]
        for pattern in winning_patterns:
                if pattern.issubset(player_pattern):
                        return True

while True:
        # Printing the game intor and the board with index
        print_intro()

        # Getting the player info
        get_player_info()

        # Getting input from player
        # Validating Input
        if check_winning_pattern({1,2,3}):
                print("Game Over")
                break
