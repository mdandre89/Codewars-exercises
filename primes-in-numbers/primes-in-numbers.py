def primeFactors(n):
    d = 2
    s = ""
    while d<=n:
        i = 1
        while n%(d)==0:
            n = n/d
            i+=1
        if i-1==1:
            s+= "("+str(d)+")"
        elif i-1>1:
            s+= "("+str(d)+"**"+str(i-1)+")"
        d += 1
    return s