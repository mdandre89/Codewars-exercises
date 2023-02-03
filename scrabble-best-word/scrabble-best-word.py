def get_best_word(points, words):
    dictio = dict(zip('abcdefghijklmnopqrstuvwxyz', points))
    new_words = sorted(words, key=lambda x: (sum(map(lambda y: dictio[y], list(x.lower()))), -len(x)))
    return words.index(new_words[-1])