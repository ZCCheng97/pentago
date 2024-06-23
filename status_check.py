import numpy as np

from utils import get_all_series, subsetter

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

def checkWin(board: np.ndarray):
  """Checks the subsection of the board if there is a winner along a row, column or diagonal.

  Args:
      board (np.ndarray): The subsection of the game board.

  Returns:
      int: 3 if a draw is found, else the winner 1 or 2, or 0 if no winner is found.
  """
  winning_player = {1:False,
                    2: False}
  series = get_all_series(board)

  for serie in series:
    winner = checkSeries(serie)
    if winner in winning_player:
      winning_player[winner] = True
  
  if winning_player[1] and winning_player[2]:
    return 3
  elif winning_player[1]:
    return 1
  elif winning_player[2]:
    return 2
  else:
    return 0
  
def check_victory(board: np.ndarray):
    wincon = {1:False,2:False,3:False}
    tempboard = board.copy()
    sub_boards = subsetter(tempboard)
    for sub_board in sub_boards:
        win_status = checkWin(sub_board)
        if win_status in wincon:
            wincon[win_status] = True

    if (wincon[3] or 
        (wincon[1] and wincon[2]) or
        (np.count_nonzero(board) == 36)):
        return 3
    elif wincon[1]:
        return 1
    elif wincon[2]:
        return 2
    else:
        return 0

# t = np.zeros((5,5))
# t[:,3] = np.ones((5,))+1 # controls 2s
# t[:,2] = np.ones((5,)) #controls 1s
# print(t)
# print(check_victory(t))