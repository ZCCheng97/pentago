import numpy as np

def check_move(board,row,col):
    """Checks if move is valid.

    Args:
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
    