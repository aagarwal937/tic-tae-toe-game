def space_check(board , position):

	 return board(position) == ' '

def full_board_check(board):

	for i in range(1,10):
		 if space_check(boar,i):
		 	return True
		 else:
		 	return False

print(full_board_ckeck(board))