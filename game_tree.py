from constants import BLACK, WHITE, SKIP

"""
Game Tree where the current state is the state of the board and the current turn, and
the children are a mapping of possible actions to GameTrees with the resulting board state 
"""
class GameTree:
    def __init__(self, board, curr_turn, children=None):
        self.board = board
        self.curr_turn = curr_turn
        self.children = children or {}

    def __eq__(self, other):
        return type(other) is GameTree and self.board == other.board

    def __ne__(self, other):
        return type(other) is not GameTree and self.board != other.board

    def is_game_over(self):
        """
        Whether the game has ended, when neither player can make another move
        # TODO check if this is actually the condition where game over

        void -> Boolean
        """
        return len(self.board.get_valid_moves(BLACK)) == 0 and \
            len(self.board.get_valid_moves(WHITE)) == 0

    def get_actions(self):
        """
        Lazily generates the next layer of the tree and returns the next layer of the 
        game tree, a mapping of moves to the next game tree state

        void -> {Move : GameTree}
        """
        moves = self.board.get_valid_moves(self.curr_turn)
        for m in moves:
            self.apply_move(m)
        if len(moves) == 0:
            self.apply_move(SKIP)
        return list(self.children.keys())

    def apply_move(self, move):
        """
        Applies the given move to the current state and updates the tree to the next
        state if it is valid.
        Posn -> [GameTree]
        """
        # lazy generation
        if move in self.children:
            return self.children[move]
        
        # otherwise need to generate the child
        if move == SKIP:
            self.children[move] = GameTree(self.board.copy(), self.next_turn())
        else:
            # TODO need to check if its valid? because board assumes it is valid
            next_board = self.board.apply_move(move, self.curr_turn)
            print(self.curr_turn)
            self.children[move] = GameTree(next_board, self.next_turn())
            print(self.curr_turn, self.next_turn(), "should be", self.children[move].curr_turn)
        return self.children[move] 
    
    def next_turn(self):
        """
        Get the player whose turn is next.
        
        void -> Color
        """
        if self.curr_turn == WHITE:
            return BLACK
        else:
            return WHITE

    def get_score(self, color):
        """
        Get the score for the given player in this game.

        Color -> Natural
        """
        return self.board.get_score(color)
