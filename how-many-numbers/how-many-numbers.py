def sel_number(n, d):
    if n<11:
        return 0
    t = 0
    for i in range(11,n+1):
        j = str(i)
        if j == "".join(sorted(j)):
            if all(0<abs(int(m)-int(n))<=d for m,n in zip(j[:-1],j[1:])):
                t+=1
    return t 