from constants import BLACK, WHITE
from board import Board
from game_tree import GameTree

"""
The referee oversees the playing of a game of Othello between two players,
ensures that valid moves are made, and determines the winner.
"""
class Referee:

    def __init__(self, players):
        self.__observers = []
        self.init_game(players)

    def init_game(self, players):
        """
        Sets up an initial game of Othello with the given players (must be exactly 2).
        The first player in the list is assigned the black tokens, and the second white
        Initializes the game tree.
        """
        self.__black_player = players[0]
        self.__white_player = players[1]
        self.__black_player.set_color(BLACK)
        self.__white_player.set_color(WHITE)
        self.__game_tree = GameTree(Board(), BLACK)

    def play_game(self):
        """
        Plays a game of Othello.
        -> Void
        """
        while(not self.__game_tree.is_game_over()):
            if (self.__game_tree.curr_turn == BLACK):
                move = self.__black_player.get_move()
            else:
                move = self.__white_player.get_move()
        return move # get rid of this >:(
            # check that move is valid and apply it or something

