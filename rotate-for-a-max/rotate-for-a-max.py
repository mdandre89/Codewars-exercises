def max_rot(n):
    t = [] 
    j = 0
    m=n
    n = str(n)
    while j < len(n):
        n = n[0:j] + n[j+1:] + n[j]
        t.append(int(n))
        j+=1
    return max(max(t),m)