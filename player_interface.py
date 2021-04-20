"""Represents interface for any AI player
"""
class PlayerInterface:

    def get_move(self):
        """
        Returns the maximal move for this AI player.

        void -> Posn
        """
        pass

    def update_with_move(self, posn):
        """
        Used to update internal state of player's game tree.

        Posn -> void
        """
        pass

    def set_color(self, color):
        """
        Let this player know their color.

        Color -> void
        """
        pass

    def update_move(self, move):
        """TODO
        """
        pass

    def set_gametree(self, tree):
        """TODO
        """
        pass