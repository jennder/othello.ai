from constants import BLACK, WHITE, SKIP
from board import Board
from game_tree import GameTree

DEBUG = False

"""
The referee oversees the playing of a game of Othello between two players,
ensures that valid moves are made, and determines the winner.
"""
class Referee:

    def __init__(self, players):
        self.__observers = []
        self.__init_game(players)

    def __init_game(self, players):
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
        self.__black_player.set_gametree(GameTree(Board(), BLACK))
        self.__white_player.set_gametree(GameTree(Board(), BLACK))

        while(not self.__game_tree.is_game_over()):
            if (self.__game_tree.curr_turn == BLACK):
                move = self.__black_player.get_move(self.__game_tree.board)
            else:
                move = self.__white_player.get_move(self.__game_tree.board)
            valid_actions = self.__game_tree.get_actions()
            if (move == SKIP and SKIP in valid_actions) or move in valid_actions:
                self.update_players(move)
                self.__game_tree = self.__game_tree.apply_move(move)
                if DEBUG:
                    print("%s MOVED %s" % (self.__game_tree.curr_turn, move))
                    self.__game_tree.board.render()
        return { BLACK: self.__game_tree.get_score(BLACK), WHITE: self.__game_tree.get_score(WHITE) }
    
    def update_players(self, move):
        self.__black_player.update_move(move)
        self.__white_player.update_move(move)
