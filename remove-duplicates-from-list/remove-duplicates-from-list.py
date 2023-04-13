def distinct(seq):
    t = []
    for j in seq:
        if j not in t:
            t.append(j)
    return t