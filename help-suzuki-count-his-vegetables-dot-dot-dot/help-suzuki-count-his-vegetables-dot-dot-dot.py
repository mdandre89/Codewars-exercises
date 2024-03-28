import collections
def count_vegetables(string):
    c = collections.Counter(string.split())
    del c["chopsticks"]
    t = []
    for i,j in c.items():
        t.append((j,i))
        
    return sorted(t,reverse=True)