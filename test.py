from board import Board
from constants import BLACK, WHITE

b = Board()
b.render()
for _ in range(0, 5):
    moves = b.get_valid_moves(BLACK)
    print("MOVES", moves, BLACK)
    b.apply_move(moves[0], BLACK)
    b.render()
    moves = b.get_valid_moves(WHITE)
    print("MOVES", moves, WHITE)
    b.apply_move(moves[0], WHITE)
    b.render()