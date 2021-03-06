from player_interface import PlayerInterface
from constants import SKIP
import random

"""A player who does iterative deepening search.
Maxes out at depth search 6 (for timing efficiency)
"""
class IterativeDeepeningPlayer(PlayerInterface):
    def __init__(self, depth=6):
        super().__init__()
        self.depth = depth

    def get_move(self, board):
        """
        Returns the maximal move for this AI player to have the highest score at the
        end of this move.

        Board -> Posn
        """
        for d in range(0, self.depth):
            winning_moves = self.__depth_limited(d)
            if winning_moves is not False and len(winning_moves) > 0:
                return winning_moves[0]
            
        # if no good moves exist to get to goal state, default to a random move
        all_moves = self.game_tree.get_actions()
        if len(all_moves) == 0:
            return SKIP
        else:
            return random.choice(all_moves)
        
    def __depth_limited(self, depth_cutoff):
        initial = (self.game_tree, [])
        frontier = [initial]
        while len(frontier) > 0:
            curr, path = frontier[-1]
            frontier = frontier[:-1] #remove curr state from frontier
            if self.__goal_test(curr):
                return path
            else:
                if len(path) < depth_cutoff:
                    moves = self.game_tree.get_actions()
                    for m in moves:
                        child = self.game_tree.children[m]
                        new_path = path[:] #copy the path
                        new_path.append(m)
                        frontier.append((child, new_path))
        return False
        
    def __goal_test(self, tree):
        """Is the state the goal state?

        GameTree -> Boolean
        """ 
        leader = tree.get_leader() == self.color
        corners = tree.board.four_corners(self.color) > 0
        #TODO determine what a goal state is
        return leader or corners