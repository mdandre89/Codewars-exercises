def box(ls):
    nw0, nw1 = max(i[0] for i in ls), min(i[1] for i in ls)
    se0, se1 = min(i[0] for i in ls), max(i[1] for i in ls)
    return { "nw": [nw0,nw1], "se": [se0,se1] }