def goldbach_partitions(n):
    if n % 2 == 1:
        return []
    s,t = set(), set()
    for i in range(2,n):
        if i not in t:
            s.add(i)
        for j in range(i,n,i):
            t.add(j)
    r = []
    t = set()
    for i in sorted(s):
        if n-i in s and n-i not in t:
            t.add(i)
            t.add(n-i)
            if i >= n-1:
                r.append(str(n-i)+"+"+str(i))
            else:
                r.append(str(i)+"+"+str(n-i))
    return r