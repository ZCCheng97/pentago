BOARD_SIZE = 6 # size of board (should always be an EVEN value!)
WIN_CONDITION = 5 # how many in a row to win (should always be SMALLER than BOARD_SIZE)
PLAYER_NUM = 2

DRAW = -1

# Game states
SETUP = 0
PVP = 1
PVA = 2
ENDED = 3

# AI Difficulties
EASY = 0
MEDIUM = 1
HARD = 2
INSANE = 3

board_quadrants = {"tr":(slice(0,BOARD_SIZE//2),slice(BOARD_SIZE//2,BOARD_SIZE)),
                   "br":(slice(BOARD_SIZE//2,BOARD_SIZE),slice(BOARD_SIZE//2,BOARD_SIZE)),
                   "bl":(slice(BOARD_SIZE//2,BOARD_SIZE),slice(BOARD_SIZE//2)),
                   "tl":(slice(BOARD_SIZE//2),slice(BOARD_SIZE//2)),}

turn_direction = {"cw":-1,
                  "ccw":1}

rotations = {1: {"rowcols":board_quadrants["tr"],
            "turn":turn_direction["cw"]},
            2: {"rowcols":board_quadrants["tr"],
            "turn":turn_direction["ccw"]},
            3: {"rowcols":board_quadrants["br"],
            "turn":turn_direction["cw"]},
            4: {"rowcols":board_quadrants["br"],
            "turn":turn_direction["ccw"]},
            5: {"rowcols":board_quadrants["bl"],
            "turn":turn_direction["cw"]},
            6: {"rowcols":board_quadrants["bl"],
            "turn":turn_direction["ccw"]},
            7: {"rowcols":board_quadrants["tl"],
            "turn":turn_direction["cw"]},
            8: {"rowcols":board_quadrants["tl"],
            "turn":turn_direction["ccw"]}}