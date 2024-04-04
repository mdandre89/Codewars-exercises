def halving_sum(n): 
    s=0
    while n>1:
        s+=n
        n = n >>1
    return s+1