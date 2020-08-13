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
	print("\nWelcome to Tic Tac Toe game!")
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
	print(f"Hi {player1}, your symbol is 'X'\n")
	player2 = input("Player 2: Enter your name: ")
	print(f"Hi {player2}, your symbol is 'O'\n")
	return player1, player2

def check_winning_pattern(player_pattern):
        '''
        input    : A list (len = 9) containing current visual
        output   : True if the pattern matches with a winning pattern
        function : There is 8 winning patterns. If any players input
                   matches with the winning sequence return True else False
        '''
        winning_patterns = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                            {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                            {1, 5, 9}, {3, 5, 7}]
        for pattern in winning_patterns:
                if pattern.issubset(player_pattern):
                        return True
        return False

def get_inputs(player_name, player1_set, player2_set):
        '''
        input    : player's name, player 1 set, player 2 set
        output   : the valid index
        function : reads the player's input and check weather it is valid
        '''
        while True:
                index = input(f"Enter a valid index, {player_name}: ")
                if not index.isdigit():
                        print(f"{index} is not an index, enter an integer!")
                        continue
                index = int(index)
                if index < 1 or index > 9:
                        print(f"{index} is out of range, enter within range")
                        continue
                if index in player1_set or index in player2_set:
                        print(f"{index} is already taken, enter another index")
                        continue
                return index
        
        

while True:
        # Printing the game intor and the board with index
        print_intro()

        # Getting the player info
        player1, player2 = get_player_info()

        # Players patterns
        player1_set = set()
        player2_set = set()
        pattern = []
        for i in range(9):
                pattern.append(' ')

        # Getting input from player
        for i in range(5):
                p1 = get_inputs(player1, player1_set, player2_set)
                player1_set.add(p1)
                pattern[p1-1] = 'X'
                display_board(pattern)
                if check_winning_pattern(player1_set):
                        print("Game over")
                        break
                p2 = get_inputs(player2, player1_set, player2_set)
                player2_set.add(p2)
                pattern[p2-1] = 'O'
                display_board(pattern)
                if check_winning_pattern(player2_set):
                        print("Game over")
                        break

        print("Would you like to play another game?")
        if not input("Type 'Y' for to play again: ").lower() == 'y':
                break
