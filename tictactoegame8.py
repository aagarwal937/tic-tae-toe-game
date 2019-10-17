print('Welcome to TIC TAC TOE')

while true:

	the_board = [' ']*10
	player1_marker,player2_marker = player_input()

	turn = choose_first
	print(turn + 'will go first')

	play_game = input('Ready to play? y or n?')

	if play_game == 'y':
		game_on = True
	
	else:
	    game_on = False	

	while game_on:

		if turn == 'Player 1':

		     display_board(the_board)

		position = player_choice(the_board)
		
		place_marker(the_board,player1_marker,position)

		if win_check(the_board,player1_marker):
			display_board(the_board)
			print('Player1 has WON!!!')
			game_on = False
		
		else:
			
			if full_board_check(the_board):
			    display_board(the_board)
			    print('TIE GAME!!!')
			    game_on = False
			else:
			    turn = 'Player2'

else:

		display_board(the_board)

		position = player_choice(the_board)
		
		place_marker(the_board,player2_marker,position)

		if win_check(the_board,player2_marker):
			display_board(the_board)
			print('Player2 has WON!!!')
			game_on = False

		else:

			if full_board_ckeck(the_board):
			    display_board(the_board)
			    print('TIE GAME!!!')
			    game_on = False
			
			else:
			    turn = 'Player1'
	
	if no_reply():
		break	    