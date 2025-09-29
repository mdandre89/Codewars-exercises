def tower_builder(n):
    t = []
    for i in range(1,n+1):
        t.append(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))
    return t if n>1 else ['*']