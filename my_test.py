from pentago import *

def test():
    
    #Counter-clockwise rotation test
    board_in = np.array([     
        [1,2,1,1,0,0],
        [1,1,1,0,0,0],
        [2,1,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_out = np.array([
        [1,1,1,1,1,0],
        [2,1,1,0,0,0],
        [1,1,2,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_tmp = apply_move(board_in,1,0,4,8)
    if ((board_tmp == board_out).all()): print("test apply_move 1 - OK !")
    else: 
        print(f"Before: \n {board_in}")
        print("")
        print(f"After: \n {board_tmp}")
        print("test apply_move 1 - Problem in the apply_move function output  !")
        
        
    #Clockwise rotation test
    board_in = np.array([     
        [1,2,1,1,0,0],
        [1,1,1,0,0,0],
        [2,1,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_out = np.array([
        [2,1,1,1,1,0],
        [1,1,2,0,0,0],
        [1,1,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_tmp = apply_move(board_in,1,0,4,7)
    if ((board_tmp == board_out).all()): print("test apply_move 2 - OK !")
    else: 
        print(f"Before: \n {board_in}")
        print("")
        print(f"After: \n {board_tmp}")
        print("test apply_move 2 - Problem in the apply_move function output  !")
        
    #Hard Clockwise rotation test
    board_in = np.array([     
        [1,2,3,1,0,0],
        [4,5,6,0,0,0],
        [7,8,9,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_out = np.array([
        [7,4,1,1,1,0],
        [8,5,2,0,0,0],
        [9,6,3,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_tmp = apply_move(board_in,1,0,4,7)
    if ((board_tmp == board_out).all()): print("test apply_move 3 - OK !")
    else: 
        print(f"Before: \n {board_in}")
        print("")
        print(f"After: \n {board_tmp}")
        print("test apply_move 3 - Problem in the apply_move function output  !")
        
    # insert marble with rot on empty submatrix
    board_in = np.array([     
        [1,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]])
    board_out = np.array([
        [0,0,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,2,0],
        [0,0,0,0,0,0]])
    board_tmp = apply_move(board_in,2,4,4,7)
    if ((board_tmp == board_out).all()): print("test apply_move 4 - OK !")
    else: 
        print(f"Before: \n {board_in}")
        print("")
        print(f"After: \n {board_tmp}")
        print("test apply_move 4 - Problem in the apply_move function output  !")


test()