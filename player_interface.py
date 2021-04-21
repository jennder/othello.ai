"""Represents interface for any AI player
"""
class PlayerInterface:

    def __init__(self):
        self.game_tree = None
        self.color = None

    def get_move(self):
        """
        Returns the maximal move for this AI player.

        void -> Posn
        """
        pass

    def set_color(self, color):
        """
        Let this player know their color.
        Should only be set once, ignore all other calls after the first

        Color -> void
        """
        if self.color is None:
            self.color = color

    def update_move(self, move):
        """
        Update the game tree with the given move to a tree with the next state

        Posn -> Void
        """
        self.game_tree = self.game_tree.apply_move(move)

    def set_gametree(self, tree):
        """
        Set this game tree with the given tree

        GameTree -> Void
        """
        self.game_tree = tree
