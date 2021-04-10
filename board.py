from constants import BLACK, WHITE
import pprint as pp

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
        self.__board = [[None] * self.BOARD_SIZE for _ in range(0, self.BOARD_SIZE)]
        self.__initialize_board()

    def __initialize_board(self):
        """
        Start a new game of Othello with standard setup.
        Four alternating color pieces at center of board.
            - See README for exact positions
        """
        # white is at (3, 3) and (4, 4)
        self.__board[3][3] = WHITE
        self.__board[4][4] = WHITE
        # black is at (3, 4) and (4, 3)
        self.__board[3][4] = BLACK
        self.__board[4][3] = BLACK

    def get_valid_moves(self, color):
        """
        Returns all the valid posns on the board for the given player's turn.
        A valid move is one where the placing a piece of the given color results in 
        outflanking the other player's pieces in at least one of the 8 directions.
        Outflanking means that the given player pieces surrounds on both ends a consecutive
        line of the other player's pieces without gaps.
        Color -> List<Posn>
        """
        return []

    def apply_move(self, posn, player):
        """
        Assumes that the move is already legal for the given player,
        and places a token of that color at the given position.
        """
        self.__board[posn[0]][posn[1]] = player

    def render(self):
        pp.pprint(self.__board)
