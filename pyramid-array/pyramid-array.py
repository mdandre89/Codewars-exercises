def pyramid(n):
    ls = []
    for i in range(1, n+1):
        ls.append([1]*i)
    return ls