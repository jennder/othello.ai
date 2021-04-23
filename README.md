# othello.ai
an AI that plays games

## Example Usage
To download all relevant Python packages, run:

`pip install -r requirements.txt`

To run the tournament with all players, run:

`python tournament.py`

## Directory Structure:
```
board.py                # Internal representation of the Othello game board
constants.py            # Gameplay constants, including player_types
*_player.py             # The different AI players
player_interface.py     # All methods which need to be overriden by AI players
referee.py              # The referee who runs each game in the tournament
tournament.py           # Script to run the tournament of all players in player_types (see constants.py)
test.py                 # Scratch file for ad hoc testing 1v1 players
```