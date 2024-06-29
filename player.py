from utils import correct_int_input
from const import BOARD_SIZE

class Player:
    def __init__(self, id:int):
        self.id = id
    
    def request_move(self,board):
        row_inp = input(f"Please input a row value from 0 to {BOARD_SIZE-1}, inclusive.")
        while not correct_int_input(row_inp,0,BOARD_SIZE-1): 
            row_inp = input(f"Invalid input. Please input a row value from 0 to {BOARD_SIZE-1}, inclusive.")
        
        col_inp = input(f"Please input a column value from 0 to {BOARD_SIZE-1}, inclusive.")
        while not correct_int_input(col_inp,0,BOARD_SIZE-1): 
            col_inp = input(f"Invalid input. Please input a column value from 0 to {BOARD_SIZE-1}, inclusive.")
        
        rot_inp = input(f"Please input a rotation value from 1 to 8, inclusive.")
        while not correct_int_input(rot_inp,1,8): 
            rot_inp = input(f"Invalid input. Please input a rotation value from 1 to 8, inclusive.")
        return self.id, int(row_inp),int(col_inp),int(rot_inp)