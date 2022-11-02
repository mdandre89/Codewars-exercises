def solve(a,b):
    for i in set(b):
        if b.count(i) > a.count(i):
            return 0
        a = a.replace(i,"",b.count(i))
    return len(a)