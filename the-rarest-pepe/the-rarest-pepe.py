import collections
def find_rarest_pepe(pepes):
    c = sorted(collections.Counter(pepes).most_common(), key = lambda a: (-a[-1],a[0]))
    ls = [i[0] for i in c if i[1]==c[-1][1]]
    if c[-1][1] >= 5:
        return 'No rare pepes!'
    return ls if len(ls)>1 else ls[0]
    