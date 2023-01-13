from collections import Counter
def missing_values(seq): 
    c = Counter(seq).most_common()[-2:]
    return c[1][0]**2 *c[0][0]