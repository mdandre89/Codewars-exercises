def ranks(ls):
    return [ sorted(ls)[::-1].index(i)+1 for i in ls]