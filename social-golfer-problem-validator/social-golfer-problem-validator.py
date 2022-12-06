from collections import Counter as c
import re
def valid(ls):
    players = ''.join(ls[0])
    n = len(players)
    lg = len(ls[0][0])
    for i in ls:
        for j in i:
            if len(j) != lg:    
                return False
    for i in ls:
        s = c(''.join(i))
        if len(s.keys()) != n or set(s)!=set(players):
            return False
    ls2 = '-'.join("-".join(i) for i in ls)        
    for i in players:
        rex = r'[A-Z]*'+ i + '[A-Z]*'
        ma = ''.join(re.findall(rex,ls2)).replace(i,"")
        ma2 = c(ma)
        if len(set(ma2)) != len(ma):
            return False
    return True       