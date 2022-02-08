from multiprocessing import Pool
from random import randint
from collections import Counter
from math import log2
from wordle.heuristics import minmax, max_space, max_entropy
from wordle.words import words
from wordle.word import Word, Space

space = Space(words)
space.words.sort()
bests = []


def quality_of_comb(word, word2, space):
    print(f"*** {word} - {word2} ***")
    word_map = space.map(word)
    k = 1
    l = 1
    solutions = [[], [], [], [], []]
    for group, space in word_map.items():
        if len(space) < 2:
            solutions[0].append((k, space, (group,)))
            print(f"{k: >3}: {group} -> {space}")
            k += 1
        else:
            word2_map = space.map(word2)
            for group2, space2 in word2_map.items():
                solutions[1].append((k, space2, (group2,)))
                if len(space2) < 2:
                    solutions[0].append((l, space2, (group2,)))
                    print(f"{l: >3}: {group} -> {group2} -> {space2}")
                    l += 1


def search_word_comb_minmax(word, candidates, space):
    word_map = space.map(word)
    best = (9999, Word(''), [])
    for i, word2 in enumerate(candidates.words):
        if not word2.is_unique() or word2 < word:
            continue
        dist = [0]*100
        #print(f'Testing with word: {word2} ({i}/{len(candidates)})')
        for gr, sp in word_map.items():
            #print(f'Testing new group: {gr}')
            worst_case = (0, gr, (0, 0, 0, 0, 0), Space())
            for gr2, sp2 in sp.map(word2).items():
                case = (len(sp2), gr, gr2, sp2)
                worst_case = max(worst_case, case)

                #print(gr, gr2)
                case = minmax(sp2)

                dist[case[0]] += 1
                if case[0] > 10:
                    pass
                    #print(case)

        s = 0
        j = 0
        for n, k in enumerate(dist):
            j += k
            s += (n**2) * k
        best = min(best, (s / j, word2, dist))
    return best


def search_word_comb_bits(word, candidates, space):
    word_map = space.map(word)
    best = (0, Word(''))
    for i, word2 in enumerate(candidates.words):
        if not word2.is_unique() or word2 < word:
            continue
        dist = [0]*100
        #print(f'Testing with word: {word2} ({i}/{len(candidates)})')
        bit_list = []
        for gr, sp in word_map.items():
            #print(f'Testing new group: {gr}')
            for gr2, sp2 in sp.map(word2).items():
                bit_list.append((log2(2315/len(sp2)), len(sp2)))
        entropy = sum(((size/2315)*bits for bits, size in bit_list))
        best = max(best, (entropy, word2))
        if entropy > 9.4:
            bests.append((entropy, word, word2))
            print(f' *** {word} - {word2} ({entropy:.2f}) ***')
    return best


def p_search(word):
    if not word.is_unique():
        return
    cands = Space()
    cands.words = space.filter(word, (0, 0, 0, 0, 0))
    entropy, word2 = search_word_comb_bits(word, cands, space)
    return entropy, word, word2
    #print(f' *** {word} - {w2} ({avg:.2f}) ***')


def search_best_combo():
    with Pool(8) as p:
        results = p.map(p_search, space.words)
        bests.sort(reverse=True)
        print('')
        print('RANKINGS!')
        for i, (entropy, w1, w2) in enumerate(bests[:50]):
            pos = i + 1
            print(f'{pos: >2}) {w1} - {w2} ({entropy})')


if __name__ == '__main__':
    # for w1, w2 in [('crane', 'spilt'), ('blast', 'price'),  ('clasp', 'tried')]:  # ('spilt', 'crane'), ('blast', 'price'), ('price', 'blast'),  ('clasp', 'tried'), ('tried', 'clasp'),
    #     quality_of_comb(Word(w1), Word(w2), space)
    #     print('')
    with Pool(8) as p:
        for w1, w2 in [
            (Word('crane'), Word('spilt')),
            (Word('spilt'), Word('crane')),
            (Word('salon'), Word('trice')),
            (Word('trice'), Word('salon')),
            (Word('cairn'), Word('stole')),
            (Word('stole'), Word('cairn')),
            (Word('close'), Word('train')),
            (Word('train'), Word('close')),
            (Word('coast'), Word('liner')),
            (Word('liner'), Word('coast')),
            (Word('cried'), Word('slant')),
            (Word('slant'), Word('cried')),
            (Word('clone'), Word('stair')),
            (Word('stair'), Word('clone')),
            (Word('price'), Word('slant')),
            (Word('slant'), Word('price')),
            (Word('scone'), Word('trail')),
            (Word('trail'), Word('scone')),
        ]:
            results = p.starmap(play, [([w1, w2], w) for w in space])
            dist = Counter(results)
            avg = sum(results) / len(results)
            print(f'{w1} - {w2}\n{avg:.4f}     ({dist})')
            print('')


