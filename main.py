import random
from game_score import score

def play_game() -> None:
	games_played:int = 0
	player_points = 0
	computer_points = 0
	total_games:int = 5

	while games_played < total_games:
		games_played+=1

		print("================== Game n°", games_played, "==============\n")

		player_option = int(input("Choice an option: 1.rock 2.paper 3.scissors\n"))
		
		computer_option:int = random.randint(1,3)
		
		print("The computer has chosen:", computer_option, "\n")

		print("Score:")
		player_points += score(player_option, computer_option)[0]
		computer_points += score(player_option, computer_option)[1]
		print("Player", player_points, "vs", "Computer", computer_points)

if __name__ == "__main__":
	play_game()