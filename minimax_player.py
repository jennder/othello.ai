from player_interface import PlayerInterface
from game_tree import GameTree
from constants import SKIP
import copy
import math
from operator import ge, le

"""A minimax player who maximizes their move assuming
others are adversarial players.
"""
class MinimaxPlayer(PlayerInterface):
    DEPTH = 2 #TODO can change this

    def __init__(self):
        #TODO: needs game tree and its own color
        self.game_tree = None
        self.color = None

    def get_move(self, board):
        """
        Returns the maximal move for this AI player.

        Board -> Posn
        """
        #tree = GameTree(board, self.color) # TODO fix this to be lazy
        # a tuple of best move and the next state
        # board.render()
        print("getting turn for", self.color)
        tree = self.game_tree
        best_action = self.__get_minimax_score(tree, self.DEPTH * 2) # *2 for num players
        return best_action[0]
    
    def __get_minimax_score(self, tree, depth):
        """
        Compute the minimax move and score for this player.
        Depth is mumber of layers of tree to look through, and number of turns for this player.

        GameTree Natural -> (Move, Natural)
        """
        # the game has ended, this should never be reached
        if tree.is_game_over():
            return (None, tree.get_score(self.color))
        moves = copy.deepcopy(tree.get_actions())
        # moves = tree.get_actions()
        # Skip if there are no possible moves
        if (len(moves) == 0):
            return (SKIP, 0)
        move_score = []
        #print(moves.keys())
        maximize = tree.curr_turn == self.color
        # print("=== player", maximize, tree.curr_turn, self.color)
        # print(depth)
        if depth == 1:
            # print(len(moves))
            for m in moves:
                next_game = tree.children[m]
                next_score = next_game.get_score(self.color)
                move_score.append((m, next_score))
        else:
            for m in moves:
                # print(m, moves.keys())
                next_game = tree.children[m]
                # print(tree, next_game)


                next_move_score = self.__get_minimax_score(next_game, depth - 1)
                next_score = next_move_score[1]
                #TODO i have no idea if this will work :)
                move_score.append((m, next_score))
        best = self.get_best_action(maximize, move_score)
        # print(best, "\n\n")
        return best

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

    def set_color(self, color):
        """
        Let this player know their color.
        Should only be set once, ignore all other calls after the first

        Color -> void
        """
        if self.color is None:
            self.color = color

    def update_move(self, move):
        self.game_tree = self.game_tree.apply_move(move)

    def set_gametree(self, tree):
        self.game_tree = tree
        