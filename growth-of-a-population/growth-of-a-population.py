def nb_year(p0, percent, aug, p):
    y = 0
    while p0<p:
        y+=1
        p0 = p0*(1+percent/100) +aug
    return y
    