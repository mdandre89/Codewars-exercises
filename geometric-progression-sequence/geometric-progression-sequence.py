def geometric_sequence_elements(a, r, n):
    return ", ".join([str(a*r**j) for  j in range(0,n)])