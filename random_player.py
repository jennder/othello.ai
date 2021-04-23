from player_interface import PlayerInterface
from constants import SKIP
import random

"""A greedy player who maximizes their move to get maximize their
score on that move
"""
class RandomPlayer(PlayerInterface):

    def get_move(self, board):
        """
        Returns the a random move for this AI player from all possible moves
        with equal probability.

        Board -> Posn
        """
        moves = self.game_tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return SKIP
        return random.choice(moves)
        