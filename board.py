from constants import BLACK, WHITE

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
        Color -> [Listof Posn]
        """
        valid = []
        occupied = self.__get_of_color(color)
        for loc in occupied:
            for dx in range(-1,2):
                for dy in range(-1,2):
                    maybe_valid = self.__get_line_end(loc, dx, dy, color)
                    if not maybe_valid == None:
                        valid.append(maybe_valid)
        return valid

    def apply_move(self, posn, player):
        """
        Assumes that the move is already legal for the given player,
        and places a token of that color at the given position.
        Posn Color -> Void
        """
        x, y = posn
        dir = None
        # Place at posn
        if self.__board[y][x] == None:
            self.__board[y][x] = player
        # Get end posn of surrounded line
        for dx in range(-1,2):
            for dy in range(-1,2):
                end = self.__get_line_end(posn, dx, dy, player, target=player)
                if not end == None:
                    dir = (dx, dy)
                    break
            else:
                continue
            break
        # Flip pieces in between
        dx,dy = dir
        x += dx
        y += dy
        while not (x,y) == end:
            self.__board[y][x] = player
            x += dx
            y += dy

    def render(self):
        for col in self.__board:
            col_str = [word if word else "mt" for word in col]
            print("".join(word.ljust(8) for word in col_str))

    def __get_line_end(self, start, dx, dy, color, target=None):
        """
        Gets coordinates of the first empty space after a continuous line of opponent
        pieces starting from the given position, where the direction is defined
        by dx dy within [-1,1]. The opponent piece color is the opposite of what is
        at the start position. If there is no valid bracket, returns None
        Posn Nat Nat Color, [Maybe Color] -> [Maybe Posn]
        """
        op_color = WHITE if color == BLACK else BLACK
        x, y = start
        x += dx
        y += dy
        if (self.__outside_board(x, y) or not self.__board[y][x] == op_color):
            return None # must be at least one in between and not out of bounds
        while (self.__board[y][x] == op_color):
            x += dx
            y += dy
        return (x,y) if self.__board[y][x] == target and not self.__outside_board(x, y) else None

    def __get_of_color(self, color):
        """
        Gets all the posns of the board that contain a piece of the given color
        Color -> [Listof Posn]
        """
        return [(x, y) for y, row in enumerate(self.__board) for x, token in enumerate(row) if token == color]

    def __outside_board(self, x, y):
        """
        Whether the given x y is out of bounds on the board
        Nat Nat -> Bool
        """
        return not x in range(0, self.BOARD_SIZE) or not y in range(0, self.BOARD_SIZE)
