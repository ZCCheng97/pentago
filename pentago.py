import numpy as np

from utils import display_board, check_move, apply_move
from status_check import check_victory
from computer import computer_move

# remember to check_victory before and after rotation. 
# to refactor further
def menu():
    turn_num = 1
    board_input = np.zeros((6,6))
    row_str = ""
    col_str = ""
    rot_str = ""
    ai_or_player = ""
    win_con = 0
    ai_difficulty = ""
    int_difficulty = 0
    print("Welcome to Pentago! 5 in a row wins!")
    while ai_or_player not in ["ai","pvp"]:
        ai_or_player = input("Key in \"pvp\" to play against a friend \nor \"ai\" to play against the computer AI:")
    if ai_or_player == "ai":
        while ai_difficulty not in ["1","2"]:
            ai_difficulty = input("Enter AI level (1 for easy, 2 for medium):")
        int_difficulty = int(ai_difficulty)
        print("Player 1 goes first.")
        while win_con == 0:
            if turn_num % 2 == 1:
                while row_str not in ["0", "1", "2", "3", "4", "5"]:
                    row_str = input("Input a row number from 0 to 5:")
                row_input = int(row_str)
                while col_str not in ["0", "1", "2", "3", "4", "5"]:
                    col_str = input("Input a column number from 0 to 5:")
                col_input = int(col_str)
                while rot_str not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    rot_str = input("Input a rotation number from 1 to 8:")
                rot_input = int(rot_str)
                turn_input = 1
                if check_move(board_input, row_input, col_input):
                    apply_move(board_input, turn_input, row_input, col_input, 0)
                    # check victory here, but with rot input of 0
                    if check_victory(board_input, turn_num, 0) == 1:
                        print(display_board(board_input))
                        print("Player 1 wins!")
                        break
                    apply_move(board_input, turn_input, row_input, col_input, rot_input)
                    turn_num += 1
                else:
                    print("That's not a valid move")
                win_con = check_victory(board_input, turn_num, rot_input)
                print(display_board(board_input))
                print("Current turn number:", turn_num)
                row_str = ""
                col_str = ""
                rot_str = ""
                if win_con == 1:
                    print("Player 1 wins!")
                    break
                if win_con == 2:
                    print("Player 2 wins!")
                    break
                if win_con == 3:
                    print("Draw!")
                    break
            if turn_num % 2 == 0:
                row_input, col_input, rot_input = computer_move(board_input, 2, int_difficulty)
                turn_input = 2
                if check_move(board_input, row_input, col_input):
                    apply_move(board_input, turn_input, row_input, col_input, 0)
                    # check victory here, but with rot input of 0
                    if check_victory(board_input, turn_num, 0) == 2:
                        print(display_board(board_input))
                        print("Player 2 wins!")
                        break
                    apply_move(board_input, turn_input, row_input, col_input, rot_input)
                    turn_num += 1
                else:
                    print("That's not a valid move")
                win_con = check_victory(board_input, turn_num, rot_input)
                print(display_board(board_input))
                print("Current turn number:", turn_num)
                row_str = ""
                col_str = ""
                rot_str = ""
                if win_con == 1:
                    print("Player 1 wins!")
                    break
                if win_con == 2:
                    print("Player 2 wins!")
                    break
                if win_con == 3:
                    print("Draw!")
                    break
    if ai_or_player == "pvp":
        while win_con == 0:
            while row_str not in ["0","1","2","3","4","5"]:
                row_str = input("Input a row number from 0 to 5:")
            row_input = int(row_str)
            while col_str not in ["0","1","2","3","4","5"]:
                col_str = input("Input a column number from 0 to 5:")
            col_input = int(col_str)
            while rot_str not in ["1","2","3","4","5","6","7","8"]:
                rot_str = input("Input a rotation number from 1 to 8:")
            rot_input = int(rot_str)
            if turn_num%2 == 1:
                turn_input = 1
                if check_move(board_input,row_input,col_input):
                    apply_move(board_input,turn_input,row_input,col_input,0)
                    #check victory here, but with rot input of 0
                    if check_victory(board_input,turn_num,0) == 1:
                        print(display_board(board_input))
                        print("Player 1 wins!")
                        break
                    apply_move(board_input,turn_input,row_input,col_input,rot_input)
                    turn_num += 1
                else:
                    print("That's not a valid move")
                win_con = check_victory(board_input, turn_num, 0)
                print(display_board(board_input))
                print("Current turn number:", turn_num)
                row_str = ""
                col_str = ""
                rot_str = ""
                if win_con == 1:
                    print("Player 1 wins!")
                    break
                if win_con == 2:
                    print("Player 2 wins!")
                    break
                if win_con == 3:
                    print("Draw!")
                    break

            elif turn_num%2 == 0:
                turn_input = 2
                if check_move(board_input, row_input, col_input):
                    apply_move(board_input, turn_input, row_input, col_input, 0)
                    # check victory here, but with rot input of 0
                    if check_victory(board_input, turn_num, 0) == 2:
                        print(display_board(board_input))
                        print("Player 2 wins!")
                        break
                    apply_move(board_input, turn_input, row_input, col_input, rot_input)
                    turn_num += 1
                else:
                    print("That's not a valid move")
                win_con = check_victory(board_input,turn_num,0)
                print(display_board(board_input))
                print("Current turn number:", turn_num)
                row_str = ""
                col_str = ""
                rot_str = ""
                if win_con == 1:
                    print("Player 1 wins!")
                    break
                if win_con == 2:
                    print("Player 2 wins!")
                    break
                if win_con == 3:
                    print("Draw!")
                    break

