def display_board(board):

	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']

print(display_board(test_board))

def place_marker(board, marker, position):

    board[position] = marker

print(place_marker(test_board,'!',8))
print(display_board(test_board))