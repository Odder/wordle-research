from collections import defaultdict

from wordle.utils import word_to_number, PRIME_MAP


class Word:
    def __init__(self, word: str):
        self.word = word
        self.prime = word_to_number(word)

    def guess(self, guess) -> tuple:
        total = self.prime
        score = [0] * 5
        checks = [
            (2, lambda a, g: a == g),
            (1, lambda a, g: a != g and total % PRIME_MAP[g] == 0),
        ]

        for points, check in checks:
            for i, (ans, gue) in enumerate(zip(self.word, guess.word)):
                if check(ans, gue):
                    score[i] = points
                    total /= PRIME_MAP[gue]

        return tuple(score)

    def is_unique(self) -> bool:
        return len(self.word) == len(set(self.word))

    def __repr__(self):
        return self.word

    def __len__(self):
        return len(self.word)

    def __lt__(self, other):
        return self.word < other.word

    def __eq__(self, other):
        return self.word == other.word


class Space:
    def __init__(self, words=None):
        self.words = words or []

    def map(self, word: Word) -> defaultdict:
        word_map = defaultdict(Space)
        for w in self:
            word_map[w.guess(word)].append(w)

        return word_map

    def only_unique(self) -> None:
        self.words = [word for word in self.words if word.is_unique()]

    def filter(self, word: Word, score: tuple = None):
        return Space([w for w in self.words if w.guess(word) == score])

    def append(self, word: Word) -> None:
        self.words.append(word)

    def __iter__(self):
        return (w for w in self.words)

    def __len__(self):
        return len(self.words)

    def __contains__(self, item):
        return item in self.words

    def __repr__(self):
        return str([w for w in self.words]) if len(self) < 30 else f'{len(self)} words in space'

