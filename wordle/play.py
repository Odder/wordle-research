from random import randint

from .word import Space, Word
from .words import words
from .algorithms import alg_random


class Game:
    def __init__(self, solution: Word = None, algorithm=None, guesses=None, printer=None):
        self.solution = solution or words[randint(0, len(words) - 1)]
        self.algorithm = algorithm or alg_random
        self.printer = printer or printer_void
        self.pre_guesses = guesses or []

    def play(self) -> int:
        full_space = Space(words=[Word(w) for w in words])
        space = Space(words=[Word(w) for w in words])
        guess = Word('')
        guesses = []
        k = 0

        while guess != self.solution:
            guess = self.algorithm(full_space, space) if k >= len(self.pre_guesses) else self.pre_guesses[k]
            guesses.append(guess)
            feedback = self.solution.guess(guess)
            space = space.filter(guess, feedback)
            k += 1
            self.printer(space, guess, feedback, k)

        return k


def printer_simple(space, guess, hints, k) -> None:
    print(f'{k}: {guess} -> {hints} {space}')


def printer_void(space, guess, hints, k) -> None:
    return
