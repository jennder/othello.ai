from player_interface import PlayerInterface
from game_tree import GameTree
from constants import SKIP
import math
from operator import ge, le

"""A minimax player who maximizes their move assuming
others are adversarial players. Depth of 2 by default.
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
        return self.maxValue(tree, self.DEPTH, -float("inf"), float("inf"))[0]

    def maxValue(self, tree, depth, alpha, beta):
        # the game has ended
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, tree.get_score(self.color))

        bestVal = -float("inf")
        for action in moves:
            valForAction = self.minValue(tree.children[action], depth, 1, alpha, beta)[1]
            if valForAction > bestVal:
                bestAction = action
                bestVal = valForAction
            alpha = max(alpha, bestVal)
            if beta < alpha:
                break
        return (bestAction, bestVal)

    def minValue(self, tree, depth, agent, alpha, beta):
        # the game has ended
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, tree.get_score(self.color))

        bestVal = float("inf")
        for action in moves:
            if depth == 1:
                valForAction = tree.children[action].get_score(tree.curr_turn)
            else:
                valForAction = self.maxValue(tree.children[action], depth - 1, alpha, beta)[1]

            if valForAction < bestVal:
                bestVal = valForAction
                bestAction = action
            beta = min(beta, bestVal)
            if beta < alpha:
                break
        return (bestAction, bestVal)
