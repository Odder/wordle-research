from wordle import Game, Word
from wordle.algorithms import alg_max_entropy
from wordle.printers import simple as printer_simple

"""
Plays a game where the user defines the feedback. The answer is unknown to the computer ahead of time and has
to rely on your feedback in the shape of inputs like "0 0 0 0 2"
"""

if __name__ == '__main__':
    game = Game(
        guesses=[Word('crane')],
        printer=printer_simple,
        algorithm=alg_max_entropy,
        manual_feedback=True
    )
    game.play()
