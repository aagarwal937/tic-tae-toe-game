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