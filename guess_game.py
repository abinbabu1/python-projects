'''Three cup guessing game
There is a list [' ', 'O', ' ']. 
User needs to guess the position of 'O'
User inputs the index position 0,1 or 2 as guess 
'''
from random import shuffle


#print(cups)
#shuffle(cups)

def  cup_shuffle(cups):

	shuffle(cups)
	return cups


def player_guess():

	guess = ''
	while guess not in ['0','1','2']:

		guess = input("Pick a number: 0, 1 or 2: ")

	return int(guess)

def check_guess(after_shuffle, x):

	y = after_shuffle[x] == 'O'
	if y:
		print("Congratulations! You guessed correctly! ")
		print(after_shuffle)
	else:
		print("Wrong Guess!")
		print(f"You picked position {x}")
		print("Actual position")
		print(after_shuffle)


while True:

	cups = [' ', 'O', ' ']
	after_shuffle = cup_shuffle(cups)
	#print(after_shuffle)
	x = player_guess()
	y = check_guess(after_shuffle, x)
	#print(y)
	#while play_again not in ['Y']	
	play_again = input("Do you want to play again? Y or N ").upper()
	if play_again != 'Y':
		break
