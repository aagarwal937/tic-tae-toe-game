def player_choice(board):

	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board , position):
		position = int(input('choose a position:(1-9)'))

	return position	

def replay():

	choice = input('play again? Enter Yes or No')

	return choice == 'Yes'
