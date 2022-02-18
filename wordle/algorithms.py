from random import randint
from functools import lru_cache

from .word import Space, Word
from .heuristics import max_entropy, minmax


@lru_cache(maxsize=10000)
def alg_random(full_space: Space, space: Space) -> Word:
    return space.words[randint(0, len(space)-1)]


@lru_cache(maxsize=10000)
def alg_max_entropy(full_space: Space, space: Space) -> Word:
    return max_entropy(space, guess_space=full_space)[1]


@lru_cache(maxsize=10000)
def alg_minmax_space(full_space: Space, space: Space) -> Word:
    return minmax(space)[1]
