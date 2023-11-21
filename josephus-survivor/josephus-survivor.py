def josephus_survivor(n,k):
    e = list(range(1,n+1))
    i = k-1
    t = []
    while e:
        while i >= len(e):
            i = i%len(e)
        t.append(e.pop(i))
        i += k-1  
    return t[-1]