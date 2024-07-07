import numpy as np

from utils import get_all_series, subsetter,check_move
from const import * 
from board import Board

# For checking winning moves.

def checkSeries(series: np.ndarray):
  """Takes a 1D numpy array and returns the found digit if all digits are the same, otherwise 0.

  Args:
      series (np.ndarray): A 1D np.ndarray.

  Returns:
      int: Returns either the first element of the array if all elements are the same, 0 if otherwise.
  """
  assert series.ndim == 1, "Series must be a 1D numpy array."

  return series[0] if np.all(series == series[0]) else 0

def check_subboard_win(board: np.ndarray, player_num:int = 2):
  """Checks the subsection of the board if there is a winner along a row, column or diagonal.

  Args:
      board (np.ndarray): The subsection of the game board.

  Returns:
      int: -1 if a draw is found, else the winner's id, or 0 if no winner is found.
  """
  winning_player = np.array([False]*player_num)
  series = get_all_series(board)

  for serie in series:
    winner = checkSeries(serie)
    if winner > 0:
      winning_player[winner-1] = True
  
  if winning_player.sum() > 1:
    return -1
  elif winning_player.sum() == 1:
    return winning_player.argmax()+1
  else:
    return 0
  
def check_win(board: np.ndarray,player_num:int = 2):
    """Checks who the winning player is. 

    Args:
        board (np.ndarray): The game board.
        player_num (int, optional): Number of players. Defaults to 2.

    Returns:
        int: -1 if a draw is found, else the winner's id, or 0 if no winner is found.
    """
    
    wincon = np.array([False]*player_num)
    tempboard = board.copy()
    sub_boards = subsetter(tempboard)
    for sub_board in sub_boards:
        win_status = check_subboard_win(sub_board)
        if win_status == -1:
            return -1
        elif win_status:
            wincon[win_status-1] = True

    if (wincon.sum() > 1 or
        (np.count_nonzero(board) == 36)):
        return -1
    elif wincon.sum() == 1:
        return wincon.argmax()+1
    else:
        return 0

def check_victory(board:Board, rot, player_num:int=2):
    board =  board.copy()
    check = check_win(board.board)
    if check:
        board.display_board()
        print("The game has ended in a draw! Game over.") if check == -1 else  print(f"Player {check} has won! Game over.")
        return check

    board.rotate(rot)

    check = check_win(board.board)
    if check:
        board.display_board()
        print("The game has ended in a draw! Game over.") if check == -1 else  print(f"Player {check} has won! Game over.")
        return check
    return 0

def list_M1s(board:Board, player_id:int=2, winning_player:int=2):
    rows,cols = board.board.shape
    outputs = list()
    for row in range(rows):
       for col in range(cols):
          for rot in range(8):
            board_copy = board.copy()
            if check_move(board_copy.board, row, col):
                board_copy.apply_move(player_id,row,col,rot)
                if check_win(board_copy.board) == winning_player:
                    outputs.append((player_id, row, col, rot))
    return outputs
             

