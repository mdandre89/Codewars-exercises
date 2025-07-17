def pattern(n):
    s = ""
    t = []
    while n>0:
        s += str(n)
        t.append(s)
        n=n-1
    return "\n".join(t[::-1])