from wordle import Game, Word
from wordle.algorithms import alg_max_entropy
from wordle.printers import simple as printer_simple

""" Make it play a single normal game """

if __name__ == '__main__':
    game = Game(
        solution=Word('robin'),
        guesses=[Word('crane')],
        printer=printer_simple,
        algorithm=alg_max_entropy
    )
    game.play()
