from math import log2

from .word import Space, Word


def minmax(space: Space) -> tuple:
    min_case = (999, (0, 0, 0, 0, 0), Word(''), Space())
    for word in space:
        word_map = space.map(word)
        max_case = (0, (0, 0, 0, 0, 0), Word(''), Space())
        for group, space in word_map.items():
            case = (len(space), group, word, space)
            max_case = max(max_case, case)
        min_case = min(min_case, max_case)

    return min_case


def max_space(space: Space) -> tuple:
    max_case = (0, Word(''))
    for word in space:
        max_case = max(max_case, (len(space.map(word)), word))

    return max_case


def max_entropy(space: Space, guess_space: Space = None) -> tuple:
    best = (0, Word(''))
    guess_space = guess_space or space
    for word in guess_space:
        bit_list = []
        for gr, sp in space.map(word).items():
            bit_list.append((log2(len(space)/len(sp)), len(sp)))
        entropy = sum(((size/len(space)*bits for bits, size in bit_list)))
        best = max(best, (entropy, word))

    return best
