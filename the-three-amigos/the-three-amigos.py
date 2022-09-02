def three_amigos(ls):
    if len(ls)==3 and check(ls):
        return ls
    s = [max(ls)+1,min(ls)]
    m = 0
    for i,j in enumerate(ls[:-2]):
        t = ls[i:i+3]
        print(t, check(t),abs(max(s)-min(s)), abs(max(t)-min(t)) )
        if check(t) and abs(max(t)-min(t))<abs(max(s)-min(s)):
            m = 1
            s = t
    return s if m else []
    
def check(t):
    return t[0]%2==t[1]%2==t[2]%2