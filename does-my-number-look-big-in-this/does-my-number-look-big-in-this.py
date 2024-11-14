def narcissistic( n ):
    l = len(str(n))
    return n == sum(map(lambda x : int(x)**l,list(str(n))))