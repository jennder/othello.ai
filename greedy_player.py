from player_interface import PlayerInterface
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
        moves = self.game_tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return SKIP
        best = max(moves, key=lambda m: self.game_tree.children[m].get_score(self.color))
        return best
        