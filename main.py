import random

def option_is_correct(option1:int, option2:int) -> bool:
	return (option1==1 and option2==3) or (option1==2 and option2==1) or (option1==3 and option2==2)

def announce_winner(player_option:int, computer_option:int) -> None:
	if option_is_correct(player_option, computer_option):
		print("Player wins\n")
	elif(option_is_correct(computer_option, player_option)):
		print("Computer wins\n") 
	else: 
		print("Tie\n")

def play_game() -> None:
	games_played:int = 0
	#player_points = 0
	#computer_points = 0
	total_games:int = 5

	while games_played < total_games:
		games_played+=1

		print("================== Game n°", games_played, "==============\n")

		player_option = int(input("Choice an option: 1.rock 2.paper 3.scissors\n"))
		
		computer_option:int = random.randint(1,4)
		
		print("The computer has chosen:", computer_option, "\n")
		
		announce_winner(player_option, computer_option)

		#print("Score:")
		#player_points += score(player_option, computer_option)
		#computer_points += score(player_option, computer_option)
		#print("Player", player_points, "vs", "Computer", computer_points)

if __name__ == "__main__":
	play_game()