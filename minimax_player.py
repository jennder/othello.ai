from player_interface import PlayerInterface
from game_tree import GameTree
from constants import SKIP
import math
from operator import ge, le

"""A minimax player who maximizes their move assuming
others are adversarial players. Depth of 2 by default.
"""
class MinimaxPlayer(PlayerInterface):

    def __init__(self, depth=2):
        super().__init__()
        self.depth = depth

    def get_move(self, board):
        """
        Returns the maximal move for this AI player.

        Board -> Posn
        """
        tree = self.game_tree
        best_action = self.get_minimax_score(tree, self.depth * 2) # *2 for num players
        return best_action[0]
    
    def get_minimax_score(self, tree, depth):
        """
        Compute the minimax move and score for this player.
        Depth is mumber of layers of tree to look through, and number of turns for this player.

        GameTree Natural -> (Move, Natural)
        """
        # the game has ended
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, tree.get_score(self.color))
        move_score = []
        maximize = tree.curr_turn == self.color

        if depth == 1:
            for m in moves:
                next_game = tree.children[m]
                next_score = next_game.get_score(self.color)
                move_score.append((m, next_score))
        else:
            for m in moves:
                next_game = tree.children[m]
                next_move_score = self.get_minimax_score(next_game, depth - 1)
                next_score = next_move_score[1]
                move_score.append((m, next_score))
        return self.get_best_action(maximize, move_score)

    def get_best_action(self, maximize, move_scores):
        """
        Get the best move, either maximize or minimize the score

        Boolean [Listof (Move, Natural)] -> (Move, Natural)
        """
        best_score = math.inf
        best_move = None
        comparator = ge if maximize else le
        if maximize:
            best_score *= -1
        for move_score in move_scores:
            move, score = move_score

            if comparator(score, best_score):
                best_score = score
                best_move = move
        return (best_move, best_score)
