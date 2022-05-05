def is_equal(player_option:int, game_option:int) -> bool:
	return player_option==game_option

def winning_option_one(player_option1, player_option2):
	return is_equal(player_option1, 1) and is_equal(player_option2, 3)

def winning_option_two(player_option1, player_option2):
	return is_equal(player_option1, 2) and is_equal(player_option2, 1)

def winning_option_three(player_option1, player_option2):
	return is_equal(player_option1, 3) and is_equal(player_option2, 2)

def is_a_winning_option(player_option1, player_option2):
	return winning_option_one(player_option1, player_option2) or winning_option_two(player_option1, player_option2) or winning_option_three(player_option1, player_option2)