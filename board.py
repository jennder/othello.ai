"""A Board is represented by a 2-D array
- Represents a standard board for Othello
- Coordinate system, see README

Each position on board is one of: Color or None
    - if color, that player is on the board at that position
    - if None, there is no one on that position
"""
class Board:
    BOARD_SIZE = 8
    def __init__(self):
        #TODO
        self.__board = [[None] * BOARD_SIZE] * BOARD_SIZE
        self.__initialize_board()

    def __initialize_board(self):
        """Start a new game of Othello with standard setup.
        Four alternating color pieces at center of board.
            - See README for exact positions
        """
        # white is at (3, 3) and (4, 4)
        self.__board[3][3] = "white"
        self.__board[4][4] = "white"
        # black is at (3, 4) and (4, 3)
        self.__board[3][4] = "black"
        self.__board[4][3] = "black"

