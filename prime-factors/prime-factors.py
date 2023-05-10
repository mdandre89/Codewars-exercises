def prime_factors (n):
    t = []
    j = 2
    while n>1:
        if n%j==0:
            while( n%j==0):
                t.append(j)
                n = n/j
        j+=1
    return t