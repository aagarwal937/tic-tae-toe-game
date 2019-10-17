def player_input():

	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player1: Choose X or O:')
	if marker == 'X':
		return ('X','O')
	else:
		return('O','X')

print(player_input())