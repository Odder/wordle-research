from wordle.words import words
from collections import Counter

if __name__ == '__main__':
    scorer = []
    scores = []
    for x in zip(*words):
        scorer.append(Counter(x))
    for w in words:
        for w2 in words:
            if len(w + w2) != len(set(w + w2)):
                continue
            score = sum(scorer[i % 5][c] for i, c in enumerate(w + w2))
            scores.append((score, w, w2))
    scores.sort(reverse=True)
    for entry in scores[:25]:
        print(entry)
