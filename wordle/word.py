from collections import defaultdict

from wordle.utils import word_to_number, PRIME_MAP


class Word:
    def __init__(self, word):
        self.word = word
        self.prime = word_to_number(word)

    def guess(self, guess):
        total = self.prime
        score = [0] * 5
        points = 0
        for i, (a, g) in enumerate(zip(self.word, guess.word)):
            if g == a:
                score[i] = 2
                total /= PRIME_MAP[g]
                points += 2

        for i, (a, g) in enumerate(zip(self.word, guess.word)):
            if g != a and total % PRIME_MAP[g] == 0:
                score[i] = 1
                total /= PRIME_MAP[g]
                points += 1
        return points, tuple(score)

    def is_unique(self):
        return len(self.word) == len(set(self.word))

    def __repr__(self):
        return self.word

    def __len__(self):
        return len(self.word)

    def __lt__(self, other):
        return self.word < other.word


class Space:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words

    def map(self, word):
        word_map = defaultdict(Space)
        for w in self:
            _, s = w.guess(word)
            word_map[s].append(w)

        return word_map

    def only_unique(self):
        words = []
        for word in self.words:
            if len(set(word)) == len(word):
                words.append(word)

        self.words = words

    def filter(self, word, score=None):
        results = []
        for w in self.words:
            _, s = w.guess(word)
            if s == score:
                results.append(w)
        return Space(results)

    def __iter__(self):
        return (w for w in self.words)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return str([w for w in self.words]) if len(self) < 30 else f'{len(self)} words in space'

    def append(self, word):
        self.words.append(word)

