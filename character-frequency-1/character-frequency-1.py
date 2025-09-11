import collections, re
def letter_frequency(text):
    c = collections.Counter(re.sub(r"[^A-Za-z]","",text).lower())
    return sorted([(i, c[i]) for i in c.keys()],key=lambda x: (-x[1], x[0]))