from math import log2

from .word import Space, Word


def minmax(local_space):
    min_case = (999, (0, 0, 0, 0, 0), Word(''), Space())
    for word in local_space:
        word_map = local_space.map(word)
        max_case = (0, (0, 0, 0, 0, 0), Word(''), Space())
        for group, space in word_map.items():
            case = (len(space), group, word, space)
            max_case = max(max_case, case)
        min_case = min(min_case, max_case)

    return min_case


def max_space(local_space):
    max_case = (0, Word(''))
    for word in local_space:
        word_map = local_space.map(word)
        case = (len(word_map), word)
        max_case = max(max_case, case)

    return max_case


def max_entropy(local_space):
    best = (0, Word(''))
    for word in local_space:
        bit_list = []
        for gr, sp in local_space.map(word).items():
            bit_list.append((log2(len(local_space)/len(sp)), len(sp)))
        entropy = sum(((size/len(local_space)*bits for bits, size in bit_list)))
        best = max(best, (entropy, word))

    return best