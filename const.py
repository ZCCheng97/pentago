board_quadrants = {"tr":(slice(0,3),slice(3,6)),
                   "br":(slice(3,6),slice(3,6)),
                   "bl":(slice(3,6),slice(3)),
                   "tl":(slice(3),slice(3)),}

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