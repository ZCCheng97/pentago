from board import Board
from status_check import *

b = Board()
b.apply_move(2,0,0)
b.rotate(3)

print(b)