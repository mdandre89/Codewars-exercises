def x(n):
    t = []
    for i in range(n//2):
        t.append([0]*i + [1] + [0]*(n-2*i-2) + [1] + [0]*i)
    if n % 2 == 1:
        return t + [[0]*(n//2) + [1] + [0]*(n//2)] + t[::-1]
    return  t + t[::-1]