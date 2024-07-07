import numpy as np
import random

from board import Board
from utils import check_move
from status_check import check_victory,list_M1s
from player import Player
from const import *

class Computer(Player):
    def __init__(self, id:int, level:int=EASY):
        super().__init__(id)
        self.level = level

    def easy(self,board:Board):
        while True:
            row = random.randint(0,BOARD_SIZE-1)
            col = random.randint(0,BOARD_SIZE-1)
            rot = random.randint(1,8)
            if check_move(board.board, row, col):
                return self.id,row,col,rot
    
    def medium(self,board:Board):
        # take note: to block a winning move, the AI most likely has to take an enemy winning position and make a move such that
        # it reaches a M2 state for the opponent,as if it reaches a M1 state, the opponent just wins anyway.
        # and of course it should never make a move where it is a M0 in the first place.

        moves = list_M1s(board,self.id,self.id) # already account for valid move.
        if moves:
            num_pos_moves = len(moves)
            _,row,col,rot = moves[random.randint(0,num_pos_moves-1)]
            if not rot:
                rot = random.randint(1,8)
            return self.id,row,col,rot

        return self.easy(board)

    def request_move(self,board:Board):
        if self.level == EASY:
            return self.easy(board)
        if self.level== MEDIUM:
            return self.medium(board)

        