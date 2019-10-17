import random

def choose_first():

	flip = random.randint(0,1)

	if flip == 0:
		return 'player1'
	else:
		return 'player2'

print(choose_first())