# develop a tic tac toe game with python
# using numbers to find spaces, and lists to build the board and play

board = [" " for i in range(9)]

def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    
print_board()
