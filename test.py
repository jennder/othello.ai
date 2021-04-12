from board import Board
from constants import BLACK, WHITE

b = Board()
b.render()
for _ in range(0, 5):
    moves = b.get_valid_moves(BLACK)
    print("MOVES", moves, BLACK)
    new_b = b.apply_move(moves[0], BLACK)
    new_b.render()
    moves = new_b.get_valid_moves(WHITE)
    print("MOVES", moves, WHITE)
    new_w = new_b.apply_move(moves[0], WHITE)
    new_w.render()
    b = new_w