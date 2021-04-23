
from minimax_player import MinimaxPlayer
from game_tree import GameTree
from constants import SKIP

"""Minimax player with added heuristics.
Heuristics include:
    - Corners occupied by this player (effectively a bonus on top of edges)
    - Pieces not in danger zone
    - Edges occupied by this player
"""
class HeuristicPlayer(MinimaxPlayer):
    
    def get_move(self, board):
        tree = self.game_tree
        best_action = self.get_minimax_score(tree, self.depth * 2) # *2 for num players
        return best_action[0]
    
    def get_minimax_score(self, tree, depth):
        """
        Compute the minimax move and score for this player, where score
        is the number of pieces this player has on the board plus points
        for the heuristics.

        GameTree Natural -> (Move, Natural)
        """
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
                next_score = next_game.get_score(self.color) + self.get_heuristic_score(tree)
                move_score.append((m, next_score))
        else:
            for m in moves:
                next_game = tree.children[m]
                next_move_score = self.get_minimax_score(next_game, depth - 1)
                next_score = next_move_score[1]
                move_score.append((m, next_score))
        return self.get_best_action(maximize, move_score)

    def get_heuristic_score(self, tree):
        """
        Get the heuristics score for this player. The heuristic is a combination
        of several observations on the game state:
            - Four corners
            - (Not) in danger zone
            - Edges
        """
        corners = tree.board.four_corners(self.color)
        danger = 20 - tree.board.num_in_danger(self.color) # cannot be negative, at max num_in danger returns 20
        edges = tree.board.num_edges(self.color)
        return corners + danger + edges