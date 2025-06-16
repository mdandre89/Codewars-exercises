def data_reverse(v):
    return sum([v[i-8:i] for i in range(len(v),0,-8)],[])