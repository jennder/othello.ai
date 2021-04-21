from player_interface import PlayerInterface
from game_tree import GameTree
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
        tree = self.game_tree
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, 0)
        return random.choice(moves)
        