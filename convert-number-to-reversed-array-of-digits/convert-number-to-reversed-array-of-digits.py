def digitize(n):
    l=len(str(n))
    m=str(n)
    m=m[::-1]
    i=0
    d=[]
    while i<l:
        d.append(int(m[i]))
        i=i+1
    print m
    return d