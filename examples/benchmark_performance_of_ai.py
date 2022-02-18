from multiprocessing import Pool, cpu_count

from wordle import Game, Word
from wordle.algorithms import alg_max_entropy, alg_random
from wordle.words import words


def p_play(answer, algorithm, guesses):
    return Game(
        solution=answer,
        guesses=guesses,
        algorithm=algorithm
    ).play()


def benchmark(alg=alg_random, guesses=None):
    with Pool(cpu_count()) as p:
        results = p.starmap(p_play, ((Word(w), alg, guesses) for w in words))

    return results


"""
Benchmarks the performance of a specific game setup
"""

if __name__ == '__main__':
    print(sum(benchmark(guesses=[Word('crane')], alg=alg_max_entropy)) / 2315)
    # print(sum(benchmark(guesses=[Word(w) for w in ['spilt', 'crane']], alg=alg_max_entropy)) / 2315)
