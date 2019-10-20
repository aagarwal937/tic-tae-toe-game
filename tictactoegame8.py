print('Welcome to TIC tAC TOE')

while True:
	the_board = [' ']*10
	Player1_marker,Player2_marker = Player_input()
	turn = choose_first
	print(turn+'will go first')

	play_game = input('ready to play? y or no')

	if play_game == y:
		game_on = True

	else:
		game_on  = False

	while game_on:

		if turn == 'Player1':
			display_board(the_board)

		position = Player_choice(the_board)

		place_marker(the_board,Player1_marker,positon)

		if win_check(the_board,Player1_marker):
		    display_board(the_board)
		    print('Player1 has WON!!!!!')
		    game_on = False
		
		else:

		    if full_board_check(the_board):
		    	display_board(the_board)
		    	print('TIE GAME!!!!')
		    	game_on = False
		    
	else:
			display_board(the_board)

	position = Player_choice(the_board)

	place_marker(the_board,Player1_marker,positon)

	if win_check(the_board,Player1_marker):
		 display_board(the_board)
		 print('Player1 has WON!!!!!')
		 game_on = False
		
	else:

		if full_board_check(the_board):
		    display_board(the_board)
		    print('TIE GAME!!!!')
		    game_on = False

	if not replay():
		break 	