def sum_of_threes(n):
    try:
        s = []
        t =  ternary(n)
        if t.count("2"):
            return "Impossible"
        for i,j in enumerate(t[::-1]):
            if j =="1":
                s.append("3^"+str(i))
        return "+".join(s[::-1])
    except:
        return "Impossible"
        
def ternary(n,b=3):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e, b) + str(q)