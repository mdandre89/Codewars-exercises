from collections import Counter
def getWinner(ls):
    c = Counter(ls).most_common(1)
    return c[0][0] if c[0][1]> len(ls)//2 else None