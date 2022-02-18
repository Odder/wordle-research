from wordle import Game, Word
from wordle.algorithms import alg_max_entropy
from wordle.printers import simple as printer_simple


""" Make user play a single normal game """
if __name__ == '__main__':
    while True:
        print('\nNEW GAME!!\n')
        game = Game(
            guesses=[],
            printer=printer_simple,
            algorithm=alg_max_entropy,
            manual_guess=True
        )
        game.play()

        print('\nTIME FOR AI!!\n')

        gameAI = Game(
            solution=game.solution,
            guesses=[Word('crane')],
            printer=printer_simple,
            algorithm=alg_max_entropy
        )
        gameAI.play()
