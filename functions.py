import numpy as np

def num_letter(x):
	dic = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J'}
	return(dic[x])

def check_fire(board, x, y):
	if board[x, y] == 'W' or board[x, y] == 'X':
		return(1)
	return(0)

def check_match(inv, x, y):
	if (x, y) in inv:
		return(1)
	return(0)

def check_coord(x, y):
	if x < 0 or x > 9 or y < 0 or y > 9:
		print("off-map coordinates")
		return(1)
	return(0)

def player_fire(player):
	while True:
		try:
			y = ord(input("First coordinate(A-J): ").lower())-97
			x = int(input("Second coordinate(1-10): "))-1
		except:
			print("Invalid coordinate")
			continue
		if check_coord(x,y) == 1:
			continue
		if check_fire(player.board_machine, x, y) == 1:
			print("Repeated coordinate")
			continue
		if player.fire(x, y) == 1:
			continue
		print(f" {np.array(['A','B','C','D','E','F','G','H','I','J'])}")
		print(player.board_machine)
		break

def machine_fire(machine,dificulty):
	while True:
		for i in range(dificulty):
			x = np.random.randint(10)
			y = np.random.randint(10)
			if check_match(machine.inv, x, y) == 1:
				break
		if check_fire(machine.board_machine, x, y) == 1:
			continue
		print(f"Machine shoots in '{num_letter(y)}{x+1}'")
		if machine.fire(x, y) == 1:
			continue
		print(f" {np.array(['A','B','C','D','E','F','G','H','I','J'])}")
		print(machine.board)
		break

def difficulty():
	while True:
		difficulty = input("Choose the level of difficulty(Easy/Medium/Hard): ").lower()
		x = 1
		if difficulty == "easy":
			break
		elif difficulty == "medium":
			x = 2
			break
		elif difficulty == "hard":
			x = 3
			break
		else:
			print("Invalid response")
			continue
	return(x)

def place_ships():
	while True:
		answer = input("Do you want to place your ships or do you prefer to assign them randomly?\
(Place/Random): ").lower()
		if answer == "random" or answer == 'r':
			return(0)
		elif answer == "place" or answer == 'p':
			print("The order of the coordinates to enter will be: \
1 boat of length 4, 2 boats of length 3, 3 boats of length 2 and finally 4 boats of length 1")
			return(1)
		else:
			print("Invalid option")
			continue

def options(player, machine):
	while True:
		answer = input("Print Board(b) / Print shots(s) /Exit game (exit) / Continue (c) ").lower()
		if answer == 'b':
			print(machine.board)
			continue
		elif answer == 's':
			print(player.board_machine)
			continue
		elif answer == 'exit':
			return(1)
		elif answer == 'c':
			break
		else:
			print("Invalid option")
			continue
	return(0)

def welcome():
	print("""
Welcome to Battleship:

The game is played on four grids, two for each player. The grids are square  10x10
and the individual squares in the grid are identified by coordinates (x,y).
On one grid the player arranges ships and records the shots by the opponent.
On the other grid, the player records their own shots.

Before play begins, each player secretly arranges their ships on their primary grid.
Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically.
The number of squares for each ship is determined by the type of ship. The ships cannot overlap.
The types and numbers of ships allowed are the same for each player.
The ships should be hidden from players sight and it's not allowed to see each other's pieces.
The game is a discovery game which players need to discover their opponents ship positions.

After the ships have been positioned, the game proceeds in a series of rounds.
In each round, each player takes a turn to announce a target square in the opponent's grid which is to be shot at.
The opponent announces whether or not the square is occupied by a ship.
If it is a "hit", the player who is hit marks this on their own or "ocean" grid.
The attacking player marks the hit or miss on their own "tracking" or "target" grid,
in order to build up a picture of the opponent's fleet.

When all of the squares of a ship have been hit, the ship's owner announces the sinking of the ship.
If all of a player's ships have been sunk, the game is over and their opponent wins.
If all ships of both players are sunk by the end of the round, the game is a draw.
""")
