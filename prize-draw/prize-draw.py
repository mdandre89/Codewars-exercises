import string
def rank(st, we, n):
    if not st:    
        return "No participants"
    if n > len(we):
        return "Not enough participants"
    t = []    
    for j,i in enumerate(st.split(",")):
        s = len(i)
        for z in i:
            s += string.ascii_lowercase.index(z.lower())+1
        s *= we[j]
        t.append((i,s))
    t = sorted(t,key=lambda tup: (-tup[1],tup[0]))
    return t[n-1][0]