def pascal(p):
    t = [[1],[1,1]]
    for i in range(p-2):
        m = t[-1]
        s = [m[i]+m[i+1] for i in xrange(len(m)-1)]
        t.append([1]+s+[1])
    return t if p > 1 else [[1]]