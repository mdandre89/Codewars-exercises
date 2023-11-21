def josephus(items,k):
    l = len(items)
    return [items[(i-1)%l] for i in josephus_survivor(l,k)]
    
    
def josephus_survivor(l, s):
    e=[i for i in range(1,l+1)]
    d=[]
    x=0
    while e:
        x+=s-1
        while x>=len(e):
            x=x-len(e)
        d.append(e.pop(x))
    return d