import numpy as np

from utils import correct_int_input, check_move
from status_check import check_victory
from computer import Computer
from const import *
from board import Board
from player import Player

# remember to check_win before and after rotation. 
class Pentago:
    def __init__(self):
        self.state = SETUP
        self.board = None
        self.turn_num = 1
        self.players = dict()
        
    def setup(self):
        temp_inp = ""
        print("Welcome to Pentago! 5 in a row wins!")
        while not correct_int_input(temp_inp,lower=PVP,upper=PVA):
            temp_inp = input("Key in 1 to play against a friend \nor 2 to play against the computer AI:")
        self.board = Board()
        self.state = int(temp_inp)
        
    def pva(self):
        difficulty = ""
        while not correct_int_input(difficulty,lower=EASY,upper=MEDIUM):
            difficulty = input("Enter AI level (0 for easy, 1 for medium):")
        self.players[1] = Player(1)
        self.players[2] = Computer(2,int(difficulty))

        while self.state != ENDED:
            curr_player = self.turn_num%2 if self.turn_num%2 else 2
            print(f"Player {curr_player}'s turn. {self.turn_num} turns have elapsed.")
            print(f"Current board state:")
            self.board.display_board()
            turn,row,col,rot = self.players[curr_player].request_move(self.board.board)
            
            while not check_move(self.board.board,row,col) and curr_player == 1:
                print(f"The move you entered was not valid.")
                turn,row,col,rot = self.players[curr_player].request_move(self.board.board)
            self.board.apply_move(turn,row,col,0)
            
            if check_victory(self.board,0):
                self.state = ENDED
                break
            self.board.rotate(rot)
            if check_victory(self.board,rot):
                self.state = ENDED
                break
            self.turn_num += 1

    def pvp(self):
        curr_player = ""
        while not correct_int_input(curr_player,lower=PLAYER_NUM,upper=PLAYER_NUM):
            curr_player = input("Enter the number of players:")
        for i in range(1,int(curr_player)+1):
            self.players[i] = Player(i)

        while self.state != ENDED:
            curr_player = self.turn_num%len(self.players) if self.turn_num%len(self.players) else len(self.players)
            print(f"Player {curr_player}'s turn. {self.turn_num} turns have elapsed.")
            print(f"Current board state:")
            self.board.display_board()
            turn,row,col,rot = self.players[curr_player].request_move(self.board.board)
            
            while not check_move(self.board.board,row,col):
                print(f"The move you entered was not valid.")
                turn,row,col,rot = self.players[curr_player].request_move(self.board.board)
            self.board.apply_move(turn,row,col,0)
            
            if check_victory(self.board,0):
                self.state = ENDED
                break
            self.board.rotate(rot)
            if check_victory(self.board,rot):
                self.state = ENDED
                break
            self.turn_num += 1

    def run(self):
        while self.state != ENDED:
            if self.state == SETUP:
                self.setup()
            elif self.state == PVA:
                self.pva()
            elif self.state == PVP:
                self.pvp()

# b = Board()
# b.board[0:3,0] = np.full((3,),2)
# b.board[4,0] = 2
# c = Computer(2,MEDIUM)
# print(b)
# print(c.request_move(b))