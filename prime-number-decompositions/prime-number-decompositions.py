def getAllPrimeFactors(n):
    try:
        if int(n)!=n or n <=0:
            return []
    except:
        return []
    if n == 1:
        return [1]
    return prime(n)

def getUniquePrimeFactorsWithCount(n):
    try:
        if int(n)!=n or n <=0:
            return [[],[]]
    except:
        return [[],[]]
    if n == 1:
        return [[1],[1]]
    pre = prime(n)
    t = sorted(list(set(prime(n))))
    s = []
    for i in t:
        s.append(pre.count(i))
    return [t,s]

def getUniquePrimeFactorsWithProducts(n):
    try:
        if int(n)!=n or n <=0:
            return []
    except:
        return []
    if n == 1:
        return [1]
    pre = prime(n)
    t = sorted(list(set(prime(n))))
    s = []
    for i in t:
        s.append(i**pre.count(i))
    return s
    
def prime(n):
    d = 2
    t = []
    while d<=n:
        i = 1
        while n%(d)==0:
            n = n/d
            i+=1
            t.append(d)
        d += 1
    return t