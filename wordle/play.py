from random import randint

from .word import Space, Word
from .words import words


class Game:
    def __init__(self, solution=None, algorithm=None, guesses=None, printer=None):
        self.solution = solution if solution else words[randint(0, len(words) - 1)]
        self.algorithm = algorithm if algorithm else alg_random
        self.printer = printer if printer else printer_void
        self.pre_guesses = guesses if guesses else []

    def play(self):
        full_space = Space(words=[Word(w) for w in words])
        space = Space(words=[Word(w) for w in words])
        guess = Word('')
        guesses = []
        k = 0

        while str(guess) != str(self.solution):
            guess = self.algorithm(full_space, space) if k >= len(self.pre_guesses) else self.pre_guesses[k]
            guesses.append(guess)
            feedback = self.solution.guess(guess)[1]
            space = space.filter(guess, feedback)
            k += 1
            self.printer(space, guess, feedback, k)

        return k


def printer_simple(space, guess, hints, k):
    print(f'{k}: {guess} -> {hints} {space}')


def printer_void(space, guess, hints, k):
    return
