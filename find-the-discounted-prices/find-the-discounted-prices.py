import math
def find_discounted(ls):
    t = []
    ls = ls.split()
    ls = [int(i) for i in ls]
    for i in range(len(ls)/2):
        m = max(ls)
        ls.remove(m)
        ls.remove(math.trunc(m*3/4))
        t.append(math.trunc(m*3/4)) 
    t.sort()    
    t = [str(i) for i in t]
    return " ".join(t)