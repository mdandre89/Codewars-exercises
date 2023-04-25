def range_function(*ls):
    s = 1
    if len(ls) == 1:   
        j = 0
        z = ls[0]
    elif len(ls) == 2:
        j = ls[0] -1
        z = ls[1]
    else:
        j = ls[0] -ls[1]
        z = ls[2]
        s = ls[1]
    while j<=z-s:
        j+=s
        yield j