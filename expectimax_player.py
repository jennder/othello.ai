from minimax_player import MinimaxPlayer

"""A minimax player who maximizes their move assuming
others are adversarial players. Depth 2 by default.
"""
class ExpectimaxPlayer(MinimaxPlayer):

    def __init__(self, depth=2):
        super().__init__(depth)

    def get_best_action(self, maximize, move_scores):
        """
        Get the best move, either maximize or find the average the score

        Boolean [Listof (Move, Natural)] -> (Move, Natural)
        """
        if maximize:
            return max(move_scores, key=lambda m: m[1])
        else:
            scores = [m[1] for m in move_scores]
            avg_score = sum(scores) / len(scores)
            return (None, avg_score)
        