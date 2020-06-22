import random

# sempre escolhendo as bifurcações mais curtas 
infections_path1 = [1, 3, 5, 12, 26, 36, 41, 43, 45, 50, 55, 67, 76, 88, 93, 98, 105, 111]
preventions_path1 = [16, 31, 59, 78, 82, 90, 102]
board_length_path1 = 112

# escolhendo a bifurcação mais curta, depois a mais longa
infections_path2 = [1, 3, 5, 12, 26, 36, 41, 53, 58, 70, 79, 91, 96, 101, 108, 114]
preventions_path2 = [16, 31, 46, 62, 81, 85, 93, 105]
board_length_path2 = 115

# escolhendo a bifurcação mais longa, depois a mais curta
infections_path3 = [9, 16, 30, 40, 45, 47, 49, 54, 59, 71, 92, 97, 102, 109, 115]
preventions_path3 = [4, 20, 35, 63, 86, 94, 106]
board_length_path3 = 116

# sempre escolhendo as bifurcações mais longas
infections_path4 = [9, 16, 30, 40, 45, 57, 62, 74, 83, 95, 100, 105, 112, 118]
preventions_path4 = [4, 20, 35, 50, 66, 85, 97, 109] 
board_length_path4 = 119


def roll_dice():
	return random.randint(1, 6)


def frequency_counter(board_length):
	board = [0]*board_length
	for game in range(10000):
		position = -1
		no_winner = True
		while no_winner:
			position += roll_dice()
			if position >= board_length:
				no_winner = False
			else :
				board[position] += 1
	print(board)
	return board


def frequency_counter_with_effects(board_length, infections, preventions):
	board = [0]*board_length
	position = -1
	for game in range(10000):
		position = -1
		no_winner = True
		while no_winner:
			position += roll_dice()
			if position in infections:
				poistion = position if random.random() < 0.5 else position - roll_dice() 
			if position in preventions:
				position = position if random.random() < 0.5 else position + roll_dice()
			if position >= board_length:
				no_winner = False
			else :
				board[position] += 1
	print(board)
	return board

frequency_counter(board_length_path1)
frequency_counter(board_length_path2)
frequency_counter(board_length_path3)
frequency_counter(board_length_path4)

frequency_counter_with_effects(board_length_path1, infections_path1, preventions_path1)
frequency_counter_with_effects(board_length_path2, infections_path2, preventions_path2)
frequency_counter_with_effects(board_length_path3, infections_path3, preventions_path3)
frequency_counter_with_effects(board_length_path4, infections_path4, preventions_path4)