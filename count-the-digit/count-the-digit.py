def nb_dig(n, d):
    return "".join([str(j*j) for j in range(n+1)]).count(str(d)) 