import numpy as np
import random

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

    board_copy = board.copy()
    board_copy[row][col] = turn

    if (rot % 2 == 0):
        #counter clockwise
        return rotate_counter_clockwise(board_copy, rot)
    else:
        #clockwise
        return rotate_clockwise(board_copy,rot)

    
def rotate_clockwise(board,rot):
    temp = board.copy()    

    if rot == 1:
        top_row = temp[0][3:]
        middle_row = temp[1][3:]
        bottom_row = temp[2][3:]
        
        for i in range(0,3):
            board[i][3] = bottom_row[i] 
            board[i][4] = middle_row[i]
            board[i][5] = top_row[i]
        
    elif rot == 3:
        top_row = temp[3][3:]
        middle_row = temp[4][3:]
        bottom_row = temp[5][3:]
        
        for i in range(0,3):
            board[i+3][3] = bottom_row[i] 
            board[i+3][4] = middle_row[i]
            board[i+3][5] = top_row[i]
        
    elif rot == 5:
        top_row = temp[3][:3]
        middle_row = temp[4][:3]
        bottom_row = temp[5][:3]
        
        for i in range(0,3):
            board[i+3][0] = bottom_row[i] 
            board[i+3][1] = middle_row[i]
            board[i+3][2] = top_row[i]
        
    else:
        top_row = temp[0][:3]
        middle_row = temp[1][:3]
        bottom_row = temp[2][:3]
        
        for i in range(0,3):
            board[i][0] = bottom_row[i] 
            board[i][1] = middle_row[i]
            board[i][2] = top_row[i]
    
    return board
    
def rotate_counter_clockwise(board,rot):
    temp = board.copy()    
    
    if rot == 2:
        right_col = temp[:,5]
        middle_col = temp[:,4]
        left_col = temp[:,3]
        
        for i in range(0,3):
            board[0][i+3] = right_col[i] 
            board[1][i+3] = middle_col[i]
            board[2][i+3] = left_col[i]
        
    elif rot == 4:
        right_col = temp[:,5]
        middle_col = temp[:,4]
        left_col = temp[:,3]
        
        for i in range(3,6):
            board[3][i] = right_col[i] 
            board[4][i] = middle_col[i]
            board[5][i] = left_col[i]
        
    elif rot == 6:
        right_col = temp[:,2]
        middle_col = temp[:,1]
        left_col = temp[:,0]
        
        for i in range(0,3):
            board[3][i] = right_col[i+3] 
            board[4][i] = middle_col[i+3]
            board[5][i] = left_col[i+3]
        
    else:
        right_col = temp[:,2]
        middle_col = temp[:,1]
        left_col = temp[:,0]
        
        for i in range(0,3):
            board[0][i] = right_col[i] 
            board[1][i] = middle_col[i]
            board[2][i] = left_col[i]
            
   
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