import re 
from collections import Counter as c
def mix(s1, s2):
    t = []
    c1 = c(re.sub("[^a-z]","",s1))
    c2 = c(re.sub("[^a-z]","",s2))
    for j in set(c1.keys()).union(c2.keys()):
        m, n = c1[j], c2[j]
        if m>n and m>1:
            t.append([c1[j],j,"1"])
        elif n>m and n>1:
            t.append([c2[j],j,"2"])
        elif n>1:
            t.append([c2[j],j,"="])
    return "/".join(k+":"+j*i for i,j,k in sorted(t, key=lambda x: (-x[0],x[2],x[1])))
