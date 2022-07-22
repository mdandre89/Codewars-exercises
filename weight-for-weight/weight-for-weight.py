def order_weight(strng):
    t = strng.split()
    l = len(t)
    for j in range(len(t)-1,0,-1):
        for i in range(j):
            if sum([int(s) for s in str(t[i])])>sum([int(s) for s in str(t[i+1])]):
                t[i],t[i+1] = t[i+1],t[i]
            elif sum([int(s) for s in str(t[i])])==sum([int(s) for s in str(t[i+1])]):
                if  t[i]>t[i+1]:
                    t[i],t[i+1] = t[i+1],t[i]
    return " ".join(t)
        