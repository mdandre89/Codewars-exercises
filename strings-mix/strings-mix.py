from collections import Counter as c
import re
def mix(s1, s2):     
    t = []
    ss1=c(re.sub(r"[^a-z]","",re.sub(r"[^a-z]","",s1)))
    ss2=c(re.sub(r"[^a-z]","",re.sub(r"[^a-z]","",s2)))
    for i in set(list((ss1+ss2).elements())):
        if ss1[i]>1 or ss2[i]>1:
            if ss1[i] > ss2[i]:
                t.append([i*ss1[i],"1"])
            elif ss1[i] < ss2[i]:    
                t.append([i*ss2[i],"2"])
            else:
                t.append([i*ss2[i],"="])
    t = sorted(t,key=lambda x: (-len(x[0]),x[1],x[0]))    
    return "/".join(k+":"+i for i,k in t)