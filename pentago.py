import numpy as np
import random

def display_board(board):
    print(board)
    
def check_victory(board,turn,rot):
    
    result = check_board_victory(board)
    if result == 0:
        board_copy = board.copy()
        board_copy_rotated = rotate(board_copy,rot)
        return check_board_victory(board_copy_rotated)
    else:
        return result    

def check_board_victory(board):
    
    PLAYER_1_WIN = False
    PLAYER_2_WIN = False
    
    #check row by row
    for row in board:
        result = check_array_victory(row) 
        if result == 0:
            continue
        elif result == 1:
            PLAYER_1_WIN = True
        elif result == 2:
            PLAYER_2_WIN = True
        
    #check column by column
    for i in range (6):
        result = check_array_victory(board[:,i])
        if result == 0:
            continue
        elif result == 1:
            PLAYER_1_WIN = True
        elif result == 2:
            PLAYER_2_WIN = True
    
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
            PLAYER_1_WIN = True
        elif result == 2: 
            PLAYER_2_WIN = True
            
    if PLAYER_1_WIN and PLAYER_2_WIN:
        return 3
    elif (0 not in board):     #check if board is all filed up
        return 3
    elif PLAYER_1_WIN:
        return 1
    elif PLAYER_2_WIN:
        return 2
    else:
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
        
        elif item == 0:
            player1, player2 = 0,0
            
    return 0

def apply_move(board,turn,row,col,rot):

    board_copy = board.copy()
    board_copy[row][col] = turn

    return rotate(board_copy,rot)

def rotate(board, rot):
    if (rot % 2 == 0):
        #counter clockwise
        return rotate_counter_clockwise(board, rot)
    else:
        #clockwise
        return rotate_clockwise(board,rot)
    
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
    return (board[row][col] == 0)

def computer_move(board,turn,level):

    if level == 1:
        return random_computer_player(board, turn)
    else:
        return medium_computer_player(board, turn)

def random_computer_player(board, turn):
    possible_moves = []
    for i in range(6):
        for j in range(6):
            if (board[i][j] == 0):
                possible_moves.append((i,j))
                
    move = random.randint(0, len(possible_moves) - 1 )
    rotation = random.randint(1,8)
    (row, col) = possible_moves[move]
    return (row,col,rotation)

def medium_computer_player(board, turn):
    
    (x,y,z) = (total_possible_win(board))
    if (x >= 0 and y >= 0 and z >= 1):
        return (x,y,z)
    else:
        return random_computer_player(board,turn)

def total_possible_win(board):

    copy = board.copy()
    # do for normal board
    (x,y) = possible_win(copy)
    if (x >= 0 and y >= 0):
        return (x,y,1)
    # do for all possible rotations
    for i in range(1,9):
        board_copy = board.copy()
        board_copy_rotated = rotate(board_copy,i)
        (x,y) = possible_win(board_copy_rotated)
        if (x >= 0 and y >= 0):
            (x,y) = pre_rotation_coords(board,i,(x,y))
            return (x,y,i)
        
    return (-1,-1,-1)

def pre_rotation_coords(board,rot,coords):
    
    board_copy = board.copy()
    
    if (rot%2==0):
        rot -= 1
    else:
        rot += 1
    
    (x,y) = coords
    board_copy[x][y] = 3
    board_copy = rotate(board_copy,rot)
    
    for i in range(6):
        for j in range(6):
            if (board_copy[i][j] == 3):
                return (i,j)
    
def possible_win(board):
    
    # check along each row
    for i in range(6):
        result = possible_row_victory(board[i,:])
        if (result >= 0 ):
            return (i,result)
            
    # check along each column
    for i in range (6):
        result = possible_row_victory(board[:,i])
        if (result >= 0 ):
            return (result,i)
        
    first_diagonal_ltr = [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5]]
    second_diagonal_ltr = [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]]
    third_diagonal_ltr = [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]]
    
    first_diagonal_rtl = [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]]
    second_diagonal_rtl = [board[0][5], board[1][4], board[2][3], board[3][2], board[4][1], board[5][0]]
    third_diagonal_rtl = [board[1][5], board[2][4], board[3][3], board[4][2], board[5][1]]

    diagonals = [first_diagonal_ltr, second_diagonal_ltr, third_diagonal_ltr, first_diagonal_rtl, second_diagonal_rtl, third_diagonal_rtl]

    # check for each diagonal
    for i in range(6):
        result = possible_row_victory(diagonals[i])
        if (result >= 0):
            return get_diagonal_coordinate((i,result))
            
            
    return(-1,-1)

def get_diagonal_coordinate(input):
    
    dia_coord = [
        [(0,1),(1,2),(2,3),(3,4),(4,5)],
        [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)],
        [(1,0),(2,1),(3,2),(4,3),(5,4)],
        [(0,4),(1,3),(2,2),(3,1),(4,0)],
        [(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)],
        [(1,5),(2,4),(3,3),(4,2),(5,1)]
    ]
    
    (x,y) = input
    
    return dia_coord[x][y]

