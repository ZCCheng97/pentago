import numpy as np
from const import rotations

def display_board(board):
    return board

def apply_move(board,turn,row,col,rot):
    
    # move added
    board[row, col] = turn

    # returns board with rotation input
    return rotate(board,rot)

def check_move(board: np.ndarray,row,col):
    """Checks if move is valid.

    Args:
        board (np.ndarray): The game board.
        row (int): Row idx, between 0 and len(board)-1.
        col (int): Col idx, between 0 and len(board[0])-1.

    Returns:
        bool: True if move is valid, False if otherwise.
    """
    if row >= 6 or col >= 6:
        return False
    if board[row,col] == 1 or board[row,col] == 2:
        return False
    else:
        return True

def rotate(board: np.ndarray, rot: int):
  """Rotates the chosen quadrant of the board clockwise or anticlockwise.

  Args:
      board (np.ndarray): The game board
      rot (int): The integers 1 to 8 each signifying one of the 4 quadrants and 1 of 2 rotational directions.

  Returns:
      np.ndarray: The rotated board.
  """
  rotation = rotations[rot]
  rows,cols = rotation["rowcols"]
  turns = rotation["turn"]
  return np.rot90(board[rows,cols],turns)

def subsetter(board: np.ndarray, dims: int = 5):
    """Generates an array of board subsets of shape (dims, dims), to facilitate checks of rows, cols or diagonals
    of len(dims).

    Args:
        board (np.ndarray): The game board
        dims (int, optional): The (dims, dims) size to subset from the board. Defaults to 5.

    Returns:
        np.ndarray: A 3D nd.array of the subsections of the original board.
  """
    assert board.shape[0] == board.shape[1], "board.shape must be equal in size."
    assert dims <= len(board), "Chosen dims must be smaller or equal to dimensions of the board."
  
    output = list()
    rows, cols = board.shape
    for rowIdx in np.arange(rows-dims+1):
        for colIdx in np.arange(cols-dims+1):
            output.append(board[np.arange(rowIdx,rowIdx+dims),np.arange(colIdx,colIdx+dims)])
    return np.array(output)

def get_all_series(board: np.ndarray):
    """Returns all possible rows, columns and both diagonals of a given board.

    Args:
        board (np.ndarray): The game board.

    Returns:
        np.ndarray: A 2D array containing all the 1D rows, columns and diagonals.
    """
    return np.vstack((board,board.T,board.diagonal(),np.rot90(board).diagonal()))
    