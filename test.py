from board import Board
from constants import BLACK, WHITE
from minimax_player import MinimaxPlayer
from greedy_player import GreedyPlayer
from random_player import RandomPlayer
from referee import Referee

def board_test():
    b = Board()
    moves = b.get_valid_moves(BLACK)
    print(moves == [(2, 3), (4, 5), (3, 2), (5, 4)])

    for i in range(0, 3):
        for j in range(0,3):
            b.board[j][i] = BLACK
    b.board[1][1] = None
    b.render()
    print(b.get_valid_moves(BLACK))

def board_game_test():
    b = Board()
    b.render()
    for _ in range(0, 20):
        moves = b.get_valid_moves(BLACK)
        print("MOVES", moves, BLACK)
        new_b = b.apply_move(moves[0], BLACK)
        new_b.render()
        moves = new_b.get_valid_moves(WHITE)
        print("MOVES", moves, WHITE)
        new_w = new_b.apply_move(moves[0], WHITE)
        new_w.render()
        b = new_w

def game_test(player1, player2):
    ref = Referee([player1, player2])
    scores = ref.play_game()
    print("MINIMAX GAME RESULTS: ", scores)

# game_test(MinimaxPlayer(), MinimaxPlayer())
# game_test(GreedyPlayer(), GreedyPlayer())
# game_test(RandomPlayer(), RandomPlayer())
# board_game_test()
# board_test()