def compute_sum(n):
    i = 0
    t = 0
    while i <=n:
        t += sum(int(j) for j in str(i))
        i+=1
    return t