import collections
def flatten(lst):    
    t= []
    for i in lst:
        if isinstance(i, collections.Iterable):
            for j in i:
                t.append(j)
        else:    
            t.append(i)
    return t