def possible_row_victory(row):
    
    player1, player2 = 0,0
    gap = False
    gap_pos = -1
    
    for item in row:
        if item == 1:
            player1+=1
            
        elif item == 2:
            player2+=1
            
        elif item == 0:
            if gap:
                # Scenario 1 : There is 1 or 2's in-between the two empty tiles -> update gap pos
                if (gap_pos != player1+player2):
                    gap_pos = player1+player2+1
                # Scenario 2 : Consecutive 0's
                elif (gap_pos == player1+player2):
                    if (gap_pos == 0):
                        gap_pos = 1
                    else:
                        return (-1)
            else:
                gap = True
                gap_pos = player1+player2
            
        if ((player1 == 4 or player2 == 4) and gap):
            return gap_pos

    return -1

def menu():  
    
    main_menu()

def main_menu():
    print("")
    print("------------ PENTAGO ------------")
    print("Please enter your desired option")
    print("(1) Play against another player")
    print("(2) Play against easy level computer")
    print("(3) Play against medium level computer")
    print("(4) Quit the game.")
    
    valid_input = False
    while not valid_input:
        option = input(">")
        try:
            option = int(option)
        except ValueError:
            print("Please enter a number")

        if (option > 4 or option < 1):
            print("Please enter a valid number")
        else:
            valid_input = True
            
    if (option == 1):
            pvp()
    elif (option == 2):
            pve(1)
    elif (option == 3):
            pve(2)   
    else:
            return
        
def pve(level):
    
    game_over = False
    
    game_board = np.zeros((6,6))
    print(game_board)
    
    while not game_over:
        
        print("")
        print("  -------------------- Player's Turn --------------------  ")
        (row, column, rotation) = get_input(game_board)
        game_board = apply_move(game_board, 1, row, column, rotation)
        result = check_victory(game_board, 1, rotation)
        
        if (result != 0):
            game_over = True
            continue
        else:
            print("")
            print(game_board)
        
        print("")
        print("  -------------------- CPU's Turn --------------------  ")
        (row, column, rotation) = computer_move(game_board, 2, level)
        print(f"\n CPU played row: {row}, column: {column}, rotation: {rotation}")
        game_board = apply_move(game_board, 2, row, column, rotation)
        result = check_victory(game_board, 2, rotation)
        
        if (result != 0):
            game_over = True
        else:
            print("")
            print(game_board)
        
        print("")
        next_turn = input("Would you like to continue? (y/n) : ")
        game_over = next_turn.lower() == "n"
    
    print("")    
    if (result == 1):
            print("-------------------- Player Wins!! --------------------")
    elif (result == 2):
            print("-------------------- CPU Wins!! --------------------") 
    elif (result == 3):
            print("-------------------- It's a Draw!! --------------------")   
        
    input(" >>>        Press Enter to go back to the main menu        <<< ")
    main_menu()   
    
def pvp():
    
    game_over = False
    
    game_board = np.zeros((6,6))
    print(game_board)
    
    while not game_over:
        
        print("")
        print("  -------------------- Player One's Turn --------------------  ")
        (row, column, rotation) = get_input(game_board)
        game_board = apply_move(game_board, 1, row, column, rotation)
        result = check_victory(game_board, 1, rotation)
        
        if (result != 0):
            game_over = True
            continue
        else:
            print("")
            print(game_board)
        
        print("")
        print("  -------------------- Player Two's Turn --------------------  ")
        (row, column, rotation) = get_input(game_board)
        game_board = apply_move(game_board, 2, row, column, rotation)
        result = check_victory(game_board, 2, rotation)
        
        if (result != 0):
            game_over = True
        else:
            print("")
            print(game_board)
        
        print("")
        next_turn = input("Would you like to continue? (y/n) : ")
        game_over = next_turn.lower() == "n"
    
    print("")    
    if (result == 1):
            print("-------------------- Player One Wins!! --------------------")
    elif (result ==2):
            print("-------------------- Player Two Wins!! --------------------") 
    elif (result == 3):
            print("-------------------- It's a Draw!! --------------------")   
        
    input(" >>>        Press Enter to go back to the main menu        <<< ")
    main_menu()   
    
def get_input(board):
    
    print("Please enter the row, column and rotation you'd like to play")
    
    valid_input = False
    
    while not valid_input:
        try:
            row = int(input("Row: "))
            column = int(input("Column: "))
            rotation = int(input("Rotation: "))
        except ValueError:
            print("Please enter a number for each of the inputs.")
            continue
    
        if (row > 5 or row < 0):
            print("Please enter a valid row from 0 to 5.")
            continue
        elif (column > 5 or column < 0):
            print("Please enter a valid column from 0 to 5.")
            continue
        elif (rotation > 8 or rotation < 1):
            print("Please enter a valid rotation from 1 to 8.")
            continue
        
        valid_input = check_move(board, row, column)
        
        if not valid_input:
            print("That is not a valid move, please enter again.")
        
    return(row,column,rotation)
    
if __name__ == "__main__":
    menu()