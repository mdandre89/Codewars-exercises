def two_sum(ls, n):
    l = len(ls)
    for i in range(l):
        for j in range(i+1,l):
            if ls[i] + ls[j] == n:
                return [i,j]