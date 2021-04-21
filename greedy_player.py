from player_interface import PlayerInterface
from game_tree import GameTree
from constants import SKIP

"""A greedy player who maximizes their move to get maximize their
score on that move
"""
class GreedyPlayer(PlayerInterface):

    def get_move(self, board):
        """
        Returns the maximal move for this AI player to have the highest score at the
        end of this move.

        Board -> Posn
        """
        tree = self.game_tree
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, 0)
        best = max(moves, key=lambda m: tree.children[m].get_score(self.color))
        return best
        