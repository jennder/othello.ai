from constants import BLACK, WHITE

"""A Board is represented by a 2-D array
- Represents a standard board for Othello
- Coordinate system (the initial board is shown):
    Posn is a (Nat[0, 7], Nat[0, 7])
            - Represents a position on the board (row, col)
    +-----+-----+-----+-----+-----+-----+-----+-----+
    | 0,0 | 1,0 | 2,0 |     |     |     |     | 7,0 |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    | 0,1 |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    | 0,2 |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |  w  |  b  |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |  b  |  w  |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    | 0,7 |     |     |     |     |     |     | 7,7 |
    +-----+-----+-----+-----+-----+-----+-----+-----+

Each position on board is one of: Color or None
    - if color, that player is on the board at that position
    - if None, there is no one on that position
"""
class Board:
    BOARD_SIZE = 8
    def __init__(self):
        self.board = [[None] * self.BOARD_SIZE for _ in range(0, self.BOARD_SIZE)]
        self.__initialize_board()

    def __eq__(self, other):
        return type(other) is Board and self.board == other.board

    def __initialize_board(self):
        """
        Start a new game of Othello with standard setup.
        Four alternating color pieces at center of board.
            - See README for exact positions
        """
        # white is at (3, 3) and (4, 4)
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        # black is at (3, 4) and (4, 3)
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK

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
        occupied = self.__get_of_color(self, color)
        for loc in occupied:
            for dx in range(-1,2):
                for dy in range(-1,2):
                    maybe_valid = self.__get_line_end(self, loc, dx, dy, color)
                    if not maybe_valid == None:
                        valid.append(maybe_valid)
        return valid

    def apply_move(self, posn, player):
        """
        Assumes that the move is already legal for the given player,
        and places a token of that color at the given position.

        Posn Color -> Board
        """
        new_board = self.copy()
        x, y = posn
        dirs = []
        # Place at posn
        if new_board.board[y][x] == None:
            new_board.board[y][x] = player
        # Get end posn of surrounded line
        for dx in range(-1,2):
            for dy in range(-1,2):
                end = self.__get_line_end(new_board, posn, dx, dy, player, target=player)
                if not end == None:
                    dirs.append(((dx, dy), end))

        # Flip pieces in between
        for dir in dirs:
            delta, target = dir
            dx, dy = delta
            x, y = posn
            x += dx
            y += dy
            while not (x,y) == target:
                new_board.board[y][x] = player
                x += dx
                y += dy
        return new_board

    def render(self):
        """
        Textual representation of this Board.
        """
        for col in self.board:
            col_str = [word if word else "mt" for word in col]
            print("".join(word.ljust(8) for word in col_str))

    def get_score(self, player):
        """
        Gets the score of the given player by how many pieces they have on the board
        Color -> Nat
        """
        return len(self.__get_of_color(self, player))

    def __get_line_end(self, board, start, dx, dy, color, target=None):
        """
        Gets coordinates of the first empty space after a continuous line of opponent
        pieces starting from the given position, where the direction is defined
        by dx dy within [-1,1]. The opponent piece color is the opposite of what is
        at the start position. If there is no valid bracket, returns None
        Board Posn Nat Nat Color [Maybe Color] -> [Maybe Posn]
        """
        op_color = WHITE if color == BLACK else BLACK
        x, y = start
        x += dx
        y += dy
        if (self.__outside_board(x, y) or not board.board[y][x] == op_color):
            return None # must be at least one in between and not out of bounds
        while (board.board[y][x] == op_color):
            x += dx
            y += dy
            if self.__outside_board(x, y):
                return None
        return (x,y) if board.board[y][x] == target and not self.__outside_board(x, y) else None

    def __get_of_color(self, board, color):
        """
        Gets all the posns of the board that contain a piece of the given color
        Board Color -> [Listof Posn]
        """
        return [(x, y) for y, row in enumerate(board.board) for x, token in enumerate(row) if token == color]

    def __outside_board(self, x, y):
        """
        Whether the given x y is out of bounds on the board
        Nat Nat -> Bool
        """
        return not x in range(0, self.BOARD_SIZE) or not y in range(0, self.BOARD_SIZE)

    def copy(self):
        """
        Create deep copy of this board.

        void -> Board
        """
        new_board = Board()
        new_board.board = [row[:] for row in self.board]
        return new_board

    def four_corners(self, color):
        """
        Get number of corners occupied by given player color.

        Color -> Nat
        """
        count = 0
        edge = self.BOARD_SIZE - 1
        if self.occupied_by(color, 0, 0):
            count += 1
        if self.occupied_by(color, 0, edge):
            count += 1
        if self.occupied_by(color, edge, 0):
            count += 1
        if self.occupied_by(color, edge, edge):
            count += 1

        return count

    def occupied_by(self, color, row, col):
        """Is the tile occupied by the given color?

        Color Nat[0, 7] Nat[0, 7] -> Boolean
        """
        return self.board[row][col] == color

    def check_row(self, color, row, lower, upper):
        """
        Get number of tiles occupied by given player color in given row
        for tiles in columns [lower, upper]

        Color Nat[0, 7] Nat[0, 7] Nat[0, 7] -> Nat
        """
        count = 0
        for col in range(lower, upper + 1):
            if self.occupied_by(color, row, col):
                count += 1

        return count

    def check_col(self, color, col, lower, upper):
        """
        Get number of tiles occupied by given player color in given col
        for tiles in rows [lower, upper]

        Color Nat[0, 7] Nat[0, 7] Nat[0, 7] -> Nat
        """
        count = 0
        for row in range(lower, upper + 1):
            if self.occupied_by(color, row, col):
                count += 1
        return count

    def num_in_danger(self, color):
        """
        Return the number of pieces the given player color has in the danger zone.
        The danger zone in Othello is defined as all tiles 1 away from each edge:
        +-----+-----+-----+-----+
        |     |     |     |       ...
        +-----+-----+-----+-----+
        |     |  x  |  x  |  x                  # shown: top left of board
        +-----+-----+-----+-----+
        |     |  x  |     | 
        +-----+-----+-----+-----+
        |     |  x  |     | 
        ...

        Color -> Nat
        """
        edge = self.BOARD_SIZE - 2
        top = self.check_row(color, 1, 1, edge)
        bottom = self.check_row(color, edge, 1, edge)
        left = self.check_col(color, 1, 2, edge - 1) # don't count corners twice
        right = self.check_col(color, edge, 2,  edge - 1)
        return top + bottom + left + right

    def num_edges(self, color):
        """
        Return the number of pieces the given player has on edges:
        +-----+-----+-----+
        |  x  |  x  |  x
        +-----+-----+-----+
        |  x  |     | ...           # shown: top left of board
        +-----+-----+-----+
        |  x  | ... | ...
        +-----+-----+-----+
        """
        edge = self.BOARD_SIZE - 1
        top = self.check_row(color, 0, 0, edge)
        bottom = self.check_row(color, edge, 0, edge)
        left = self.check_col(color, 0, 1, edge - 1) # don't count corners twice
        right = self.check_col(color, edge, 1, edge - 1)
        return top + bottom + left + right