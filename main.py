from multiprocessing import Pool, cpu_count

from wordle import Game, Word, printer_simple, printer_void
from wordle.algorithms import alg_max_entropy, alg_random
from wordle.words import words


def p_play(answer, algorithm, guesses):
    return Game(
        solution=answer,
        guesses=guesses,
        printer=printer_void,
        algorithm=algorithm
    ).play()


def benchmark(alg=alg_random, guesses=None):
    with Pool(cpu_count()) as p:
        results = p.starmap(p_play, ((Word(w), alg, guesses) for w in words))

    return results


if __name__ == '__main__':
    """ Run a benchmark """
    # print(sum(benchmark()) / 2315)
    # print(sum(benchmark(guesses=[Word(w) for w in ['spilt', 'crane']], alg=alg_max_entropy)) / 2315)

    """ Make it play a single normal game """
    game = Game(
        solution=Word('frame'),
        guesses=[Word('crane')],
        printer=printer_simple,
        algorithm=alg_max_entropy)
    game.play()
