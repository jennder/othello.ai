from constants import BLACK, WHITE

"""
Game Tree where the current state is the state of the board and the current turn, and
the children are a mapping of possible actions to GameTrees with the resulting board state 
"""
class GameTree:
    def __init__(self, board, curr_turn, children = {}):
        self.board = board
        self.curr_turn = curr_turn
        self.children = children

    def is_game_over(self):
        """
        Whether the game has ended, when neither player can make another move
        """
        # TODO
        return False

    def get_actions(self):
        """
        Lazily generates the next layer of the tree and returns the list of valid
        actions from the current state
        """
        # TODO
        return {}

    def apply_move(self, move):
        """
        Applies the given move to the current state and updates the tree to the next
        state if it is valid.
        Posn -> [Maybe GameTree]
        """
        # TODO
        return self