from board import Board
from constants import BLACK, WHITE
from minimax_player import MinimaxPlayer
from referee import Referee

def board_test():
    b = Board()
    moves = b.get_valid_moves(BLACK)
    print(moves == [(2, 3), (4, 5), (3, 2), (5, 4)])

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

def minimax_test():
    player1 = MinimaxPlayer()
    player2 = MinimaxPlayer()
    ref = Referee([player1, player2])
    scores = ref.play_game()
    print("MINIMAX GAME RESULTS: ", scores)

minimax_test()
# board_game_test()
# board_test()