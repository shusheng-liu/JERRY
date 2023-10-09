import numpy as np
import random

# check victory, apply move, check move, computer move, display board and menu

game_board = np.zeros((6,6))
print(game_board)


def display_board(board):
    # implement your function here
    pass
    
def check_victory(board,turn,rot):
    
    #check row by row
    for row in board:
        result = check_array_victory(row) 
        if result == 0:
            continue
        elif result == 1:
            return 1
        elif result == 2:
            return 2
        
    #check column by column
    for i in range (6):
        result = check_array_victory(board[:,i])
        if result == 0:
            continue
        elif result == 1:
            return 1
        elif result == 2:
            return 2
    
    #check diagonals 
    first_diagonal_ltr = [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5]]
    second_diagonal_ltr = [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]]
    third_diagonal_ltr = [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]]
    
    first_diagonal_rtl = [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]]
    second_diagonal_rtl = [board[0][5], board[1][4], board[2][3], board[3][2], board[4][1], board[5][0]]
    third_diagonal_rtl = [board[1][5], board[2][4], board[3][3], board[4][2], board[5][1]]

    diagonals = [first_diagonal_ltr, second_diagonal_ltr, third_diagonal_ltr, first_diagonal_rtl, second_diagonal_rtl, third_diagonal_rtl]

    for dia in diagonals:
        result = check_array_victory(dia)
        if result == 0:
            continue
        elif result == 1:
            return 1
        elif result == 2:
            return 2
    
    #check if board is all filed up
    if (0 not in board):
        return 3
    
    return 0

def check_array_victory(row):
    player1, player2 = 0,0
    for item in row:
        if item == 1:
            player1+=1
            player2 = 0
            if player1 == 5:
                return 1
            
        elif item == 2:
            player2+=1
            player1 = 0
            if player2 == 5:
                return 2
            
    return 0

def apply_move(board,turn,row,col,rot):






    return board
    
def check_move(board,row,col):    
    # implement your function here
    return False

def computer_move(board,turn,level):
    # implement your function here
    return (0,0,0)

def menu():  
    # implement your function here
    pass

#if __name__ == "__main__":
    #menu()=