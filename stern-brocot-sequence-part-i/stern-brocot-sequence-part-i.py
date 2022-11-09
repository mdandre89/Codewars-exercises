def stern_brocot(n):   
    i = 1
    ls = [1,1]
    while n not in ls:
        ls = ls + [ls[i-1]+ls[i],ls[i]]
        i+=1
    return ls.index(n)