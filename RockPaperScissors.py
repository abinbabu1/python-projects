'''
Python Program for Rock, Papers, Scissors Game
Uses Function, Loop, List, Dictionary
'''

import random

computer_token = ['r','p','s']
user_score = 0
comp_score = 0
print("\t\tROCK PAPER SCISSORS")

def result(user_input, comp_input):
	'''
	Takes user and computer input.
	Creates a string using both inputs.
	Compares the string with three lists
	to determine who wins or whether game is tie.
	A dictionary is used to store the print string to
	be displayed.
	'''
	global user_score, comp_score

	print_dict = {'rs': 'Rock crushes Scissors',
					'pr': 'Paper covers Rock',
					'sp': 'Scissors cuts Paper',
					'rp': 'Paper covers Rock',
					'ps': 'Scissors cuts Paper',
					'sr': 'Rock crushes Scissors'}

	exp = f"{user_input}{comp_input}"

	if exp in ['rr', 'pp', 'ss']:
		print("Game Tie")
	if exp in ['rs', 'pr', 'sp']:
		print(print_dict[exp])
		print("You win")
		user_score += 1
	if exp in ['rp', 'ps', 'sr']:
		print(print_dict[exp])
		print("Computer wins")
		comp_score += 1


while True:

	#Display score card
	print(f"\tScore Card")
	print(f"\tYou: {user_score}, Computer: {comp_score}")
	
	#Getting User input
	user_input = ''
	while user_input not in ['r', 'p', 's']:

		user_input = input("Enter your choice: R, P or S: ").lower()
		if user_input not in ['r', 'p', 's']:
			print("Invalid choice")

	#Getting computer input
	comp_input = random.choice(computer_token)
	
	print(f"Your choice: {user_input}, Computer choice: {comp_input}")
	
	#Function call to determine result
	result(user_input, comp_input)
	
	#Check if player wants to play again
	z = input("Do you want to play again? Y/N ").upper()
	if z != 'Y':
		
		#Display Final Score Card
		print(f"\tFinal Score Card")
		print(f"\tYou: {user_score}, Computer: {comp_score}")
		break
