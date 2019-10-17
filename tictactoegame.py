def display_board(board):

	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']

print(display_board(test_board))

def player_input():

	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player1: Choose X or O:')
	if marker == 'X':
		return ('X','O')
	else:
		return('O','X')

print(player_input())

def win_check(board , marker):

    return(
    (board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker))

test_board = ['#','X','O','X','O','X','O','X','O','X']  

print(win_check(test_board , 'X'))

import random

def choose_first():

	flip = random.randint(0,1)

	if flip == 0:
		return 'player1'
	else:
		return 'player2'

print(choose_first())

def space_check(board , position):

	 return board(position) == ' ' 

def full_board_check(board):

	for i in range(1,10):
		 if space_check(boar,i):
		 	return True
		 else:
		 	return False
print(full_board_ckeck())