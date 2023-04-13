def unique(integers):
    ls = []
    for i,j in enumerate(integers):
        if integers[0:i].count(j) == 0:
            ls.append(j)
    return ls