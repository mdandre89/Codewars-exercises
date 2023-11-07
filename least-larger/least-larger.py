def least_larger(a, i): 
    m = a[i]
    zz = sorted(zip(a, range(len(a))))
    for item, index in zz:
        if m < item:
            return index
    return -1
            