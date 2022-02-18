from random import randint

from .word import Space, Word
from .words import words
from .algorithms import alg_random
from .printers import void as void_printer


class Game:
    def __init__(self, solution: Word = None, algorithm=None, guesses=None, printer=None, manual_feedback=False, manual_guess=False):
        self.solution = solution or Word(words[randint(0, len(words) - 1)]) if not manual_feedback else None
        self.full_space = Space(words=[Word(w) for w in words])
        self.space = Space(words=[Word(w) for w in words])
        self.algorithm = algorithm or alg_random
        self.printer = printer or void_printer
        self.pre_guesses = guesses or []
        self.manual_feedback = manual_feedback
        self.manual_guess = manual_guess
        self.guesses = []
        self.round = 0
        self.is_won = False

    def play(self) -> int:
        while not self.is_won:
            guess = self.suggest_guess() if not self.manual_guess else Word(input('Enter guess: '))
            feedback = self.guess(guess)
            self.printer(self, guess, feedback)

        return self.round

    def suggest_guess(self):
        if self.round >= len(self.pre_guesses):
            return self.algorithm(self.full_space, self.space)
        return self.pre_guesses[self.round]

    def guess(self, guess):
        self.guesses.append(guess)
        self.round += 1
        feedback = self.solution.guess(guess) if not self.manual_feedback else self.get_feedback(guess)
        if feedback == (2, 2, 2, 2, 2):
            self.is_won = True
        self.space = self.space.filter(guess, feedback)
        return feedback

    def get_feedback(self, guess):
        return tuple(int(i) for i in input(f'Guessed "{guess}", what was the feedback? ').split())
