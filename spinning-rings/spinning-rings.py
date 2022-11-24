def spinning_rings(inner_max, outer_max):    
    i = inner_max
    j = 1
    z = 1
    while i!=j:
        i = i - 1 if i>0 else inner_max
        j = (j + 1)%(outer_max+1)
        z += 1
    return z