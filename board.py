import numpy as np

from const import BOARD_SIZE,rotations

class Board:
    def __init__(self, dims: int=BOARD_SIZE):
        self.board = np.zeros((dims,dims),dtype=np.int8)
    
    def __str__(self):
        return np.array2string(self.board, separator=' ')
    
    def copy(self):
       copy = Board(dims = BOARD_SIZE)
       copy.board = self.board.copy()
       return copy
    
    def __call__(self): 
        return self.board
    
    def display_board(self):
        # Convert the array to a string for better formatting
        board_str = np.array2string(self.board, separator=' ')
        print(board_str)
      
    def rotate(self, rot: int):
      """Rotates the chosen quadrant of the board clockwise or anticlockwise.

      Args:
          board (np.ndarray): The game board
          rot (int): The integers 1 to 8 each signifying one of the 4 quadrants and 1 of 2 rotational directions.

      Returns:
          np.ndarray: The rotated board.
      """
      if not rot: 
        return None
      rotation = rotations[rot]
      rows,cols = rotation["rowcols"]
      turns = rotation["turn"]
      self.board[rows,cols] = np.rot90(self.board[rows,cols], k= turns)

    def apply_move(self,turn: int,row: int,col: int, rot: int=0):
      # move added
      self.board[row, col] = turn
      self.rotate(rot)