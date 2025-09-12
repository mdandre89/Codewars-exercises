from collections import Counter
def validate_word(word):
    c = Counter(word.lower())
    return c.most_common()[0][1] == c.most_common()[-1][1]