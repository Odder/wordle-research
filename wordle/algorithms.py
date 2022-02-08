from random import randint

from .heuristics import max_entropy, minmax


def alg_random(full_space, space):
    return space.words[randint(0, len(space)-1)]


def alg_max_entropy(full_space, space):
    return max_entropy(space)[1]


def alg_minmax_space(full_space, space):
    return minmax(space)[1]