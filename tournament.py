from minimax_player import MinimaxPlayer
from greedy_player import GreedyPlayer
from random_player import RandomPlayer
from expectimax_player import ExpectimaxPlayer
from ids_player import IterativeDeepeningPlayer
from alphabeta_player import AlphaBetaPlayer
from heuristic_player import HeuristicPlayer
from referee import Referee
from constants import player_types, BLACK, WHITE

from collections import Counter
import pandas as pd

def player_factory(name):
    """
    Returns a new player object of the given type
    """
    players = {
        "RANDOM": RandomPlayer(),
        "GREEDY": GreedyPlayer(),
        "MINIMAX": MinimaxPlayer(),
        "EXPECTIMAX": ExpectimaxPlayer(),
        "IDS": IterativeDeepeningPlayer(),
        "ALPHABETA": AlphaBetaPlayer(),
        "HEURISTIC": HeuristicPlayer(),
        "MINIMAX3": MinimaxPlayer(3),
        "MINIMAX1": MinimaxPlayer(1)
    }
    return players[name]

# Data columns to be saved in the results CSV
data = {
    BLACK: [],
    WHITE: [],
    "BLACK_SCORE": [],
    "WHITE_SCORE": [],
    "WINNER": [],
    "DIFFERENCE": []
}

def add_to_data(new_data):
    for key, val in new_data:
        data[key] = data[key] + [val]

def run_game(nameA, nameB):
    """
    Play a game of othello with the two types of players given, and add the
    results to the data to be saved as a csv.
    If there is a random player, play this game 3 times and record the results
    based on the average of the three
    """
    print("Playing %s vs %s" % (nameA, nameB))
    playerA = player_factory(nameA)
    playerB = player_factory(nameB)
    ref = Referee([playerA, playerB])
    score = ref.play_game()
    black_score = score[BLACK]
    white_score = score[WHITE]

    # Play three times and average if there is a random player
    if "RANDOM" in [nameA, nameB]:
        for _ in range(0, 2):
            print("and another")
            playerA = player_factory(nameA)
            playerB = player_factory(nameB)
            ref = Referee([playerA, playerB])
            score = ref.play_game()

            black_score += score[BLACK]
            white_score += score[WHITE]
        black_score = black_score / 3
        white_score = white_score / 3

    if black_score > white_score:
        winner = BLACK
    elif black_score == white_score:
        winner = None
    else:
        winner = WHITE

    add_to_data([
        (BLACK, nameA.lower()),
        (WHITE, nameB.lower()),
        ("BLACK_SCORE", black_score),
        ("WHITE_SCORE", white_score),
        ("WINNER", winner),
        ("DIFFERENCE", abs(black_score - white_score) / (black_score + white_score))
    ])

def run_tournament():
    """
    Run every type of player against each other and itself in a round robin format.
    If the two players are not the same type, the players will play two games,
    switching who is the black versus white player in each game
    Saves the results of the games in a CSV file
    """
    for i, nameA in enumerate(player_types):
        for nameB in player_types[i:]:
            run_game(nameA, nameB)
            if not nameA == nameB:
                run_game(nameB, nameA)

    df = pd.DataFrame(data=data)
    df.to_csv("tournament.csv")

def analyze():
    df = pd.read_csv("tournament.csv")
    data = df.to_dict(orient="list")
    black_col = data[BLACK]
    white_col = data[WHITE]
    winner_col = data["WINNER"]

    winners = [black_col[i] if w == BLACK else white_col[i] for i, w in enumerate(winner_col) if w]
    print(Counter(winners))
    print(Counter(winner_col))

def run_baby():
    """
    Only run minimax1 player against other players
    """
    nameB = "MINIMAX1"
    for nameA in player_types[:-1]:
        run_game(nameA, nameB)
        if not nameA == nameB:
            run_game(nameB, nameA)

    df = pd.DataFrame(data=data)
    df.to_csv("baby.csv")

# analyze()
# run_tournament()
run_baby()
