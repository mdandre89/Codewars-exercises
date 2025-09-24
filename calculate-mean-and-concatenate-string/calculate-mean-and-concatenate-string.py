def mean(lst):
    n=[]
    cr=[]
    for c in lst:
        if c.upper()==c.lower():
            n.append(int(c))
        else:
            cr.append(c)
            print c
    if len(n)==0:
        mean=0
    else:
        mean=sum(n)/float(len(n))
    l="".join(cr)
    s=[mean, l]  
    return s