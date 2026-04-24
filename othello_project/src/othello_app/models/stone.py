from enum import IntEnum


#コマを定義するクラス
class Stone(IntEnum):
    WHITE = -1
    EMPTY = 0
    BLACK = 1

    FLIPPABLE = 5

    SQUARES_NUMBER = 64
    BOARD_SIDE_LENGTH = 8
        

