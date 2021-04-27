from player_interface import PlayerInterface
from constants import SKIP

"""A minimax player who maximizes their move assuming others are adversarial
players, with alpha beta pruning. Depth of 2 by default.
"""
class AlphaBetaPlayer(PlayerInterface):

    def __init__(self, depth=2):
        super().__init__()
        self.DEPTH = depth

    def get_move(self, board):
        """
        Returns the maximal move for this AI player.

        Board -> Posn
        """
        tree = self.game_tree
        return self.max_value(tree, self.DEPTH, -float("inf"), float("inf"))[0]

    def max_value(self, tree, depth, alpha, beta):
        """
        Maximizes the value for this AI player with alpha beta pruning,
        and assuming the opponent will minimize the score. Does alpha beta pruning.

        GameTree Nat int int -> (Tupleof Posn Nat)
        """
        # the game has ended
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, tree.get_score(self.color))

        best_val = -float("inf")
        for action in moves:
            val_action = self.min_value(tree.children[action], depth, alpha, beta)[1]
            if val_action > best_val:
                best_action = action
                best_val = val_action
            alpha = max(alpha, best_val)
            if beta < alpha:
                break
        return (best_action, best_val)

    def min_value(self, tree, depth, alpha, beta):
        """
        When it is the opponent player's turn, they will minimize this player's score.
        Does alpha beta pruning.

        GameTree Nat int int -> (Tupleof Posn Nat)
        """
        # the game has ended
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, tree.get_score(self.color))

        best_val = float("inf")
        for action in moves:
            if depth == 1:
                val_action = tree.children[action].get_score(self.color)
            else:
                val_action = self.max_value(tree.children[action], depth - 1, alpha, beta)[1]

            if val_action < best_val:
                best_val = val_action
                best_action = action
            beta = min(beta, best_val)
            if beta < alpha:
                break
        return (best_action, best_val)
