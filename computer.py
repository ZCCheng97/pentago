import numpy as np
import random

from board import Board
from utils import check_move
from status_check import check_victory
from player import Player
from const import *

class Computer(Player):
    def __init__(self, id:int, level:int=EASY):
        super().__init__(id)
        self.level = level

    def random_move(self,board:np.ndarray):
        while True:
            row = random.randint(0,BOARD_SIZE-1)
            col = random.randint(0,BOARD_SIZE-1)
            rot = random.randint(1,8)
            if check_move(board, row, col):
                return self.id,row,col,rot

    def request_move(self,board:np.ndarray):
        if self.level == EASY:
            return self.random_move(board)

        # if self.level == 2:
        #     pass
        #     possible_moves = 0
        #     winning_array = []
        #     winning_row = 6
        #     winning_col = 6
        #     winning_rot = 9
        #     blocking_coord = []
        #     blocking_coordlist = []
        #     tempboard = board.copy()

        #     # AI checks for possible winning moves

        #     for rot_iter in range(9):
        #         tempboard = board.copy()
        #         rotate(tempboard, rot_iter)
        #         for row_iter in range(6):
        #             for col_iter in range(6):
        #                 if check_move(board, row_iter, col_iter):
        #                     tempboard[row_iter, col_iter] = turn
        #                     if check_victory(tempboard, turn, 0) == turn:
        #                         tempboard[row_iter, col_iter] = 10
        #                         rotate(tempboard, rot_iter)
        #                         rotate(tempboard, rot_iter)
        #                         rotate(tempboard, rot_iter)
        #                         winning_array = np.where(tempboard == 10)
        #                         winning_row = int(winning_array[0])
        #                         winning_col = int(winning_array[1])
        #                         winning_rot = rot_iter
        #                         possible_moves += 1
        #                         rotate(tempboard, rot_iter)
        #                 tempboard = board.copy()
        #                 rotate(tempboard, rot_iter)
        #     if possible_moves >= 1:
        #         if check_move(board, winning_row, winning_col):
        #             return winning_row, winning_col, winning_rot
        #         else:
        #             possible_moves = 0

        #     # AI checks if opponent has winning moves

        #     if possible_moves == 0:
        #         for rot_iter in range(9):
        #             tempboard = board.copy()
        #             rotate(tempboard, rot_iter)
        #             for row_iter in range(6):
        #                 for col_iter in range(6):
        #                     if check_move(board, row_iter, col_iter):
        #                         tempboard[row_iter, col_iter] = abs(turn-3)
        #                         if check_victory(tempboard, turn, 0) == abs(turn-3):
        #                             tempboard[row_iter, col_iter] = 10
        #                             rotate(tempboard, rot_iter)
        #                             rotate(tempboard, rot_iter)
        #                             rotate(tempboard, rot_iter)
        #                             winning_array = np.where(tempboard == 10)
        #                             winning_row = int(winning_array[0])
        #                             winning_col = int(winning_array[1])
        #                             winning_rot = rot_iter
        #                             blocking_coord = [winning_row, winning_col]
        #                             blocking_coordlist.append(blocking_coord)
        #                             possible_moves += 1
        #                             rotate(tempboard, rot_iter)
        #                     tempboard = board.copy()
        #                     rotate(tempboard, rot_iter)

        #         if possible_moves >= 1 and all(x == blocking_coordlist[0] for x in blocking_coordlist):
        #             if check_move(board, winning_row, winning_col):
        #                 return winning_row, winning_col, winning_rot
        #             else:
        #                 while True:
        #                     rand_row = random.randint(0, 5)
        #                     rand_col = random.randint(0, 5)
        #                     rand_rot = random.randint(1, 8)
        #                     if check_move(board, rand_row, rand_col):
        #                         return rand_row, rand_col, rand_rot

        #     # AI makes random move if it neither has winning moves, nor if the opponent has winning moves

        #     while True:
        #         rand_row = random.randint(0, 5)
        #         rand_col = random.randint(0, 5)
        #         rand_rot = random.randint(1, 8)
        #         if check_move(board, rand_row, rand_col):
        #             return rand_row, rand_col, rand_rot


# print(Computer(1).request_move(Board().board))