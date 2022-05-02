from de import is_a_winning_option

def score(player_option:int, computer_option:int) -> list:
	points:list = [0,0]

	if is_a_winning_option(player_option, computer_option):
		points[0] = 1
	elif(is_a_winning_option(computer_option, player_option)):
		points[1] = 1
	else: 
		points = [0,0]
	return points