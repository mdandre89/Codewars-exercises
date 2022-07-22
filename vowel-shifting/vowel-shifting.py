import re
def vowel_shift(st,n):
    if st ==None or st=="":
        return st  
    
    t = "".join(re.findall(r"[AEIOUaeiou]",st))
    
    ss = re.compile(r"[AEIOUaeiou]").finditer(st)
    
    j=0
    for i in ss:
        z = i.start()
        st = st[:z]+t[(j-n)%len(t)]+st[z+1:]
        j+=1 
    return st